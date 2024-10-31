from pwn import *
r = remote("host3.dreamhack.games",10913)
r.recvuntil(b"number: ") 
rand = r.recvn(10)
print("rand: ",rand)
x = int(rand,16) ^ 0x7d1c4b0a
x = str(x).encode()
r.sendlineafter(b"Input? ", x)
r.interactive()