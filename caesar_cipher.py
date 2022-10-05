# Caesar Cipher

import sys

# Globals
cap_list=[ i for i in range(65,91)]


def enc_cipher_text(plain_list,rot_key):
	index_order=[]
	for i in plain_list:
		if i==' ':
			index_order.append(i)
		else:
			cap_index=ord(i)
			index_order.append(cap_list.index(cap_index))

# encrypting############
	scrambled=[]
	for i in index_order:
		if i==' ':
			scrambled.append(i)
		else:
			scram=(i-rot_key)%26
			scrambled.append(chr(cap_list[scram]))

	for i in scrambled:
		print(i,end='')
	print()

def dec_cipher_text(secret_list,rot_key):
	index_order=[]
	for i in secret_list:
		if i==' ':
			index_order.append(i)
		else:
			cap_index=ord(i)
			index_order.append(cap_list.index(cap_index))
# decrypting############
	scrambled=[]
	for i in index_order:
		if i==' ':
			scrambled.append(i)
		else:
			scram=(i+rot_key)%26
			scrambled.append(chr(cap_list[scram]))

	for i in scrambled:
		print(i,end='')
	print()

def plain_text():
	plain_text=input('Enter plain text: ').upper()
	rot_key=int(input('Enter rotation key (<=25) : '))
	if rot_key > 25:
		print('shift not available :(')
		start_caesar()
	else:
		plain_text_list=[]
#	print(plain_text)
		for i in plain_text:
			plain_text_list.append(i)
	enc_cipher_text(plain_text_list,rot_key)

def secret_text():
	secret_text=input('Enter cipher text: ').upper()
	rot_key=int(input('Enter secret key: (<=25): '))
	if rot_key > 25:
		print('Key not avaiable')
		start_caesar()
	else:
		secret_text_list=[]
		for i in secret_text:
			secret_text_list.append(i)
	dec_cipher_text(secret_text_list,rot_key)

def encrypt_text():
	plain_text()

def decrypt_text():
	secret_text()


def start_caesar():
	print('Caesar Cipher')
	print('Do you want to Encrypt or Decrypt? ')
	print("Type enc for encryption")
	print("Type dec for decryption")
	print("Type quit to exit")
	while True:
		choice=input('> ')
		if choice == 'quit':
			sys.exit('Quit')
		elif choice == 'enc':
			encrypt_text()
		elif choice == 'dec':
			decrypt_text()
		else:
			print('Invalid choice :(')


start_caesar()
