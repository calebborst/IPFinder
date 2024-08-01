import geoip2.database
import threading
import random
import socket
import struct
import time
import math
import sys
import os

#settings
global counter
counter = 0
global threads
threads = 0
global workers
workers = 10
global saved
saved = 0
global dupe
dupe = 0

start_time = time.time()

def f():
	global threads
	global workers
	global counter
	global saved

	threads += 1
	counter += 1

	randomip = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))

	#Rounds up time
	global ctime
	ctime = time.time() - start_time
	ctime = math.ceil(int(ctime))

	settitle = 'Threads: ' + str(threads) + ' :: found: ' + str(counter) + ' :: Saved: '  + str(saved) + ' :: Dupes: ' + str(dupe) + ' :: Time: ' + str(ctime) + ' :: Scanning: ' + randomip
	print(f'\33]0;{settitle}\a', end='', flush=True)

	first,second,third,forth = randomip.split('.', 3)

	#Checking to see if it is a lan ip or not.
	if first == "10":
		threads -= 1
		return
	if first == "172":
		if int(second) <= 15:
			pass
		elif int(second) >= 16:
			threads -= 1
			return
		else:
			pass
	if first+'.'+second == "192.168":
		threads -= 1
		return

	try:
		with geoip2.database.Reader('City.mmdb') as reader:
			responce = reader.city(randomip)
			foundcountry = responce.country.name
			countrycode = responce.country.iso_code
			
			if foundcountry == None:
				foundcountry = 'Unknown'
				threads -= 1
				savedornot = "Fail"
				print('{: <20}'.format('IP: ' + randomip) + ' | ' + '{: ^25}'.format(foundcountry+':'+countrycode) + '| ' + '{: >6}'.format(savedornot))
				return
	except:
		foundcountry = "None"
		countrycode = "None"
		threads -= 1
		savedornot = "Fail"
		print('{: <20}'.format('IP: ' + randomip) + ' | ' + '{: ^25}'.format(foundcountry+':'+countrycode) + '| ' + '{: >6}'.format(savedornot))
		return


	#Check country code
	if countrycode != " ":
		pass
	else:
		savedornot = "Not right country"
		print('{: <20}'.format('IP: ' + randomip) + ' | ' + '{: ^25}'.format(foundcountry+':'+countrycode) + '| ' + '{: >6}'.format(savedornot))
		threads -= 1
		return
	
	try:
		readfile = open('foundips.txt', 'r')
	except:
		readfile = open('foundips.txt', 'w')
		readfile.close()
		readfile = open('foundips.txt', 'r')

	if randomip in readfile:
		savedornot = "Dupe"
		print('{: <20}'.format('IP: ' + randomip) + ' | ' + '{: ^25}'.format(foundcountry+':'+countrycode) + '| ' + '{: >6}'.format(savedornot))
		threads -= 1
		return

	with open('foundips.txt', 'a') as f:
		saved += 1
		f.write(randomip + '\n')

	savedornot = "Saved"

	spcs = 2

	print('{: <20}'.format('IP: ' + randomip) + ' | ' + '{: ^25}'.format(foundcountry+':'+countrycode) + '| ' + '{: >6}'.format(savedornot))

	try:
		threads -= 1
	except:
		threads -= 1

if __name__ == '__main__':
	try:
		while True:
			if threads >= workers:
				pass
			else:
				t = threading.Thread(target=f)
				t.start()
	except KeyboardInterrupt:
		time.sleep(1)
		print("\n")
		print("Threads used: " + str(threads))
		print("Generated: " + str(counter))
		print("Time took: " + str(ctime))
		print("Saved: " + str(saved))
		try:
			exit()
		except:
			exit()

	print("Script stopped")

