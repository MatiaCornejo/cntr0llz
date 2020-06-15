from pwn import *
URL="l4tinhtb.com"
PORT=1337
#context.log_level = 'DEBUG'
cnct = remote(URL, PORT)
result=str(cnct.recvuntil("BRUTA!\n")).strip().split("\n")
ecuacion=result[0].split(" ")
value=int(ecuacion[-1][2:],16)^int(ecuacion[0][2:],16)
cnct.sendline(hex(value)+"\n")
cnct.interactive()
