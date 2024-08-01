import geoip2.database
import threading
import argparse
import random
import socket
import struct
import time
import sys
import os
from requests import get
from sys import platform

#portlist = ['80', '8080', '7000', '443']
#openports = []

#settings (DONT CHANGE!)
ipscan = 0
downips = 0
upips = 0

#os detect
if platform == "linux" or platform == "linux2":
    print("Detected linux OS.")
    uselinux = 1
elif platform == "darwin":
    print("Detected Mac OS")
    usemac = 1
    print("Unsaported atm...")
    exit()
elif platform == "win32":
    print("Detected Windows OS")
    usewindows = 1

print("")
print("")

#styleing.
G, B, R, W, M, C, end, Y = '\033[92m', '\033[94m', '\033[91m', '\x1b[37m', '\x1b[35m', '\x1b[36m', '\033[0m', "\033[93m"
good = end + G
bad = end + R
info = end + Y + "[-]" + Y
scanning = end + M + "[" + W + "*" + M + "]"
added = end + G + "[" + W + "+" + G + "]"

try:
	foundips = open('foundips.txt', 'r')
except:
	print("Found ips file not found!")
	exit()

number_of_lines = len(open('foundips.txt').readlines(  ))
print("Scanning", number_of_lines, "ips.")
time.sleep(1)

for ip in foundips:
	ipscan = ipscan + 1

	if usewindows == 1:
		#If this if statement isnt here there is an error for some reason...
		if ipscan == 1:
			pass
		else:
			settitle = '\x1b]2;'+str(ipscan)+"/"+str(number_of_lines)+"  "+ip+'\x07'
			sys.stdout.write(settitle)

	validonline = open('validonline.txt', 'a+')
	#remove new line from end of ip so ping command will work (added back latter).
	ip = ip.rstrip('\n')
	#if on windows, mac, linux do this type of ping
	if usewindows == 1:
		response = os.system(f"ping -n 1 " + ip + " >nul")
	elif usemac == 1:
		exit()
	elif uselinux == 1:
		response = os.system("ping -c 1 " + ip + " > /dev/null 2>&1")
	
	#if responce == 0 then host is up else its dead/down
	if response == 0:
		##Scans to see if any needed ports are open (experamental)
		#for port in portlist:
		#	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		#	result = sock.connect_ex((ip,int(port)))
		#	if result == 0:
		#		openports.append(port)
		#		print("ALIVE", port)
		#	else:
		#		print("DEAD", port)
		#		continue

		try:
			with geoip2.database.Reader('City.mmdb') as reader:
				responce = reader.city(ip)
				country = responce.country.name
				if country == None:
					country = 'unknown'
		except:
			country = "Does not exist in database..."

		print(scanning + "Scanning:" + end, ip, "=", good + 'UP!' + end + " Country: " + country)
		validonline.write(ip+'\n')
		upips = upips + 1
	else:
		print(scanning + "Scanning:" + end, ip, "=", bad + 'DOWN!' + end)
		downips = downips + 1
	
	validonline.close()
	#openports.clear()



print("Done! :)")
print("Online: " + upips + "Offline: " + downips)




