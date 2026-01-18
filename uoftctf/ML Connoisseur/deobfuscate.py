import re
import ast

# Read the obfuscated file
with open('ml-connoisseur/model.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace import statements
content = content.replace('import torch as G0GoSqu1d', 'import torch')
content = content.replace('import torch.nn as SQUID', 'import torch.nn as nn')
content = content.replace('import torch.nn.functional as GgS', 'import torch.nn.functional as F')
content = content.replace('from __future__ import annotations as G0gOSqu1D', 'from __future__ import annotations')

# Replace all G0GoSqu1d with torch
content = re.sub(r'\bG0GoSqu1d\b', 'torch', content)
content = re.sub(r'\bSQUID\b', 'nn', content)
content = re.sub(r'\bGgS\b', 'F', content)

# The main XOR function
def xor_func(a, b):
    return a ^ b

# Function to evaluate G0goSQuId_531543 calls
def eval_xor(match):
    try:
        a = int(match.group(1))
        b = int(match.group(2))
        result = a ^ b
        return str(result)
    except:
        return match.group(0)

# Replace G0goSQuId_531543(a, b) with a^b result
content = re.sub(r'G0goSQuId_531543\((\d+),\s*(\d+)\)', eval_xor, content)

# Simplify function names
content = re.sub(r'\bG0g0sQu1D_116510\b', 'xor_string', content)
content = re.sub(r'\bG0goSQuId_531543\b', 'xor', content)
content = re.sub(r'\bG0g0sQu1D\b', 'xor', content)
content = re.sub(r'\bG0gosQuId\b', 'div_xor', content)
content = re.sub(r'\bg0GOsquiD_37121\b', 'join_chr', content)
content = re.sub(r'\bgOg0sQuId_362335\b', 'process_string', content)
content = re.sub(r'\bG0goSQUid\b', 'div_xor2', content)
content = re.sub(r'\bgOg0sQuId\b', 'calc', content)
content = re.sub(r'\bg0GOsquiD\b', 'divide', content)
content = re.sub(r'\bG0G0SQU1D_169432\b', 'int', content)
content = re.sub(r'\bgoG0SQu1d\b', 'list', content)
content = re.sub(r'\bg0gosqu1D\b', 'str', content)

# Write the partially deobfuscated file
with open('ml-connoisseur/model_deobfuscated.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Deobfuscation complete! Output saved to model_deobfuscated.py")
print("\nNote: The file is partially deobfuscated. The control flow obfuscation")
print("(nested while loops with state machines) still needs manual analysis.")
