import os
import re
import sys
import math
import time
import pygame
import random
import socket
import struct
import pyperclip
import threading
import geoip2.database
	
from text import Text
from requests import get
from variables import COLORS, FONTS_DF, FONTS_FT

class Output():
	def __init__(self, full_rect: tuple, base_color: tuple, memorylimit: int = 200):
		self.x, self.y, self.w, self.h = full_rect
		self.base_color_r, self.base_color_g, self.base_color_b = base_color

		if self.base_color_r + 10 > 255:
			changed_border_color_r = self.base_color_r - 10
		else:
			changed_border_color_r = self.base_color_r + 10
		if self.base_color_g + 10 > 255:
			changed_border_color_g = self.base_color_g - 10
		else:
			changed_border_color_g = self.base_color_g + 10
		if self.base_color_b + 10 > 255:
			changed_border_color_b = self.base_color_b - 10
		else:
			changed_border_color_b = self.base_color_b + 10

		self.fill_color = (self.base_color_r, self.base_color_g, self.base_color_b)
		self.text_color = (255 - self.base_color_r, 255 - self.base_color_g, 255 - self.base_color_b)
		self.border_color = (changed_border_color_r, changed_border_color_g, changed_border_color_r)
		self.border_width = 5
		self.x_offset = 6
		self.y_offset = 6
		self.char_w = 8

		self.line_count = (self.h - 10) // 20
		self.surface = pygame.Surface((self.w, self.h))
		self.cityloc = 'program_files/data/City.mmdb'
		self.my_font = FONTS_DF['display_output']
		self.mode = 'offline'
		self.can_copy = 1
	
		self.current_line_text = ''
		self.on_current_line = True
		self.initial_trigger = False
		self.set_settings = True
		self.started = False
		self.scroll_offset = 0
		self.memorylimit = 200
		self.content = []
		self.line = 0

		##THREAD SHTUFF
		self.goverment_ips = None
		self.ip_save_file = None
		self.blitable_ip = None
		self.proxy_ips = None
		self.scan_file = None
		self.tor_ips = None
		self.myip = None
		self.exc = None
		self.ct = None

		self.get_host_name = False
		self.scan_trigger = False
		self.show_esttime = False
		self.fast_loader = False
		self.scan_finish = False
		self.hidden_ips = False
		self.blacklist = False
		self.know_sys = False
		self.active = False
		self.cleant = False
		self.tstart = True
		self.save = False


		self.how_many_done_so_far = 0
		self.active_time = 0
		self.start_time = 0
		self.use_linx = 0
		self.counter = 0
		self.use_mac = 0
		self.use_win = 0
		self.settime = 0
		self.tcount = 0
		self.ctime = 0
		self.queue = 0
		self.saved = 0
		self.delay = 0
		self.n = 0

		self.show_stats = True
		self.stats = Text((self.x + self.border_width, self.h + self.border_width + 5), '', FONTS_FT['stats_font'], COLORS['WHITE'], mode = 'freetype')

		self.esttime = Text((self.w - 500, 20), '', FONTS_FT['stats_font'], COLORS['WHITE'], mode = 'freetype')

	def display_text(self, text, y, bg = None):
		if text.startswith('[&]'):
			lsb = self.my_font.render('[', 0, COLORS['RED'], bg)
			amper = self.my_font.render('&', 0, COLORS['WHITE'], bg)
			rsb = self.my_font.render(']', 0, COLORS['RED'], bg)
			text = self.my_font.render(text.replace('[&]', ''), 0, COLORS['ORANGE'], bg)
			self.surface.blit(lsb, (self.x_offset, y - self.y_offset))
			self.surface.blit(amper, (self.char_w + self.x_offset, y - self.y_offset))
			self.surface.blit(rsb, ((self.char_w * 2) + self.x_offset, y - self.y_offset))
			self.surface.blit(text, ((self.char_w * 3) + self.x_offset, y - self.y_offset))
		elif text.startswith('[+]'):
			lsb = self.my_font.render('[', 0, COLORS['GREEN'], bg)
			plus = self.my_font.render('+', 0, COLORS['WHITE'], bg)
			rsb = self.my_font.render(']', 0, COLORS['GREEN'], bg)
			text = self.my_font.render(text.replace('[+]', ''), 0, COLORS['WHITE'], bg)
			self.surface.blit(lsb, (self.x_offset, y - self.y_offset))
			self.surface.blit(plus, (self.char_w + self.x_offset, y - self.y_offset))
			self.surface.blit(rsb, ((self.char_w * 2) + self.x_offset, y - self.y_offset))
			self.surface.blit(text, ((self.char_w * 3) + self.x_offset, y - self.y_offset))

		elif text.startswith('[*]'):
			lsb = self.my_font.render('[', 0, COLORS['PURPLE'], bg)
			star = self.my_font.render('*', 0, COLORS['WHITE'], bg)
			rsb = self.my_font.render(']', 0, COLORS['PURPLE'], bg)
			if 'ONLINE' in text:
				pos = text.find('ONLINE')
				text.replace('ONLINE', '      ')
				onln = self.my_font.render('ONLINE', 0, COLORS['GREEN'], bg)
				self.surface.blit(onln, ((self.char_w * pos) + self.x_offset, y - self.y_offset))
			elif 'OFFLINE' in text:
				pos = text.find('OFFLINE')
				text.replace('OFFLINE', '       ')
				offln = self.my_font.render('OFFLINE', 0, COLORS['RED'], bg)
				self.surface.blit(offln, ((self.char_w * pos) + self.x_offset, y - self.y_offset))
			text = self.my_font.render(text.replace('[*]', ''), 0, COLORS['WHITE'], bg)
			self.surface.blit(lsb, (self.x_offset, y - self.y_offset))
			self.surface.blit(star, (self.char_w + self.x_offset, y - self.y_offset))
			self.surface.blit(rsb, ((self.char_w * 2) + self.x_offset, y - self.y_offset))
			self.surface.blit(text, ((self.char_w * 3) + self.x_offset, y - self.y_offset))


		elif text.startswith('[-]'):
			lsb = self.my_font.render('[', 0, COLORS['YELLOW'], bg)
			minus = self.my_font.render('-', 0, COLORS['WHITE'], bg)
			rsb = self.my_font.render(']', 0, COLORS['YELLOW'], bg)
			text = self.my_font.render(text.replace('[-]', ''), 0, COLORS['LYELLOW'], bg)
			self.surface.blit(lsb, (self.x_offset, y - self.y_offset))
			self.surface.blit(minus, (self.char_w + self.x_offset, y - self.y_offset))
			self.surface.blit(rsb, ((self.char_w * 2) + self.x_offset, y - self.y_offset))
			self.surface.blit(text, ((self.char_w * 3) + self.x_offset, y - self.y_offset))

		else:
			text = self.my_font.render(text, 0, COLORS['WHITE'], bg)
			self.surface.blit(text, (self.x_offset, y - self.y_offset))

	def control(self, key: str):
		if key == 'newline':
			self.new_line()
		elif key == 'jumptopress':
			self.on_current_line = True
		else:
			self.on_current_line = True

	def new_line(self):
		self.content.append(self.current_line_text)
		if 'clear' in self.current_line_text:
			self.scroll_offset = 0
			self.on_current_line = True
			self.content = []
			self.current_line_text = ''
			self.content_to_display = []

	def input_text(self, text: str):
		self.current_line_text = text
		self.scroll_offset = 0
		self.new_line()

	def update(self):
		try:
			if self.show_stats:
				if self.mode == 'online':
					stat_text = f'IPs scanned: {str(self.how_many_done_so_far)} | Saved: {str(self.counter)} | Elapsed Time: {self.disptime(self.ctime)} | Queue: {str(self.queue)} | Scanning: {self.blitable_ip}'
				elif self.mode == 'offline':
					if self.save:
						stat_text = f'Tested: {str(self.counter)} | Saved: {str(self.saved)} | Elapsed Time: {self.disptime(self.ctime)} | Scanning: {self.blitable_ip}'
					else:
						stat_text = f'Tested: {str(self.counter)} | Found: {str(self.saved)} | Elapsed Time: {self.disptime(self.ctime)} | Scanning: {self.blitable_ip}'
				self.stats.update_text(stat_text)
		except NameError:
			pass
		if len(self.content) >= self.memorylimit:
			del self.content[0]
		if self.show_esttime:
			self.et()


	def draw(self, _surface):
		self.surface.fill(self.fill_color)
		pygame.draw.rect(self.surface, self.border_color, (0, 0, self.w, self.h), self.border_width)

		if self.on_current_line:
			self.scroll_offset = 0
		if self.line_count < len(self.content):
			for i in range(0 + self.scroll_offset, self.line_count + self.scroll_offset):
				self.display_text(self.content[len(self.content) - (i + 1)], (self.h - 20) - (self.line * 20))
				self.line += 1
		else:		
			for i in range(0 + self.scroll_offset, len(self.content) + self.scroll_offset):
				self.display_text(self.content[len(self.content) - (i + 1)], (self.h - 20) - (self.line * 20))
				self.line += 1
		self.line = 0
		_surface.blit(self.surface, (self.x, self.y))
		if self.show_stats:
			self.stats.draw(_surface)
		if self.show_esttime:
			self.esttime.draw(_surface)
			

	def et(self):
		global speeds
		if self.active:
			self.active_time = time.time() - self.start_time
			try:
				line = line_count
			except NameError:
				line = 0
			zaatime = 10 # needs to be fixed due to speedtest import not working. ##############################################################
			if zaatime < 0:
				zaatime = 0

			try:
				azapercent = round((self.n / line) * 100, 1)
			except ZeroDivisionError:
				azapercent = 0.0
			zztext = f'{azapercent}% Done | Est. Time Remaining: {self.disptime(zaatime)}'
		else:
			self.active_time = 0
			zaatime = self.active_time
			azapercent = 0.0
			zztext = f'{azapercent}% Done | Est. Time Remaining: {self.disptime(zaatime)}'

		self.esttime.update_text(zztext)

	def disptime(self, time):
		return f'{int(time // 3600):02d}:{int(time // 60) - (int(time // 3600) * 60):02d}:{int(time) - (int(time // 60) * 60):02d}'

	def online_scan(self):
		self.queue = self.queue + 1
		self.queue = math.ceil(self.queue)
		randomip = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
		self.blitable_ip = randomip

		if self.hidden_ips >= 1:
			if randomip in self.goverment_ips:
				self.queue -= 1
				return
			elif randomip in self.proxy_ips: 
				self.queue -= 1
				return
			elif randomip in self.tor_ips:
				self.queue -= 1
				return

		if self.blacklist:
			if randomip in self.blacklisted_ips:
				self.queue -= 1
				return

		#Makes sure its not a gateway ip or your own ip.
		if '255.255.255' in randomip:
			self.queue -= 1
			return
		if randomip == self.myip:
			self.queue -= 1
			return
		
		first,second,third,forth = randomip.split('.', 3)

		#Checking to see if it is a lan ip or not.
		if first == '10':
			self.queue -= 1
			return
		if first == '172':
			if int(second) <= 15:
				pass
			elif int(second) >= 16:
				self.queue -= 1
				return
			else:
				pass
		if f'{first}.{second}' == '192.168':
			self.queue -= 1
			return

		if self.use_win == 1:
			response = os.system(f'ping -n 1 ' + randomip + ' >nul')
		elif self.use_mac == 1:
			response = os.system('ping -c 1 ' + randomip + ' > /dev/null 2>&1')
		elif self.use_linx == 1:
			response = os.system('ping -c 1 ' + randomip + ' > /dev/null 2>&1')
		else:
			response = None

		if response == 0:
			try:
				with geoip2.database.Reader(self.cityloc) as reader:
					responce = reader.city(randomip)
					foundcountry = responce.country.name
					countrycode = responce.country.iso_code
					if foundcountry == None:
						foundcountry = 'unknown'
			except:
				foundcountry = 'Does not exist in database...'
				countrycode = 'Does not exist in database...'
			if self.cleant:
				pass
			else:
				self.input_text(f'[*] Scanning: {randomip} = ONLINE | Queue = {str(self.queue)} | Country: {foundcountry}')
			try:
				ipshostname = socket.getfqdn(randomip)
			except:
				self.input_text('[-] Unable to get info.')
				self.queue -= 1
				return

			if self.get_host_name >= 1:
				if ipshostname == randomip:
					pass
					self.input_text(f'[-] ISP: Not found or same as IP')
				else:
					pass
					self.input_text(f'[-] ISP: {ipshostname}')
			else:
				pass

			if ipshostname == 'localhost':
				self.queue -= 1
				return

			
			if self.save:
				if self.keep != None:
					if countrycode == self.keep:
						pass
					else:
						self.queue -= 1
						return
				else:
					pass

				if ipshostname in self.ip_read.read():
					self.input_text('[-] IP already in file')
					self.queue -= 1
					return

				if int(self.get_host_name) >= 1:
					
					writetofile = f'{str(randomip)} -> {str(ipshostname)}\n'
					with open(self.ip_save_file, 'a') as foundips:
						foundips.write(str(writetofile))
						foundips.close()

					self.input_text(f'[+] Added: {randomip}, Number: {str(self.counter)}, Country: {foundcountry}')
					self.counter = self.counter + 1
					
				else:
					writetofile = f'{str(randomip)}\n'
					with open(self.ip_save_file, 'a') as foundips:
						foundips.write(str(writetofile))
						foundips.close()

					self.counter = self.counter + 1
					self.input_text(f'[+] Added: {randomip}, Number: {str(self.counter)}, Country: {foundcountry}')
			else:
				pass
				self.input_text(f'[+] Online: {randomip}, Number: {str(self.counter)}, Country: {foundcountry}')

		else:
			if self.cleant:
				pass
			else:
				self.input_text(f'[*] Scanning: {randomip} = OFFLINE | Queue = {str(self.queue)}')

		self.how_many_done_so_far += 1

		try:
			self.queue -= 1
		except:
			self.queue -= 1

	def offline_scan(self):
		self.queue += 1
		self.queue = math.ceil(self.queue)
		print(self.queue)

		self.counter += 1
		
		randomip = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
		self.blitable_ip = randomip
		first,second,third,forth = randomip.split('.', 3)
		if first == '10':
			self.queue -= 1
			return
		if first == '172':
			if int(second) <= 15:
				pass
			elif int(second) >= 16:
				self.queue -= 1
				return
			else:
				pass
		if f'{first}.{second}' == '192.168':
			self.queue -= 1
			return
		try:
			with geoip2.database.Reader(self.cityloc) as reader:
				responce = reader.city(randomip)
				foundcountry = responce.country.name
				countrycode = responce.country.iso_code
				
				if foundcountry == None:
					foundcountry = 'Unknown'
					savedornot = 'Fail'
					self.input_text(f'[*] IP: {randomip} | {foundcountry}:{countrycode} | {savedornot}')
					self.queue -= 1
					return
		except:
			foundcountry = 'None'
			countrycode = 'None'
			savedornot = 'Fail'
			self.input_text(f'[*] IP: {randomip} | {foundcountry}:{countrycode} | {savedornot}')
			self.queue -= 1
			return
			
		if self.save:
			if self.keep != None:
				if countrycode == self.keep:
					pass
				else:
					savedornot = 'Not right country'
					self.input_text(f'[*] IP: {randomip} | {foundcountry}:{countrycode} | {savedornot}')
					self.queue -= 1
					return
			else:
				pass
			if randomip in self.ip_read:
				savedornot = 'Dupe'
				self.input_text(f'[*] IP: {randomip} | {foundcountry}:{countrycode} | {savedornot}')
				self.queue -= 1
				return
			with open(self.ip_save_file, 'a') as f:
				self.saved += 1
				if self.keep != None:
					f.write(f'{randomip} -> {foundcountry}:{countrycode}\n')

			savedornot = 'Saved!'
			self.input_text(f'[+] IP: {randomip} | {foundcountry}:{countrycode} | {savedornot}')
		else:
			self.saved += 1
			savedornot = 'Clean!'
			self.input_text(f'[+] IP: {randomip} | {foundcountry}:{countrycode} | {savedornot}')

		try:
			self.queue -= 1
		except:
			self.queue -= 1

	def checkips(self):
		global valid_ip_save_file
		global line_count
		global downips
		global speeds
		global upips
		global lines
		global E

		if self.active:
			if self.mode == 'online':
				if self.scan_trigger:
					self.scan_trigger = False
					self.scan_finish = False
					self.n = 0
					upips = 0
					downips = 0
					E = True

					foundips = open(self.scan_file, 'r')
					lines = foundips.readlines()
					line_count = len(lines)
					self.input_text(f'[-] Scanning {line_count} ips.')
					valid_ip_save_file = self.scan_file.replace('.txt', '-scanned.txt')

				while self.n < line_count:
					if self.delay == 1000:
						self.delay = 0
						speeds = speed.get_best_server()
					self.delay += 1
					if E:
						self.start_time = time.time()
						E = False
					ip = lines[self.n]
					ip = ip.replace('\n', '')	

					validonline = open(valid_ip_save_file, 'a+')
					if self.use_win == 1:
						cresponse = os.system(f'ping -n 1 {ip} >nul')
					elif self.use_linx == 1:
						cresponse = os.system(f'ping -c 1 {ip} > /dev/null 2>&1')

					if cresponse == 0:
						##Scans to see if any needed ports are open (experamental)
						#for port in portlist:
						#	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
						#	result = sock.connect_ex((ip,int(port)))
						#	if result == 0:
						#		openports.append(port)
						#		print('ALIVE', port)
						#	else:
						#		print('DEAD', port)
						#		continue
						try:
							with geoip2.database.Reader(self.cityloc) as reader:
								countree = reader.city(ip)
								country = countree.country.name
								if country == None:
									country = 'unknown'
						except:
							country = 'Does not exist in database...'

						self.input_text(f'[+] Scanning: {ip} = UP! | Country: {country}')
						validonline.write(f'{ip}\n')
						upips += 1
					else:
						self.input_text(f'[*] Scanning: {ip} = DOWN!')
						downips += 1

					validonline.close()
					self.n += 1

				if self.active:
					validonline = open(valid_ip_save_file, 'a')
					self.scan_finish = True
					self.input_text('-----------------------------')
					validonline.write('-----------------------------\nResults:\n')
					try:
						self.input_text(f'[+] Online: {upips} ({str(round((upips / line_count) * 100, 1))}%)')
						validonline.write(f'[+] Online: {upips} ({str(round((upips / line_count) * 100, 1))}%)\n')
					except ZeroDivisionError:
						self.input_text(f'[+] Online: {upips} (0.0%)')
						validonline.write(f'[+] Online: {upips} (0.0%)\n')
					try:
						self.input_text(f'[&] Offline: {downips} ({str(round((downips / line_count) * 100, 1))}%)')
						validonline.write(f'[&] Offline: {downips} ({str(round((downips / line_count) * 100, 1))}%)\n')
					except ZeroDivisionError:
						self.input_text(f'[&] Offline: {downips} (0.0%)')
						validonline.write(f'[&] Offline: {downips} (0.0%)\n')
					self.input_text('[-] Done!')
					self.input_text('-----------------------------')
					validonline.write(f'[-] Finished after {self.disptime(time.time() - self.start_time)}\n----------------------------------\n')
					validonline.close()
					self.ct = None
			else: 
				print('???')
		else:
			print('????')

	def startchecker(self, file):
		self.scan_file = file
		if self.tstart:
			self.tstart = False
			try:
				with open(self.scan_file, 'r') as f:
					f.close()
			except FileNotFoundError:
				self.tstart = True
				raise FileNotFoundError
			if self.mode != 'online':
				self.tstart = True
				raise NotImplementedError
			try:
				self.ct = threading.Thread(target = self.checkips)
				self.ct.start()
			except ValueError:
				self.ct = threading.Thread(target = self.checkips)
				self.ct.start()

	def updater_for_check(self, online):
		self.show_esttime = True
		if online:
			self.mode = 'online'
		if not self.know_sys:
			self.know_sys = True	
			if sys.platform == 'linux' or sys.platform == 'linux2':
				self.input_text('[&] Detected linux OS.')
				self.use_linx = True
			elif sys.platform == 'darwin':
				self.input_text('[&] Detected Mac OS')
				self.use_mac = True
				self.input_text('[-] macOS Unsupported - Sorry')
			elif sys.platform == 'win32':
				self.input_text('[&] Detected Windows OS')
				self.use_win = True

	def offlnrunner(self, tcount: int, save: bool, save_loc: str, keep: str):
		if self.set_settings:
			self.keep = keep
			self.save = save
			self.tcount = tcount
			self.ip_save_file = save_loc
			self.mode = 'offline'
			self.cleant = False
			self.hidden_ips = False
			self.set_settings = False

		if self.initial_trigger:
			if not self.know_sys:
				self.know_sys = True
				if sys.platform == 'linux' or sys.platform == 'linux2':
					self.input_text('[&] Detected linux OS.')
					self.use_linx = True
				elif sys.platform == 'darwin':
					self.input_text('[&] Detected Mac OS')
					self.use_mac = True
					self.input_text('[-] macOS Unsupported - Sorry')
				elif sys.platform == 'win32':
					self.input_text('[&] Detected Windows OS')
					self.use_win = True

			self.start_time = time.time()
			self.initial_trigger = False 
			self.ip_save_file = self.ip_save_file.replace('.txt', '-offln.txt')

			self.tcount = int(self.tcount)
			if self.tcount < 1:
				self.fast_loader = False
			else:
				self.fast_loader = True

			if self.keep == '':
				self.keep = None

			if self.save:
				try:
					with open(self.ip_save_file, 'a') as f:
						f.close()
					self.ip_read = open(self.ip_save_file, 'r')
				except FileNotFoundError:
					self.input_text(f'[&] Directory: <{self.ip_save_file}> cannot be used; Resetting to default')
					self.ip_save_file = 'output/foundips.txt'
					self.ip_read = open('output/foundips.txt', 'r')
		
		isthrd = threading.Thread(target = self.offline_scan)
		self.ctime = time.time() - self.start_time

		if self.started == True:
			if self.use_mac == False:
				if self.fast_loader:
					try:			
						if self.queue >= int(self.tcount):
							pass
						else:
							isthrd.start()
					except:
						print('Something went wrong. - Restarting script.')
						time.sleep(3)
				else:
					try:
						time.sleep(0)
						isthrd.start()
					except:
						print('Something went wrong. - Restarting script.')
						time.sleep(3)

	def onlnrunner(self, tcount: int, save: bool, save_loc: str, keep: str, get_host_name: bool, hidden: bool, _clean: bool):
		if self.set_settings:
			self.set_settings = False
			self.get_host_name = get_host_name
			self.ip_save_file = save_loc
			self.hidden_ips = hidden
			self.tcount = tcount
			self.cleant = _clean
			self.keep = keep
			self.mode = 'online'
			self.save = save
			
		if self.initial_trigger:
			if not self.know_sys:
				self.know_sys = True
				if sys.platform == 'linux' or sys.platform == 'linux2':
					self.input_text('[&] Detected linux OS.')
					self.use_linx = True
				elif sys.platform == 'darwin':
					self.input_text('[&] Detected Mac OS')
					self.use_mac = True
					self.input_text('[-] macOS Unsupported - Sorry')
				elif sys.platform == 'win32':
					self.input_text('[&] Detected Windows OS')
					self.use_win = True
			
			if self.save:
				try:
					with open(self.ip_save_file, 'a') as f:
						f.close()
					self.ip_read = open(self.ip_save_file, 'r')
				except FileNotFoundError:
					self.input_text(f'[&] Directory: <{self.ip_save_file}> cannot be used; Resetting to default')
					self.ip_save_file = 'output/foundips.txt'
					self.ip_read = open('output/foundips.txt', 'r')
	
			if self.tcount == '' or int(self.tcount) <= 0:
				self.tcount = 1
				self.fast_loader = False
			else:
				try:
					self.tcount = int(self.tcount)
				except ValueError:
					self.tcount = 1
				self.fast_loader = True
			
			if self.keep == '':
				self.keep = None

			self.start_time = time.time()

			if self.hidden_ips == True:
				self.input_text('[&] Getting goverment IP types...')
				url = 'https://raw.githubusercontent.com/frankielivada22/IPTYPES/main/GOVIPTYPES.txt'
				self.goverment_ips = get(url).text
				self.input_text('[&] Got goverment IP types...')

				self.input_text('[&] Getting proxy IP types...')
				url = 'https://raw.githubusercontent.com/frankielivada22/IPTYPES/main/proxylist.txt'
				self.proxy_ips = get(url).text
				self.input_text('[&] Got proxy IP types...')

				self.input_text('[&] Getting tor IP types...')
				url = 'https://raw.githubusercontent.com/frankielivada22/IPTYPES/main/torips.txt'
				self.tor_ips = get(url).text
				self.input_text('[&] Got tor IP types...')
			
			try:
				self.blacklist = True
				with open('program_files/data/blacklist.txt', 'r') as f:
					self.blacklisted_ips = f.read()
					f.close()
			except:
				self.blacklist = False
				self.blacklisted_ips = None
			if self.keep != None:
				self.input_text(f'[-] Keeping: {self.keep}')
	
			self.myip = get('http://myip.dnsomatic.com/').text
			self.input_text(f'[&] My ip: {self.myip}')
			self.initial_trigger = False

		self.ctime = time.time() - self.start_time
		
		isthrd = threading.Thread(target = self.online_scan)

		if self.started == True:
			if self.use_mac == False:
				if self.fast_loader:
					try:			
						if self.queue >= int(self.tcount):
							pass
						else:
							isthrd.start()
					except:
						print('Something went wrong. - Restarting script.')
						time.sleep(3)
				else:
					try:
						time.sleep(0)
						isthrd.start()
					except:
						print('Something went wrong. - Restarting script.')
						time.sleep(3)