try:
	import Tkinter as tk
	from Tkinter import *
except:
	import tkinter as tk
	from tkinter import *
import threading as th
import os
import geoip2.database
import argparse
import random
import socket
import struct
import math
import time
import os
import sys
from sys import platform
from requests import get

#Globaling the Config#
global saveipstofile
global gethostname
global fastloader
global cleant
global info
global good
global bad
global scanning

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#

#################
#	Variables   #
#################

#-=-Changable-=-#

#Window Creation#
title_A = "IPFinder: 0.7.0"#		<-- Title of Customization Window
title_B = "Debug Menu"#				<-- Title of Debug (Output) Window
A_sx_sy_px_py = "400x400+50+50"#	<-- The X and Y Size Followed by the X and Y Position of Creation of Window A 
B_sx_sy_px_py = "600x600+550+50"#	<-- The X and Y Size Followed by the X and Y Position of Creation of Window B

#Widgets#
special_font = "comicsans"#				<-- Title Font
main_font = "comicsans"#				<--	General Font
main_title = "IP Finder"#				<-- Main Title of Program
save_title = "Save to File?"#			<-- Text for Saving to File
threads_title = "Threadcount:"#			<-- Text for Threadcount
disp_country_title = "Display Contry?"#	<-- Text for Displaying Contry 
target_title = "Targeted Contry:"#		<-- Text for Targeted Country
hostgrab_title = "Grab Hoastname?"#		<-- Text for Grabbing Hoastname
clean_title = "Clean Interface?"#		<-- Text for Clean Interface
DB_title = "Use Maxmind DB?"#			<-- Text for Use Maxmind
button_text_1 = "Find Me IP's"#			<-- Text for Start Button
button_text_2 = "Stop!"#				<-- Text for Stop Button

Green, Blue, Red, White, Magenta, Cyan, end, Yellow = '\033[92m', '\033[94m', '\033[91m', '\x1b[37m', '\x1b[35m', '\x1b[36m', '\033[0m', "\033[93m"
good = end + Green
bad = end + Red
info = end + Yellow + "[-]" + Yellow
scanning = end + Magenta + "[" + White + "*" + Magenta + "]"
added = end + Green + "[" + White + "+" + Green + "]"

#Other Variables#
defult_thread_count = 1#			<-- The Defult Thread Count (Safe Range 1 - ~100 Depending on Your Computer), this is redefined in the threadcount textbox.

#-=-DO NOT CHANGE-=-#
#STARTING Color Settings#
x_color_mode = 0#					<-- The Starting Mode Definer
color_mode = 'Dark Mode'#			<-- The Starting Mode
fg_style  = "#E9DFF0"#				<-- (Hex) Defult Forground Color of any Widget
actv_fg_style = "#925856"#			<-- (Hex) Defult Active Forground Color of any Widget 
bg_style = "#1C1A19"#				<-- (Hex) Defult Background Colorof any Widget
actv_bg_style = "#584855"#			<-- (Hex) Defult Active Background Colorof any Widget
sp_fg_style = "#9418EA"#			<-- (Hex) Special Forground Color of any Widget
actv_sp_fg_style = "#80C370"#		<-- (Hex) Special Active Forground Color of any Widget
sp_bg_style = "#A4EA18"#			<-- (Hex) Special Background Colorof any Widget
actv_sp_bg_style = "#729256"#		<-- (Hex) Special Active Background Colorof any Widget
#Main Loop#
myip = get('http://myip.dnsomatic.com/').text
saveipstofile = 0#					<-- Saves the IPs to 'foundips.txt' [0 is Off, 1 is On]
fastloader = 0#						<-- chooses a Threadcount for mainloop [Defults to 1 if Unchanged]
getcountry = 0#						<-- displays Country in Readout [0 is off, 1 is On]
gethostname = 0#					<-- ##### [0 is Off, 1 is On]
cleant = 0#							<-- Only shows online IPs [0 is Off, 1 is On]
keep = 0#							<-- Filter By Contry [0 is Off, 1 is On]
blacklist = 0#						<-- 
workerspeed = 0#					<-- Defines speed of program the higher the number the faster it will run. (set to 1 if no other value supplyed)
usewindows = 0#						]
uselinux = 0#						[<-- Defult Os Detection State Updates On Program Start
usemac = 0#							]

#Other#
ipstart = False#					<-- Defines Whether the IpFinder is On Start of Program {True = On, False = Off}
version_title = "Version: 0.7.0"#	<-- Version Number

#-=-Variables Defined By Program-=-#


#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#

###############
#	Widgets   #
###############

#-=-Main Menu Widgets-=-#
def generate_buttons():
	#Titles#
	global ma_title
	global ma_version
	global ma_save
	global ma_threads
	global ma_disp_country
	global ma_target
	global ma_hostgrab
	global ma_clean
	global ma_use_DB

	#Tickboxes#
	global tb_save
	global tb_fast_mode
	global tb_disp_country
	global tb_target
	global tb_hostgrab
	global tb_clean
	global tb_use_DB

	#Textboxes#
	global wb_country
	global wb_thread_count

	#Buttons#
	global begin_button
	global stop_button

	#Other#
	global color_picker
	global color_trigger
	global color_variable
	global color_mode

	#Variables#
	global ma_save_var
	global ma_fast_mode_var
	global ma_disp_country_var
	global ma_target_var
	global ma_hostgrab_var
	global ma_clean_var
	global ma_use_DB_var
	global resp_country
	global resp_thread_count
	global color_mode
	global x_color_mode

#-=-Titles-=-#
	#Main Title#
	ma_title = tk.Label(main_window, 
						text = main_title, 
						fg = fg_style, 
						bg = bg_style, 
						font = (special_font, 30))
	#Version#
	ma_version = tk.Label(main_window, 
						text = version_title, 
						fg = fg_style, 
						bg = bg_style, 
						font = (main_font, 10))
	#Save?#
	ma_save = tk.Label(main_window, 
						text = save_title, 
						fg = fg_style, 
						bg = bg_style, 
						font = (main_font, 15))
	#Threadcount?#
	ma_threads = tk.Label(main_window, 
						text = threads_title, 
						fg = fg_style, 
						bg = bg_style, 
						font = (main_font, 15))
	#Display Contry??#
	ma_disp_country = tk.Label(main_window, 
						text = disp_country_title, 
						fg = fg_style, 
						bg = bg_style, 
						font = (main_font, 15))
	#Targeted Contry#
	ma_target = tk.Label(main_window, 
						text = target_title, 
						fg = fg_style, 
						bg = bg_style, 
						font = (main_font, 15))
	#Grab HoastName#
	ma_hostgrab = tk.Label(main_window, 
						text = hostgrab_title, 
						fg = fg_style, 
						bg = bg_style, 
						font = (main_font, 15))
	#Clean Interface#
	ma_clean = tk.Label(main_window, 
						text = clean_title, 
						fg = fg_style, 
						bg = bg_style, 
						font = (main_font, 15))
	#Use Maxmind DB#
	ma_use_DB = tk.Label(main_window, 
						text = DB_title, 
						fg = fg_style, 
						bg = bg_style, 
						font = (main_font, 15))
#-=-Tickboxes-=-#
	ma_save_var = tk.IntVar()#			]
	ma_fast_mode_var = tk.IntVar()#		|
	ma_disp_country_var = tk.IntVar()#	|
	ma_target_var = tk.IntVar()#		[<-- Tick Box Variable creation
	ma_hostgrab_var = tk.IntVar()#		|
	ma_clean_var = tk.IntVar()#			|
	ma_use_DB_var = tk.IntVar()#		]

	#Tickbox for Saving To File#
	tb_save = tk.Checkbutton(main_window, 
						text = '',
						bg = bg_style,
						activeforeground = actv_fg_style,
						activebackground = bg_style,
						variable = ma_save_var,  
						command = save_check)
	#Tickbox for ZoOm#
	tb_fast_mode = tk.Checkbutton(main_window, 
						text = '',
						bg = bg_style,
						activeforeground = actv_fg_style,
						activebackground = bg_style,
						variable = ma_fast_mode_var, 
						command = fast_check)
	#Tickbox for Displaying Contry#
	tb_disp_country = tk.Checkbutton(main_window,
						text = '',
						bg = bg_style,
						activeforeground = actv_fg_style,
						activebackground = bg_style,
						variable = ma_disp_country_var,
						command = disp_country_check)
	#Tickbox for target#
	tb_target = tk.Checkbutton(main_window,
						text = '',
						bg = bg_style,
						activeforeground = actv_fg_style,
						activebackground = bg_style,
						variable = ma_target_var,
						command = target_check)
	#Tickbox For Grabbing Host#
	tb_hostgrab = tk.Checkbutton(main_window, 
						text = '',
						bg = bg_style,
						activeforeground = actv_fg_style,
						activebackground = bg_style,
						variable = ma_hostgrab_var, 
						command = hostgrab_check)
	#Tickbox for Cleaning Debug Menu#
	tb_clean = tk.Checkbutton(main_window,
						text = '',
						bg = bg_style,
						activeforeground = actv_fg_style,
						activebackground = bg_style,
						variable = ma_clean_var,
						command = clean_check)
	#Tickbox for Maxmind DB#
	tb_use_DB = tk.Checkbutton(main_window,
						text = '',
						bg = bg_style,
						activeforeground = actv_fg_style,
						activebackground = bg_style,
						variable = ma_use_DB_var,
						command = DB_check)

#-=-Text Boxes-=-#
	resp_country = tk.StringVar()
	resp_thread_count = tk.StringVar()
	#What Contry?#
	wb_country = tk.Entry(main_window, 
						width = 15, 
						textvariable = resp_country,
						bg = bg_style,
						fg = fg_style)	
	#Ammount Of Threads#
	wb_thread_count = tk.Entry(main_window,	
						width = 5, 
						textvariable = resp_thread_count,
						bg = bg_style,
						fg = fg_style)
 
#-=-Buttons-=-# 
	#Begin Button (Starts the IPFinder)#
	begin_button = tk.Button(main_window, 
						text = button_text_1, 
						fg = fg_style, 
						bg = bg_style, 
						activeforeground = actv_fg_style, 
						activebackground = actv_bg_style, 
						command = ipfinderbegintrigger)
	begin_button.config(height = "3", width = "20")
	
	#Stop Button (Stops the Program)
	stop_button = tk.Button(main_window, 
						text = button_text_2, 
						fg = fg_style, 
						bg = bg_style, 
						activeforeground = actv_fg_style, 
						activebackground = actv_bg_style, 
						command = ipfinderendtrigger)
	stop_button.config(height = "3", width = "20")

#-=-Just For You Bud the Strawberry Colorchanger MkIII™-=-#
	color_mode_choices = ['Dark Mode', 'Light Mode']
	color_variable = StringVar()
	color_picker = tk.OptionMenu(main_window, 
						color_variable, 
						*color_mode_choices, 
						command = color_trigger)
	if x_color_mode == 0:
		color_variable.set('Dark Mode')
	elif x_color_mode == 1:
		color_variable.set('Light Mode')
	else:
		x_color_mode = 0
	color_picker.config(fg = fg_style,
						bg = bg_style,
						activeforeground = actv_fg_style,
						activebackground = actv_bg_style)

	#Titles - 9#
	ma_title.pack()
	ma_version.pack()
	ma_save.pack()
	ma_threads.pack()
	ma_disp_country.pack()
	ma_target.pack()
	ma_hostgrab.pack()
	ma_clean.pack()
	ma_use_DB.pack()
	ma_title.pack_forget()
	ma_version.pack_forget()
	ma_save.pack_forget()
	ma_threads.pack_forget()
	ma_disp_country.pack_forget()
	ma_target.pack_forget()
	ma_hostgrab.pack_forget()
	ma_clean.pack_forget()
	ma_use_DB.pack_forget()
	
	#Tick Boxes - 7#
	tb_save.pack()
	tb_fast_mode.pack()
	tb_disp_country.pack()
	tb_target.pack()
	tb_hostgrab.pack()
	tb_clean.pack()
	tb_use_DB.pack()
	tb_save.pack_forget()
	tb_fast_mode.pack_forget()
	tb_disp_country.pack_forget()
	tb_target.pack_forget()
	tb_hostgrab.pack_forget()
	tb_clean.pack_forget()
	tb_use_DB.pack_forget()

	#Text Boxes - 2#
	wb_country.pack()
	wb_thread_count.pack()
	wb_country.pack_forget()
	wb_thread_count.pack_forget()

	#Buttons - 2#
	begin_button.pack()
	stop_button.pack()
	begin_button.pack_forget()
	stop_button.pack_forget()

	#Other - 1#
	color_picker.pack()
	color_picker.pack_forget()

	main_menu()

#-=-Debug Menu Widgets-=-#
def generate_dbg_buttons():
	dbg_menu()

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
def kill_buttons():
	#Titles - 9#
	ma_title.destroy()
	ma_version.destroy()
	ma_save.destroy()
	ma_threads.destroy()
	ma_disp_country.destroy()
	ma_target.destroy()
	ma_hostgrab.destroy()
	ma_clean.destroy()
	ma_use_DB.destroy()
	
	#Tick Boxes - 7#
	tb_save.destroy()
	tb_fast_mode.destroy()
	tb_disp_country.destroy()
	tb_target.destroy()
	tb_hostgrab.destroy()
	tb_clean.destroy()
	tb_use_DB.destroy()

	#Text Boxes - 2#
	wb_country.destroy()
	wb_thread_count.destroy()

	#Buttons - 2#
	begin_button.destroy()
	stop_button.destroy()

	#Other - 1#
	color_picker.destroy()


############
#	Menu   #
############

#-=-Main Menu-=-#
def main_menu():
	#Titles#
	ma_title.pack()
	ma_title.place(relx = 0.3, rely = 0.05, anchor = N)
	ma_version.pack()
	ma_version.place(relx = 0.32, rely = 0.155, anchor = N)
	ma_save.pack()
	ma_save.place(relx = 0.43, rely = 0.3, anchor = E)
	ma_threads.pack()
	ma_threads.place(relx = 0.43, rely = 0.365, anchor = E)
	ma_disp_country.pack()
	ma_disp_country.place(relx = 0.43, rely = 0.43, anchor = E)
	ma_target.pack()
	ma_target.place(relx = 0.43, rely = 0.495, anchor = E)
	ma_hostgrab.pack()
	ma_hostgrab.place(relx = 0.43, rely = 0.56, anchor = E)
	ma_clean.pack()
	ma_clean.place(relx = 0.43, rely = 0.625, anchor = E)

	
	#Tick Boxes#
	tb_save.pack()
	tb_save.place(relx = 0.43, rely = 0.3, anchor = W)
	tb_fast_mode.pack()
	tb_fast_mode.place(relx = 0.43, rely = 0.365, anchor = W)	
	tb_disp_country.pack()
	tb_disp_country.place(relx = 0.43, rely = 0.43, anchor = W)
	tb_target.pack()
	tb_target.place(relx = 0.43, rely = 0.495, anchor = W)	
	tb_hostgrab.pack()
	tb_hostgrab.place(relx = 0.43, rely = 0.56, anchor = W)	
	tb_clean.pack()
	tb_clean.place(relx = 0.43, rely = 0.625, anchor = W)	

	
	#Buttons#
	begin_button.pack()
	begin_button.place(relx = 0.8, rely = 0.85, anchor = N)

	#Other#
	color_picker.pack()
	color_picker.place(relx = 0.8, rely = 0.05, anchor = N)

#-=-Dbg Menu-=-#
def dbg_menu():
	pass


#-=-Main Program Loop-=-#
def ipfinderbegintrigger():
	global ipstart
	global writelinenum
	global looper
	global counter
	global queue
	global workers
	global workerspeed
	
	begin_button.pack()
	begin_button.pack_forget()
	stop_button.pack()
	stop_button.place(relx = 0.8, rely = 0.85, anchor = N)
	
	#-=-Startup Code-=-#
	save_check()
	fast_check()
	disp_country_check()
	target_check()
	hostgrab_check()
	clean_check()
	DB_check()
	print('IpSave: {},\nFastLoad:{},\nWorkerspeed: {},\nKeep: {},\nTarget Contry: {},\nClean Menu: {},\nGet Hoast: {},\nDisplay Contry: {}'\
		.format(saveipstofile, fastloader, workerspeed, keep, countryname, cleant, gethostname, getcountry))

	writelinenum = 0
	looper = 0
	counter = 0
	queue = 0
	workers = workerspeed
	ipstart = True
	

def ipfinderendtrigger():
	global ipstart
	stop_button.pack()
	stop_button.pack_forget()
	begin_button.pack()
	begin_button.place(relx = 0.8, rely = 0.85, anchor = N)
	ipstart = False

#-=-Checks-=-#
def save_check():
	global saveipstofile
	if ma_save_var.get() == 1:
		saveipstofile = 1
	else:
		saveipstofile = 0

def fast_check():
	global fastloader
	global workerspeed
	global defult_thread_count
	if ma_fast_mode_var.get() == 1:
		wb_thread_count.pack()
		wb_thread_count.place(relx = 0.5, rely = 0.365, anchor = W)
		fastloader = 1
		try:
			workerspeed = int(resp_thread_count.get())
		except ValueError:
			fastloader = 0
			workerspeed = defult_thread_count
			print("use Numberz EgG")
	else:
		wb_thread_count.pack()
		wb_thread_count.pack_forget()
		fastloader = 0
		workerspeed = defult_thread_count

def disp_country_check():
	global getcountry
	if ma_disp_country_var.get() == 1:
		getcountry = 1
	else:
		getcountry = 0

def target_check():
	global keep
	global countryname
	if ma_target_var.get() == 1:
		keep = 1
		wb_country.pack()
		wb_country.place(relx = 0.5, rely = 0.495, anchor = W)
		if resp_country.get() != '':#or doesnt match country list (need to impliment this)
			countryname = resp_country.get()
		else:
			countryname = 0
			keep = 0
	else:
		keep = 0
		countryname = 0
		wb_country.pack()
		wb_country.pack_forget()
	if keep == 1:
		print("Aa1a")



def hostgrab_check():
	global gethostname
	if ma_hostgrab_var == 1:
		gethostname = 1
	else: 
		gethostname = 0

def clean_check():
	global cleant
	if ma_clean_var.get == 1:
		cleant = 0
	else:
		cleant = 1

def DB_check():
	pass

def os_checker():
	global usemac
	global uselinux
	global usewindows
	try:
		Aba1 = open("blacklist.txt", "r")
		blacklist = 1
	except:
		blacklist = 0

	if platform == "linux" or platform == "linux2":
		print("Detected linux OS.")
		uselinux = 1
	elif platform == "darwin":
		print("Detected Mac OS")
		usemac = 1
		print("Unsaported atm...")
		end_prog()
	elif platform == "win32":
		print("Detected Windows OS")
		usewindows = 1

#main function of the program
def f():
	global blacklistedips
	global readblacklist
	global writelinenum
	global counter
	global queue

	if fastloader <= 0:
		pass
	else:
		queue = queue + 1
		queue = math.ceil(queue)

	#main code

	#generates a random ip
	randomip = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))

	if blacklist >= 1:
		if randomip in blacklistedips:
			print("Found a black listed ip! Generating a new one.")
			randomip = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
		else:
			pass
	else:
		pass

	#sets console title to the queue count (only if your on windows)
	if usewindows == 1:
		settitle = 'title Queue = ' + str(queue) + ' ' + randomip
		os.system(settitle)

	#where to save the ips to a file
	if saveipstofile >= 1:
		foundips = open('foundips.txt', 'a')
		readips = open('foundips.txt', 'r')
	else:
		pass

	#Makes sure its not a gateway ip or your own ip.
	if "255.255.255" in randomip:
		print("255.255.255 ip found! Generating new ip.")
		randomip = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
	if randomip == myip:
		print("Some how got your own ip...")
		randomip = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
	
	first,second,third,forth = randomip.split('.', 3)

	#Checking to see if it is a lan ip or not.
	if first == "10":
		print("10. lan ip found! Generating new ip. IP was = " + randomip)
		randomip = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
	if first == "172":
		if int(second) <= 15:
			pass
		elif int(second) >= 16:
			print("172. lan ip found! Generating new ip. IP was = " + randomip)
			randomip = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
		else:
			pass
	if first+'.'+second == "192.168":
		print("192.168. lan ip found! Generating new ip. IP was = " + randomip)
		randomip = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))



	if usewindows == 1:
		response = os.system(f"ping -n 1 " + randomip + " >nul")
	elif usemac == 1:
		exit()
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

		if saveipstofile >= 1:
			if keep >= 1:
				if countrycode == str(countryname):
					pass
				else:
					queue = queue - 1
					return
			else:
				pass

			if ipshostname in readips.read():
				print("IP already in file")
				return

			if int(gethostname) >= 1:
				writetofile = str(randomip) + " = " + str(ipshostname) + "\n"
				foundips.write(str(writetofile))
				foundips.close()
				writelinenum = writelinenum + 1
				counter = counter + 1
				if getcountry >= 1:
					print(added + "Added:" + end, randomip, "Number:", good + str(counter) + end + " Country: " + foundcountry)
				else:
					print(added + "Added:" + end, randomip, "Number:", good + str(counter) + end)
			else:
				writetofile = str(randomip) + "\n"
				foundips.write(str(writetofile))
				foundips.close()
				writelinenum = writelinenum + 1
				counter = counter + 1
				if getcountry >= 1:
					print(added + "Added:" + end, randomip, "Number:", good + str(counter) + end + " Country: " + foundcountry)
				else:
					print(added + "Added:" + end, randomip, "Number:", good + str(counter) + end)
		else:
			if getcountry >= 1:
				print(added + "Added:" + end, randomip, "Number:", good + str(counter) + end + " Country: " + foundcountry)
			else:
				print(added + "Added:" + end, randomip, "Number:", good + str(counter) + end)


	else:
		if cleant >= 1:
			pass
		else:
			print(scanning + "Scanning:" + end, randomip, "=", bad + 'DOWN!' + end + " Queue = " + str(queue))

	#main code ends here
	if fastloader <= 0:
		pass
	else:
		queue = queue - 1



def color_trigger(color_variable):
	global fg_style
	global bg_style
	global actv_fg_style
	global actv_bg_style
	global sp_fg_style
	global sp_bg_style
	global actv_sp_fg_style
	global actv_sp_bg_style
	global x_color_mode
	print(color_variable)
	if color_variable == str('Dark Mode') and x_color_mode != 0:
		x_color_mode = 0
		fg_style  = "#E9DFF0"#				<-- (Hex) Defult Forground Color of any Widget
		actv_fg_style = "#925856"#			<-- (Hex) Defult Active Forground Color of any Widget 
		bg_style = "#1C1A19"#				<-- (Hex) Defult Background Colorof any Widget
		actv_bg_style = "#584855"#			<-- (Hex) Defult Active Background Colorof any Widget
		sp_fg_style = "#9418EA"#			<-- (Hex) Special Forground Color of any Widget
		actv_sp_fg_style = "#80C370"#		<-- (Hex) Special Active Forground Color of any Widget
		sp_bg_style = "#A4EA18"#			<-- (Hex) Special Background Colorof any Widget
		actv_sp_bg_style = "#729256"#		<-- (Hex) Special Active Background Colorof any Widget

		kill_buttons()
		restart_windows()
		generate_buttons()
		generate_dbg_buttons()
		
	elif color_variable == str('Light Mode') and x_color_mode != 1:
		x_color_mode = 1
		fg_style  = 'Black'
		actv_fg_style = 'Blue'
		bg_style = 'White'
		actv_bg_style = 'Grey'
		sp_fg_style = 'Red'
		actv_sp_fg_style = 'Orange'
		sp_bg_style = 'White'
		actv_sp_bg_style = 'Black'
		
		kill_buttons()
		restart_windows()
		generate_buttons()
		generate_dbg_buttons()
	
	else:
		print("Setting Already Selected")



#-=-Creates Main Window-=-#
def create_window_A():
	global main_window
	main_window = tk.Tk()
	generate_buttons()
	main_menu()
	main_window.title(title_A)
	main_window.geometry(A_sx_sy_px_py)
	main_window.config(bg = bg_style)
	main_window.mainloop()


#-=-Creates Debug Window-=-#
def create_window_B():
	global dbg_window
	dbg_window = tk.Tk()
	generate_dbg_buttons()
	dbg_menu()
	dbg_window.title(title_B)
	dbg_window.geometry(B_sx_sy_px_py)
	dbg_window.config(bg = bg_style)
	dbg_window.mainloop()

#-=-Killing Program-=-#
def restart_windows():
	restart_function = True
	try:
		main_window.quit()
	except:
		print("Error 1Ab")
		sys.exit(0)
	try:
		dbg_window.quit()
	except:
		print("Error 1Ac")
	#threadB.terminate()
	#threadA.terminate() 
	threadA.stop()
	threadB.stop()
	create_windows()

def end_prog():
	try:
		dbg_window.quit()
		main_window.quit()
		sys.exit(0)
	except:
		dbg_window.quit()
		main_window.quit()
		sys.exit(0)

os_checker()
#-=-Running Loop-=-#
class StoppableThread(th.Thread):
	def __init__(self,  *args, **kwargs):
		super(StoppableThread, self).__init__(*args, **kwargs)
		self._stop_event = th.Event()

	def stop(self):
		self._stop_event.set()

	def stopped(self):
		return self._stop_event.is_set()

def create_windows():
	global threadA
	global threadB
	if __name__ == '__main__':
		#threadA = th.Thread(target = create_window_A)
		#threadB = th.Thread(target = create_window_B)
		threadA = StoppableThread(target = create_window_A)
		threadB = StoppableThread(target = create_window_B)
		threadA.setDaemon(True)
		threadB.setDaemon(True)
		
		threadA.start()
		threadB.start()
		restart_windows = False

create_windows()
while True:
	if threadA.is_alive() is False or threadB.is_alive() is False and restart_windows != True:
		end_prog()
	if ipstart == True:
		if __name__ == "__main__":
			while True:
				#setting thread
				t = th.Thread(target=f)
		
				if fastloader >= 1:
					#NEW QUEUE METHOD
					try:			
						if queue >= workers:
							pass
						else:
							t.start()
					except:
						print("Something went wrong. - Restarting script.")
						time.sleep(3)
				else:
					try:
						time.sleep(1.0)
						t.start()
					except:
						print("Something went wrong. - Restarting script.")
						time.sleep(3)
		