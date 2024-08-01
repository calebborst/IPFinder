import geoip2.database
import threading
import argparse
import random
import socket
import struct
import math
import time
import sys
import os
import re
from requests import get
from sys import platform

#config
#Globaling the config...
global saveipstofile
global gethostname
global fastloader
global cleant
global info
global good
global bad
global scanning

#Gets arguments or adds them? idk...
parser = argparse.ArgumentParser(description="IPFinder")

#adding argumeents...
parser.add_argument("-s", "--save", type=str, help="Saves output to a foundips.txt or to a name of your choice.")
parser.add_argument("-bl", "--blacklist", help="Checks to see if the ip generated is in the blacklist.txt file. (Try keep blacklist short for optimal performance.)",
	action="store_true")
parser.add_argument("-hd", "--hiddenips", help="Check the ip to see if it is from a certian type (VPN, Proxy or goverment IP).",
	action="store_true")
parser.add_argument("-hn", "--hostname", help="Saves hostnames to the output file.",
	action="store_true")
parser.add_argument("-f", "--fast", type=str, help="Makes the program use a queue method, can change by using the arguement then using a number of your choice. Higher the number faster it goes.")
parser.add_argument("-c", "--clean", help="Only shows IP's online.",
	action="store_true")
parser.add_argument("-kp", "--keep", type=str, help="Only keeps ips from a certian country (enter country code only EG: US, CA, CN).")
parser.add_argument("-p", "--port", type=str, help="Makes the program scan for specified ports open on an ip.")
args = parser.parse_args()

arglist = ['-s', '-hn', '-f', '-c', '-ct', 'kp', '--save', '--hostname', '--fast', '--clean', '--country', '--keep', ' ']

if args.save:
	print("Option: Save ON.")
	saveipstofile = 1 #if 0 it wont save else if its 1 it will save found ips.
	savefilename = str(args.save)

	if savefilename[-4:] != ".txt":
		savefilename = savefilename + ".txt"
	print("Output file: " + savefilename)
	
else:
	print("Option: Save OFF")
	saveipstofile = 0 #if 0 it wont save else if its 1 it will save found ips.

if args.blacklist:
	print("Option: Blacklist ON.")
	blacklist = 1
else:
	print("Option: Blacklist OFF.")
	blacklist = 0

if args.hiddenips:
	print("Option: Hiddenips ON.")
	hiddenips = 1
else:
	print("Option: Hiddenips OFF.")
	hiddenips = 0

if args.hostname:
	print("Option: Get hostname ON.")
	gethostname = 1 #if is greater then 1 will save hostname to output file else if less then 1 then it wont.
else:
	print("Option: Get hostname OFF.")
	gethostname = 0 #if is greater then 1 will save hostname to output file else if less then 1 then it wont.

if args.fast:
	print("Option: Fast ON.")
	fastloader = 1 #if is lower then 1 will have a 0.1 delay else it will go as fast as it can.
	workerspeed = int(args.fast)
else:
	print("Option: Fast OFF.")
	fastloader = 0 #if is lower then 1 will have a 0.1 delay else it will go as fast as it can.
	workerspeed = 1

if args.clean:
	print("Option: Clean interface ON.")
	cleant = 1 #keeps the terminal clean and only outputs ips that are alive.
else:
	print("Option: Clean interface OFF.")
	cleant = 0 #keeps the terminal clean and only outputs ips that are alive.

if args.keep:
	print("Option: Keep ON.")
	keep = 1
else:
	print("Option: keep OFF.")
	keep = 0

if keep == 1:
	print("Checking what country to keep...")
	if args.keep in arglist:
		print("Error did not specify what country or had another option in front of this one.")
		exit()
	else:
		print("Keeping: " + str(args.keep))

if args.port:
	print("Option: Ports ON.")
	global scan_for_ports
	scan_for_ports = True
	global port_list
	port_list = []
	portlist = args.port
	if "," in portlist:
		portlist = portlist.split(",")
		for port in portlist:
			port_list.append(port)
	else:
		port = args.port
		port_list.append(port)
	print(f"Scanning though ports: {port_list}")
else:
	print("Option: Ports OFF.")
	scan_for_ports = False


print("")

#settings (DONT CHANGE!)
myip = get('http://myip.dnsomatic.com/').text
print("My ip:", myip)

uselinux = 0
usemac = 0
usewindows = 0

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

G, B, R, W, M, C, end, Y = '\033[92m', '\033[94m', '\033[91m', '\x1b[37m', '\x1b[35m', '\x1b[36m', '\033[0m', "\033[93m"
good = end + G
bad = end + R
info = end + Y + "[-]" + Y
scanning = end + M + "[" + W + "*" + M + "]"
added = end + G + "[" + W + "+" + G + "]"

global writelinenum
writelinenum = 0
global looper
looper = 0
global counter
counter = 0
global howmanydonefsofar
howmanydonefsofar = 0

#NEW QUEUE METHOD
global workers
workers = workerspeed

if hiddenips >= 1:
	print("Getting goverment IP types...")
	url = 'https://raw.githubusercontent.com/frankielivada22/IPTYPES/main/GOVIPTYPES.txt'
	govermentiptypes = get(url).text
	
	print("Getting proxy IP types...")
	url = 'https://raw.githubusercontent.com/frankielivada22/IPTYPES/main/proxylist.txt'
	proxyiptypes = get(url).text

	print("Getting tor IP types...")
	url = 'https://raw.githubusercontent.com/frankielivada22/IPTYPES/main/torips.txt'
	toriptypes = get(url).text

if blacklist >= 1:
	readblacklist = open('blacklist.txt', 'r', errors="ignore")
	blacklistedips = readblacklist.read()
else:
	pass

start_time = time.time()

#main function of the program
def f():
	global howmanydonefsofar
	global blacklistedips
	global scan_for_ports
	global readblacklist
	global writelinenum
	global port_list
	global counter

	#main code

	#generates a random ip
	randomip = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))

	if hiddenips >= 1:
		if randomip in govermentiptypes:
			return
		elif randomip in proxyiptypes: 
			return
		elif randomip in toriptypes:
			return

	if blacklist >= 1:
		if randomip in blacklistedips:
			return
		

	#sets console title to the queue count (only if your on windows)
	if usewindows == 1:
		#Rounds up time
		ctime = time.time() - start_time
		ctime = math.ceil(int(ctime))
		settitle = 'title Press ctrl + c to stop :: IPs scanned: ' + str(howmanydonefsofar) + ' :: Saved: ' + str(counter) + ':: Time (s): ' + str(ctime) + ' :: Queue = ' + str(queue) + ' :: ' + randomip
		os.system(settitle)
	elif uselinux == 1:
		ctime = time.time() - start_time
		ctime = math.ceil(int(ctime))
		settitle = 'title Press ctrl + c to stop :: IPs scanned: ' + str(howmanydonefsofar) + ' :: Saved: ' + str(counter) + ':: Time (s): ' + str(ctime) + ' :: Queue = ' + str(queue) + ' :: ' + randomip
		print(f'\33]0;{settitle}\a', end='', flush=True)

	#File detect
	if saveipstofile >= 1:
		try:
			readips = open(savefilename, 'r')
		except:
			print("File not found! Making new file.")
			createfoundips = open(savefilename, 'a')
			readips = open(savefilename, 'r')

	#Makes sure its not a gateway ip or your own ip.
	if "255.255.255" in randomip:
		return
	if randomip == myip:
		return
	
	first,second,third,forth = randomip.split('.', 3)

	#Checking to see if it is a lan ip or not.
	if first == "10":
		return
	if first == "172":
		if int(second) <= 15:
			pass
		elif int(second) >= 16:
			return
		else:
			pass
	if first+'.'+second == "192.168":
		return



	if usewindows == 1:
		response = os.system(f"ping -n 1 " + randomip + " >nul")
	elif usemac == 1:
		response = os.system("ping -c 1 " + randomip + " > /dev/null 2>&1")
	elif uselinux == 1:
		response = os.system("ping -c 1 " + randomip + " > /dev/null 2>&1")

	if response == 0:

		try:
			with geoip2.database.Reader('City.mmdb') as reader:
				responce = reader.city(randomip)
				foundcountry = responce.country.name
				countrycode = responce.country.iso_code
				if foundcountry == None:
					foundcountry = 'unknown'
		except:
			foundcountry = "Does not exist in database..."
			countrycode = "Does not exist in database..."

		print(scanning + "Scanning:" + end, randomip, "=", good + 'UP!' + end + " Queue = " + str(queue) + " Country: " + foundcountry)
		try:
			ipshostname = socket.getfqdn(randomip)
		except:
			print("Unable to get info.")
			return

		if gethostname >= 1:
			if ipshostname == randomip:
				print(info + "ISP:" + end, " Not found or same as IP")
			else:
				print(info + "ISP:" + end, ipshostname)
		else:
			pass

		if ipshostname == "localhost":
			return

		openports = ""
		if scan_for_ports == True:
			target = socket.gethostbyname(randomip)
			for port in port_list:
				s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				socket.setdefaulttimeout(1)
				result = s.connect_ex((target,int(port)))
				if result == 0:
					openports = openports + f" {port}"
				s.close()
		
		if scan_for_ports == True:
			if openports == "":
				return


		if saveipstofile >= 1:
			if keep >= 1:
				if countrycode == str(args.keep):
					pass
				else:
					return
			else:
				pass

			if ipshostname in readips.read():
				print("IP already in file")
				return

			if int(gethostname) >= 1:
				writetofile = str(randomip) + " = " + str(ipshostname) + "\n"
				
				with open(savefilename, 'a') as foundips:
					foundips.write(str(writetofile))
					foundips.close()

				writelinenum = writelinenum + 1
				counter = counter + 1
				print(added + "Added:" + end, randomip, "Number:", good + str(counter) + end + " Country: " + foundcountry + " Ports: " + str(openports))
				
			else:
				writetofile = str(randomip) + "\n"

				with open(savefilename, 'a') as foundips:
					foundips.write(str(writetofile))
					foundips.close()

				writelinenum = writelinenum + 1
				counter = counter + 1
				print(added + "Added:" + end, randomip, "Number:", good + str(counter) + end + " Country: " + foundcountry + " Ports: " + str(openports))
		else:
			print(added + "Added:" + end, randomip, "Number:", good + str(counter) + end + " Country: " + foundcountry + " Ports: " + str(openports))


	else:
		if cleant >= 1:
			pass
		else:
			print(scanning + "Scanning:" + end, randomip, "=", bad + 'DOWN!' + end + " Queue = " + str(queue))

	#main code ends here
	howmanydonefsofar += 1



#multithreaded prosess
if __name__ == "__main__":
	while True:
		#setting thread
		t = threading.Thread(target=f)
		queue = threading.active_count()

		if fastloader >= 1:
			#NEW QUEUE METHOD
			try:			
				if threading.active_count() >= workers:
					pass
				else:
					t.start()
			except:
				print("Something went wrong. - Restarting script.")
				time.sleep(3)
		else:
			try:
				time.sleep(0)
				t.start()
			except:
				print("Something went wrong. - Restarting script.")
				time.sleep(3)
