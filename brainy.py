'''
____author__night king
____open source_____
____more info__tg__@chill_vibez
'''

import hashlib 

print(" ____            _             ")
print("| __ ) _ __ __ _(_)_ __  _   _ ")
print("|  _ \| '__/ _` | | '_ \| | | |")
print("| |_) | | | (_| | | | | | |_| |")
print("|____/|_|  \__,_|_|_| |_|\__, |")
print("                         |___/ ")
print("[~ Made by <3 by NIght KIng ~] ")




flag = 0
#counter = 0

pass_hash = input("Enter md5 hash: ")

wordlist = input("File name: ")

try:
	pass_file = open (wordlist, "r")
except:
	print(" :( No file found ")
	quit()

for word in pass_file:

	enc_wrd = word.encode('utf-8')
	digest = hashlib.md5(enc_wrd.strip()).hexdigest()


  #print(word)
  #print(digest)
  #print(pass_hash)

#counter += 1
	if digest == pass_hash:
		print("password found")
		print("password is " + word)
		flag = 1 
		break 

if flag == 0:
	print("password/passphrase is not in the list")
