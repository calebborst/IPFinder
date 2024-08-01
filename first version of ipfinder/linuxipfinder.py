import threading
import random
import socket
import struct
import time
import sys
import os
from requests import get

#settings
foundips = open('foundips.txt', 'a')
readips = open('foundips.txt', 'r')
myip = get('http://myip.dnsomatic.com/').text
print("My ip:", myip)

global writelinenum
writelinenum = 0
global wlnthread 
wlnthread = 1000

#config
global gethostname
gethostname = 0 #if is greater then 1 will save hostname if less then 1 then wont.
global fastloader
fastloader = 0 #if is lower then 1 will have a 0.1 delay
global looper
looper = 0




#main code to gen random ips and scan them save then etc
def f():
	global writelinenum
	randomip = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))

	if "255.255.255" in randomip:
		print("255.255.255 ip found! Generating new ip.")
		randomip = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
	if "192.168" in randomip:
		print("192.168 ip found! Generating new ip.")
		randomip = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
	if randomip == myip:
		print("Some how got your own ip...")
		randomip = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))


	response = os.system("ping -c 1 " + randomip + " > /dev/null 2>&1")

	if response == 0:
		print(randomip, 'is up!')
		try:
			ipshostname = socket.getfqdn(randomip)
			print(ipshostname)
		except:
			print("Unable to get info.")
			return

		if ipshostname == randomip:
			print("ips isp is same")
		else:
			print("ips isp is", ipshostname)

		if ipshostname == "localhost":
			return

		if ipshostname in readips.read():
			print("ip already in file")
			return

		if int(gethostname) >= 1:
			writetofile = str(randomip) + " = " + str(ipshostname) + "\n"
			foundips.write(str(writetofile))
			writelinenum = writelinenum + 1
		else:
			writetofile = str(randomip) + "\n"
			foundips.write(str(writetofile))
			writelinenum = writelinenum + 1
	else:
		print(randomip, 'is down!')


#multithreaded prosess
if __name__ == "__main__":
	while True:
		if fastloader >= 1:
			try:
				t = threading.Thread(target=f)
				#print(looper) DEBUG LINE
				looper = looper + 1
				if writelinenum == wlnthread:
					print("1000 More lines of ips have been added")
					print("Sleeping for a bit...")
					time.sleep(10)
					wlnthread = wlnthread + 1000
					
				time.sleep(0.0)
				t.start()
			except:
				print("Something went wrong. - Restarting script.")
				time.sleep(3)
		else:
			t = threading.Thread(target=f)
			time.sleep(0.1)
			t.start()
