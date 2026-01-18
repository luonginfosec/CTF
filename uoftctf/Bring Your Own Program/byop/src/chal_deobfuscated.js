'use strict';

const fs = require('fs');
const path = require('path');
const readline = require('readline');

// Constants
const PUBLIC_DATA_PATH = '/data/public';
const MAX_FILE_SIZE = 0x1000; // 4096 bytes

// Limits configuration
const limits = {
    maxRegisters: 0x40,        // 64 registers max
    maxConstants: 0x80,        // 128 constants max
    maxBytecode: 0x4000,       // 16384 bytes max bytecode
    maxSteps: 0x927c0,         // 600000 max execution steps
    maxStringLength: 0x200,    // 512 max string length
    maxLineLength: 0x3d090,    // 250000 max input line length
    maxArgs: 0x8,              // 8 max function arguments
    inlineCacheSize: 0x4       // 4 inline cache entries
};

// Allowed capability names
const allowedCapabilities = new Set(['caps']);

// Type identifiers for constants/operations
const typeIds = {
    toString: 0x1,      // a
    math: 0x2,          // b
    io: 0x3,            // c
    pow: 0x4,           // d
    readPublic: 0xa,    // e
    ioVersion: 0xb      // f
};

const validTypes = new Set([
    typeIds.toString,
    typeIds.math,
    typeIds.io,
    typeIds.pow,
    typeIds.readPublic,
    typeIds.ioVersion
]);

// Opcodes for the bytecode interpreter
// Original mapping: p['a']=0x1, p['b']=0x2, p['c']=0x20, p['d']=0x21, 
//                   p['e']=0x30, p['f']=0x31, p['g']=0x32, p['h']=0x60, 
//                   p['i']=0x61, p['j']=0x40, p['k']=0x70
const opcodes = {
    LOAD_CONST: 0x01,       // a: Load constant into register
    LOAD_CAP: 0x02,         // b: Load capability into register
    GET_PROP: 0x20,         // c: Get property from object (NOT 0x3!)
    LOOKUP_METHOD: 0x21,    // d: Lookup method with inline caching (NOT 0x4!)
    CALL: 0x30,             // e: Call function
    RET_REG: 0x31,          // f: Return value from register
    RET_UNDEF: 0x32,        // g: Return undefined
    JUMP: 0x60,             // h: Unconditional jump
    JUMP_IF: 0x61,          // i: Conditional jump
    ADD: 0x40,              // j: Add two registers
    PREPARE_DEOPT: 0x70     // k: Prepare for deoptimization (inline cache hint)
};

// Parse hex string input into Uint8Array
function parseHexInput(input) {
    const trimmed = input.trim();
    
    if (trimmed.length === 0) throw 1;
    if (trimmed.length > limits.maxLineLength) throw 1;
    if (!/^[0-9a-fA-F]+$/.test(trimmed) || trimmed.length & 1) throw 1;
    
    const bytes = new Uint8Array(trimmed.length >> 1);
    for (let i = 0; i < bytes.length; i++) {
        bytes[i] = parseInt(trimmed.slice(i << 1, (i << 1) + 2), 16);
    }
    return bytes;
}

// Read 16-bit unsigned integer (little-endian)
function readUint16(buffer, offset) {
    return buffer[offset] | (buffer[offset + 1] << 8);
}

// Read 16-bit signed integer (little-endian)
function readInt16(buffer, offset) {
    const val = readUint16(buffer, offset);
    return val & 0x8000 ? val - 0x10000 : val;
}

// Read 64-bit float (little-endian)
function readFloat64(buffer, offset) {
    const view = new DataView(buffer.buffer, buffer.byteOffset, buffer.byteLength);
    return view.getFloat64(offset, true);
}

// Read file contents (up to MAX_FILE_SIZE bytes)
function readFileContents(filePath) {
    const stats = fs.statSync(filePath);
    if (!stats.isFile()) return '';
    
    const fd = fs.openSync(filePath, fs.constants.O_RDONLY);
    try {
        const size = Math.min(stats.size, MAX_FILE_SIZE);
        const buffer = Buffer.alloc(size);
        const bytesRead = fs.readSync(fd, buffer, 0, size, 0);
        return buffer.subarray(0, bytesRead).toString('utf8');
    } finally {
        fs.closeSync(fd);
    }
}

// Parse bytecode program from bytes
function parseProgram(bytes) {
    let offset = 0;
    
    const checkBounds = (size) => {
        if (offset + size > bytes.length) throw 1;
    };
    
    // Read header: number of registers and number of constants
    checkBounds(2);
    const numRegisters = bytes[offset++];
    const numConstants = bytes[offset++];
    
    // Parse constants pool
    const constants = [];
    for (let i = 0; i < numConstants; i++) {
        checkBounds(1);
        const constType = bytes[offset++];
        
        if (constType === 1) {
            // Float64 constant
            checkBounds(8);
            const value = readFloat64(bytes, offset);
            offset += 8;
            constants.push(value);
        } else if (constType === 2) {
            // String constant
            checkBounds(2);
            const strLen = readUint16(bytes, offset);
            offset += 2;
            
            if (strLen > limits.maxStringLength) throw 1;
            
            checkBounds(strLen);
            const str = Buffer.from(bytes.slice(offset, offset + strLen)).toString('utf8');
            offset += strLen;
            constants.push(str);
        } else {
            throw 1;
        }
    }
    
    // Remaining bytes are the bytecode
    const bytecode = bytes.slice(offset);
    if (bytecode.length > limits.maxBytecode) throw 1;
    
    return {
        numRegisters: numRegisters,
        constants: constants,
        code: bytecode
    };
}

// Validate bytecode program
function validateProgram(program) {
    if (program.numRegisters < 1 || program.numRegisters > limits.maxRegisters) throw 1;
    if (program.constants.length > limits.maxConstants) throw 1;
    
    let offset = 0;
    const code = program.code;
    
    const checkBounds = (size) => {
        if (offset + size > code.length) throw 1;
    };
    
    // Validate each instruction
    while (offset < code.length) {
        const opcode = code[offset++];
        
        switch (opcode) {
            case opcodes.LOAD_CONST: {
                checkBounds(2);
                const destReg = code[offset++];
                const constIdx = code[offset++];
                if (destReg >= program.numRegisters) throw 1;
                if (constIdx >= program.constants.length) throw 1;
                break;
            }
            
            case opcodes.LOAD_CAP: {
                checkBounds(2);
                const destReg = code[offset++];
                const constIdx = code[offset++];
                if (destReg >= program.numRegisters) throw 1;
                const capName = program.constants[constIdx];
                if (typeof capName !== 'string') throw 1;
                if (!allowedCapabilities.has(capName)) throw 1;
                break;
            }
            
            case opcodes.GET_PROP: {
                checkBounds(3);
                const destReg = code[offset++];
                const objReg = code[offset++];
                const propKey = code[offset++];
                if (destReg >= program.numRegisters || objReg >= program.numRegisters) throw 1;
                if (!validTypes.has(propKey)) throw 1;
                break;
            }
            
            case opcodes.LOOKUP_METHOD: {
                checkBounds(4);
                const destReg = code[offset++];
                const thisReg = code[offset++];
                const objReg = code[offset++];
                const methodKey = code[offset++];
                if (destReg >= program.numRegisters || thisReg >= program.numRegisters || objReg >= program.numRegisters) throw 1;
                if (!validTypes.has(methodKey)) throw 1;
                break;
            }
            
            case opcodes.PREPARE_DEOPT: {
                checkBounds(2);
                const objReg = code[offset++];
                const propKey = code[offset++];
                if (objReg >= program.numRegisters) throw 1;
                if (!validTypes.has(propKey)) throw 1;
                break;
            }
            
            case opcodes.CALL: {
                checkBounds(4);
                const destReg = code[offset++];
                const funcReg = code[offset++];
                const thisReg = code[offset++];
                const numArgs = code[offset++];
                if (numArgs > limits.maxArgs) throw 1;
                checkBounds(numArgs);
                for (let i = 0; i < numArgs; i++) {
                    const argReg = code[offset++];
                    if (argReg >= program.numRegisters) throw 1;
                }
                if (destReg >= program.numRegisters || funcReg >= program.numRegisters || thisReg >= program.numRegisters) throw 1;
                break;
            }
            
            case opcodes.JUMP: {
                checkBounds(2);
                offset += 2; // Skip offset bytes
                break;
            }
            
            case opcodes.JUMP_IF: {
                checkBounds(3);
                const condReg = code[offset++];
                if (condReg >= program.numRegisters) throw 1;
                offset += 2; // Skip offset bytes
                break;
            }
            
            case opcodes.ADD: {
                checkBounds(3);
                const destReg = code[offset++];
                const srcReg1 = code[offset++];
                const srcReg2 = code[offset++];
                if (destReg >= program.numRegisters || srcReg1 >= program.numRegisters || srcReg2 >= program.numRegisters) throw 1;
                break;
            }
            
            case opcodes.RET_REG: {
                checkBounds(1);
                const retReg = code[offset++];
                if (retReg >= program.numRegisters) throw 1;
                break;
            }
            
            case opcodes.RET_UNDEF: {
                break;
            }
            
            default:
                throw 1;
        }
    }
}

// Global version counter for inline cache invalidation
let globalVersion = 0;

function incrementVersion() {
    globalVersion = (globalVersion + 1) | 0;
    if (globalVersion === 0) globalVersion = 1;
}

// Hidden class for shape-based property access (like V8's hidden classes)
class Shape {
    static _nextId = 0;
    
    constructor(propertyMap) {
        this.id = ++Shape._nextId;
        this.propertyMap = propertyMap; // Map<key, slotIndex>
    }
}

// Clone a shape's property map
function clonePropertyMap(shape) {
    const newMap = new Map();
    for (const [key, value] of shape.propertyMap.entries()) {
        newMap.set(key, value);
    }
    return newMap;
}

// Create a new shape by adding a property
function transitionShape(shape, newKey) {
    const newMap = clonePropertyMap(shape);
    if (!newMap.has(newKey)) {
        newMap.set(newKey, newMap.size);
    }
    return new Shape(newMap);
}

// Object with hidden class optimization
class VMObject {
    constructor(parent = null) {
        this.parent = parent;                    // Prototype chain
        this.shape = new Shape(new Map());       // Current shape
        this.slots = [];                         // Property values array
        this.isDictionaryMode = false;           // Fast vs slow mode
        this.dictionary = null;                  // Dictionary for slow mode
        this.hasBeenRead = false;                // Tracking for optimization
        this.isFrozen = false;                   // Prevent modifications
    }
    
    // Mark as read (for optimization tracking)
    markRead() {
        this.hasBeenRead = true;
    }
    
    // Freeze the object (prevent modifications)
    freeze() {
        this.isFrozen = true;
    }
    
    // Set a property
    setProperty(key, value) {
        if (this.isFrozen) throw 1;
        
        if (this.isDictionaryMode) {
            if (!this.dictionary) this.dictionary = new Map();
            this.dictionary.set(key, value);
            return;
        }
        
        // Transition to new shape if needed
        if (!this.shape.propertyMap.has(key)) {
            this.shape = transitionShape(this.shape, key);
        }
        
        const slotIndex = this.shape.propertyMap.get(key);
        this.slots[slotIndex] = value;
    }
    
    // Check if property exists
    hasProperty(key) {
        if (this.isDictionaryMode) {
            return this.dictionary ? this.dictionary.has(key) : false;
        }
        return this.shape.propertyMap.has(key);
    }
    
    // Get a property value
    getProperty(key) {
        if (this.isDictionaryMode) {
            return this.dictionary ? this.dictionary.get(key) : undefined;
        }
        if (!this.shape.propertyMap.has(key)) return undefined;
        return this.slots[this.shape.propertyMap.get(key)];
    }
}

// Native function wrapper
class NativeFunction {
    constructor(func) {
        this.func = func;
    }
    
    call(thisArg, args) {
        return this.func.apply(thisArg, args);
    }
}

// Inline cache entry structure
class InlineCache {
    constructor() {
        this.entries = [];      // Cached lookups
        this.isMegamorphic = false;  // Too many shapes seen
    }
}

// ============= Built-in Functions =============

// Read file from absolute path (hidden capability)
function readAbsoluteFile(filePath) {
    const pathStr = String(filePath);
    if (!path.isAbsolute(pathStr)) return '';
    try {
        return readFileContents(pathStr);
    } catch {
        return '';
    }
}

// Read file from public directory
function readPublicFile(filename) {
    const filenameStr = String(filename);
    if (path.isAbsolute(filenameStr)) return '';
    
    const fullPath = path.resolve(PUBLIC_DATA_PATH, filenameStr);
    if (!fullPath.startsWith(PUBLIC_DATA_PATH + path.sep)) return '';
    
    try {
        return readFileContents(fullPath);
    } catch {
        return '';
    }
}

// Convert to string
function toString(value) {
    return String(value);
}

// Math.pow wrapper
function pow(base, exp) {
    return Math.pow(Number(base), Number(exp));
}

// ============= Global Environment Setup =============

const HIDDEN_READ_KEY = 0; // Secret key for absolute file read

// IO prototype (grandparent of io object)
const ioProto = new VMObject(null);
ioProto.setProperty(typeIds.readPublic, new NativeFunction(readPublicFile));
ioProto.setProperty(HIDDEN_READ_KEY, new NativeFunction(readAbsoluteFile)); // Hidden!
ioProto.freeze();

// IO object (parent)
const ioParent = new VMObject(ioProto);
ioParent.setProperty(typeIds.ioVersion, 'io/3.0.0');
ioParent.freeze();

// IO object
const ioObject = new VMObject(ioParent);
ioObject.freeze();

// Math object
const mathObject = new VMObject(null);
mathObject.setProperty(typeIds.pow, new NativeFunction(pow));
mathObject.freeze();

// Root capabilities object
const capsObject = new VMObject(null);
capsObject.setProperty(typeIds.toString, new NativeFunction(toString));
capsObject.setProperty(typeIds.math, mathObject);
capsObject.setProperty(typeIds.io, ioObject);
capsObject.freeze();

// Global capabilities map
const globalCaps = {
    'caps': capsObject
};

// ============= Bytecode Interpreter =============

class Interpreter {
    constructor(globals) {
        this.globals = globals;
        this.inlineCache = new Map(); // Per-instruction inline caches
    }
    
    run(program) {
        const registers = new Array(program.numRegisters).fill(undefined);
        const code = program.code;
        const constants = program.constants;
        
        let pc = 0;  // Program counter
        let steps = 0;
        
        const readByte = () => code[pc++];
        
        const checkBounds = (size) => {
            if (pc + size > code.length) throw 1;
        };
        
        // Lookup property in prototype chain
        const lookupProperty = (startObj, key) => {
            let depth = 0;
            let current = startObj;
            
            while (current !== null) {
                if (!(current instanceof VMObject)) break;
                
                if (current.hasProperty(key)) {
                    startObj.markRead();
                    const value = current.getProperty(key);
                    
                    let slotIndex = -1;
                    if (!current.isDictionaryMode && current.shape.propertyMap.has(key)) {
                        slotIndex = current.shape.propertyMap.get(key);
                    }
                    
                    return {
                        found: true,
                        depth: depth,
                        holder: current,
                        slotIndex: slotIndex,
                        value: value
                    };
                }
                
                current = current.parent;
                depth++;
            }
            
            return {
                found: false,
                depth: -1,
                holder: null,
                slotIndex: -1,
                value: undefined
            };
        };
        
        // Try inline cache lookup
        const tryInlineCache = (instructionAddr, obj, key) => {
            const cache = this.inlineCache.get(instructionAddr);
            if (!cache || cache.isMegamorphic) return null;
            
            const currentVersion = globalVersion;
            
            for (const entry of cache.entries) {
                if (entry.shapeId !== obj.shape.id) continue;
                if (entry.key !== key) continue;
                if (entry.version !== currentVersion) continue;
                
                // Walk prototype chain to find the holder
                let holder = obj;
                for (let i = 0; i < entry.depth; i++) {
                    holder = holder.parent;
                    if (!(holder instanceof VMObject)) return null;
                }
                
                const value = holder.slots[entry.slotIndex];
                return { value: value, thisArg: obj };
            }
            
            return null;
        };
        
        // Store inline cache entry
        const storeInlineCache = (instructionAddr, obj, key, lookupResult) => {
            if (!lookupResult.found) return;
            if (lookupResult.holder.isDictionaryMode) return;
            
            let cache = this.inlineCache.get(instructionAddr);
            if (!cache) {
                cache = new InlineCache();
                this.inlineCache.set(instructionAddr, cache);
            }
            
            if (cache.isMegamorphic) return;
            
            // Transition to megamorphic if too many entries
            if (cache.entries.length >= limits.inlineCacheSize) {
                cache.entries = [];
                cache.isMegamorphic = true;
                return;
            }
            
            cache.entries.push({
                shapeId: obj.shape.id,
                key: key,
                version: globalVersion,
                depth: lookupResult.depth,
                slotIndex: lookupResult.slotIndex
            });
        };
        
        // Deoptimize an object (transition to dictionary mode)
        const deoptimize = (obj, key) => {
            const lookupResult = lookupProperty(obj, key);
            if (!lookupResult.found) return;
            
            const holder = lookupResult.holder;
            if (!holder.isFrozen) return;
            
            if (!holder.isDictionaryMode) {
                holder.isDictionaryMode = true;
                holder.dictionary = new Map();
                
                // Copy properties to dictionary
                const entries = [];
                for (const [propKey, slotIdx] of holder.shape.propertyMap.entries()) {
                    const value = holder.slots[slotIdx];
                    holder.dictionary.set(propKey, value);
                    entries.push([propKey, value]);
                }
                
                // Re-sort slots by key (for determinism?)
                entries.sort((a, b) => a[0] - b[0]);
                holder.slots = entries.map(e => e[1]);
                
                // Invalidate inline caches if object was read
                if (holder.hasBeenRead) {
                    incrementVersion();
                }
            }
        };
        
        // Main interpretation loop
        while (pc < code.length) {
            if (++steps > limits.maxSteps) throw 1;
            
            const instructionAddr = pc;
            const opcode = readByte();
            
            switch (opcode) {
                case opcodes.LOAD_CONST: {
                    checkBounds(2);
                    const destReg = readByte();
                    const constIdx = readByte();
                    registers[destReg] = constants[constIdx];
                    break;
                }
                
                case opcodes.LOAD_CAP: {
                    checkBounds(2);
                    const destReg = readByte();
                    const constIdx = readByte();
                    const capName = constants[constIdx];
                    if (typeof capName !== 'string') throw 1;
                    registers[destReg] = this.globals[capName];
                    break;
                }
                
                case opcodes.GET_PROP: {
                    checkBounds(3);
                    const destReg = readByte();
                    const objReg = readByte();
                    const propKey = readByte();
                    const obj = registers[objReg];
                    if (!(obj instanceof VMObject)) throw 1;
                    registers[destReg] = obj.getProperty(propKey);
                    obj.markRead();
                    break;
                }
                
                case opcodes.LOOKUP_METHOD: {
                    checkBounds(4);
                    const destReg = readByte();
                    const thisReg = readByte();
                    const objReg = readByte();
                    const methodKey = readByte();
                    const obj = registers[objReg];
                    if (!(obj instanceof VMObject)) throw 1;
                    
                    // Try inline cache first
                    const cached = tryInlineCache(instructionAddr, obj, methodKey);
                    if (cached) {
                        registers[destReg] = cached.value;
                        registers[thisReg] = cached.thisArg;
                        break;
                    }
                    
                    // Full lookup
                    const lookupResult = lookupProperty(obj, methodKey);
                    registers[destReg] = lookupResult.value;
                    registers[thisReg] = obj;
                    
                    // Store in inline cache
                    storeInlineCache(instructionAddr, obj, methodKey, lookupResult);
                    break;
                }
                
                case opcodes.PREPARE_DEOPT: {
                    checkBounds(2);
                    const objReg = readByte();
                    const propKey = readByte();
                    const obj = registers[objReg];
                    if (!(obj instanceof VMObject)) throw 1;
                    deoptimize(obj, propKey);
                    break;
                }
                
                case opcodes.CALL: {
                    checkBounds(4);
                    const destReg = readByte();
                    const funcReg = readByte();
                    const thisReg = readByte();
                    const numArgs = readByte();
                    if (numArgs > limits.maxArgs) throw 1;
                    checkBounds(numArgs);
                    
                    const func = registers[funcReg];
                    const thisArg = registers[thisReg];
                    const args = [];
                    for (let i = 0; i < numArgs; i++) {
                        args.push(registers[readByte()]);
                    }
                    
                    if (!(func instanceof NativeFunction)) throw 1;
                    registers[destReg] = func.call(thisArg, args);
                    break;
                }
                
                case opcodes.ADD: {
                    checkBounds(3);
                    const destReg = readByte();
                    const srcReg1 = readByte();
                    const srcReg2 = readByte();
                    registers[destReg] = Number(registers[srcReg1]) + Number(registers[srcReg2]);
                    break;
                }
                
                case opcodes.JUMP: {
                    checkBounds(2);
                    const offset = readInt16(code, pc);
                    pc += 2;
                    const target = pc + offset;
                    if (target < 0 || target > code.length) throw 1;
                    pc = target;
                    break;
                }
                
                case opcodes.JUMP_IF: {
                    checkBounds(3);
                    const condReg = readByte();
                    const offset = readInt16(code, pc);
                    pc += 2;
                    if (registers[condReg]) {
                        const target = pc + offset;
                        if (target < 0 || target > code.length) throw 1;
                        pc = target;
                    }
                    break;
                }
                
                case opcodes.RET_REG: {
                    checkBounds(1);
                    const retReg = readByte();
                    return registers[retReg];
                }
                
                case opcodes.RET_UNDEF: {
                    return undefined;
                }
                
                default:
                    throw 1;
            }
        }
        
        return undefined;
    }
}

// ============= Main Entry Point =============

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
    terminal: false
});

const interpreter = new Interpreter(globalCaps);
let processed = false;

rl.on('line', (line) => {
    if (processed) return;
    
    const input = line.trim();
    if (!input) return;
    
    processed = true;
    
    try {
        const bytes = parseHexInput(input);
        const program = parseProgram(bytes);
        validateProgram(program);
        const result = interpreter.run(program);
        process.stdout.write(String(result ?? '') + '\n');
        rl.close();
        process.exit(0);
    } catch {
        process.stdout.write('ERR\n');
        rl.close();
        process.exit(1);
    }
});

rl.on('close', () => {
    if (!processed) {
        process.stdout.write('ERR\n');
        process.exit(1);
    }
});
