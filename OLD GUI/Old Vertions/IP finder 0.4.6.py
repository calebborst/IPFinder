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
title_A = "IPFinder: 0.4.6"#		<-- Title of Customization Window
title_B = "Debug Menu"#				<-- Title of Debug (Output) Window
A_sx_sy_px_py = "600x600+50+50"#	<-- The X and Y Size Followed by the X and Y Position of Creation of Window A 
B_sx_sy_px_py = "600x600+750+50"#	<-- The X and Y Size Followed by the X and Y Position of Creation of Window B

#Widgets#
special_font = "comicsans"#			<-- Title Font
main_font = "comicsans"#			<--	General Font
main_title = "IP Finder"#			<-- Main Title of Program
save_title = "Save to File?"#		<-- Text for Saving to File
threads_title = "Threadcount:"#		<-- Text for Threadcount
target_title = "Targeted Contry:"#	<-- Text for Targeted Country
hostgrab_title = "Grab Hoastname?"#	<-- Text for Grabbing Hoastname
clean_title = "Clean Interface?"#	<-- Text for Clean Interface
DB_title = "Use Maxmind DB?"#		<-- Text for Use Maxmind
button_text_1 = "Find Me IP's"#		<-- Text for Start Button
button_text_2 = "Stop!"#			<-- Text for Stop Button

#Colors#
fg_style  = "#E9DFF0"#				<-- (Hex) Defult Forground Color of any Widget
actv_fg_style = "#925856"#			<-- (Hex) Defult Active Forground Color of any Widget 
bg_style = "#1C1A19"#				<-- (Hex) Defult Background Colorof any Widget
actv_bg_style = "#584855"#			<-- (Hex) Defult Active Background Colorof any Widget
sp_fg_style = "#9418EA"#			<-- (Hex) Special Forground Color of any Widget
actv_sp_fg_style = "#80C370"#		<-- (Hex) Special Active Forground Color of any Widget
sp_bg_style = "#A4EA18"#			<-- (Hex) Special Background Colorof any Widget
actv_sp_bg_style = "#729256"#		<-- (Hex) Special Active Background Colorof any Widget

#Other Variables#
defult_thread_count = 10#			<-- The Defult Thread Count (Safe Range 1 - ~100 Depending on Your Computer), this is redefined in the threadcount textbox.

#-=-DO NOT CHANGE-=-#
ipstart = False#					<-- Defines Whether the IpFinder is On Start of Program {True = On, False = Off}
version_title = "Version: 0.4.6"#	<-- Version Number

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
	global ma_target
	global ma_hostgrab
	global ma_clean
	global ma_use_DB

	#Tickboxes#
	global tb_save
	global tb_target
	global tb_hostgrab
	global tb_clean
	global tb_use_DB

	#Buttons#
	global begin_button
	global stop_button

#todo
# - 2 text boxes


#-=-Titles-=-#
	#Main Title#
	ma_title = tk.Label(main_window, text = main_title, 
						fg = fg_style, 
						bg = bg_style, 
						font = (special_font, 30))
	#Version#
	ma_version = tk.Label(main_window, text = version_title, 
						fg = fg_style, 
						bg = bg_style, 
						font = (main_font, 10))
	#Save?#
	ma_save = tk.Label(main_window, text = save_title, 
						fg = fg_style, 
						bg = bg_style, 
						font = (main_font, 15))
	#Threadcount?#
	ma_threads = tk.Label(main_window, text = threads_title, 
						fg = fg_style, 
						bg = bg_style, 
						font = (main_font, 15))
	#Targeted Contry#
	ma_target = tk.Label(main_window, text = target_title, 
						fg = fg_style, 
						bg = bg_style, 
						font = (main_font, 15))
	#Grab HoastName#
	ma_hostgrab = tk.Label(main_window, text = hostgrab_title, 
						fg = fg_style, 
						bg = bg_style, 
						font = (main_font, 15))
	#Clean Interface#
	ma_clean = tk.Label(main_window, text = clean_title, 
						fg = fg_style, 
						bg = bg_style, 
						font = (main_font, 15))
	#Use Maxmind DB#
	ma_use_DB = tk.Label(main_window, text = DB_title, 
						fg = fg_style, 
						bg = bg_style, 
						font = (main_font, 15))
#-=-Tickboxes-=-#
	ma_save_var = tk.IntVar()
	ma_target_var = tk.IntVar()
	ma_hostgrab_var = tk.IntVar()
	ma_clean_var = tk.IntVar()
	ma_use_DB_var = tk.IntVar()

	#Tickbox for Saving To File#
	tb_save = tk.Checkbutton(main_window, 
							text = '',
							bg = bg_style,
							activeforeground = actv_fg_style,
							activebackground = bg_style,
							variable = ma_save_var, 
							onvalue = 1, 
							offvalue = 0, 
							command = save_check)
	#Tickbox for target#
	tb_target = tk.Checkbutton(main_window,
							text = '',
							bg = bg_style,
							activeforeground = actv_fg_style,
							activebackground = bg_style,
							variable = ma_target_var,
							onvalue = 1,
							offvalue = 0,
							command = target_check)
	#Tickbox For Grabbing Host#
	tb_hostgrab = tk.Checkbutton(main_window, 
							text = '',
							bg = bg_style,
							activeforeground = actv_fg_style,
							activebackground = bg_style,
							variable = ma_hostgrab_var, 
							onvalue = 1, 
							offvalue = 0, 
							command = hostgrab_check)
	#Tickbox for Cleaning Debug Menu#
	tb_clean = tk.Checkbutton(main_window,
							text = '',
							bg = bg_style,
							activeforeground = actv_fg_style,
							activebackground = bg_style,
							variable = ma_clean_var,
							onvalue = 1,
							offvalue = 0,
							command = clean_check)
	#Tickbox for Maxmind DB#
	tb_use_DB = tk.Checkbutton(main_window,
							text = '',
							bg = bg_style,
							activeforeground = actv_fg_style,
							activebackground = bg_style,
							variable = ma_use_DB_var,
							onvalue = 1,
							offvalue = 0,
							command = DB_check)

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

	#Titles - 8#
	ma_title.pack()
	ma_version.pack()
	ma_save.pack()
	ma_threads.pack()
	ma_target.pack()
	ma_hostgrab.pack()
	ma_clean.pack()
	ma_use_DB.pack()
	ma_title.pack_forget()
	ma_version.pack_forget()
	ma_save.pack_forget()
	ma_threads.pack_forget()
	ma_target.pack_forget()
	ma_hostgrab.pack_forget()
	ma_clean.pack_forget()
	ma_use_DB.pack_forget()
	
	#Tick Boxes - 5#
	tb_save.pack()
	tb_target.pack()
	tb_hostgrab.pack()
	tb_clean.pack()
	tb_use_DB.pack()
	tb_save.pack_forget()
	tb_target.pack_forget()
	tb_hostgrab.pack_forget()
	tb_clean.pack_forget()
	tb_use_DB.pack_forget()

	#Buttons - 2#
	begin_button.pack()
	stop_button.pack()
	begin_button.pack_forget()
	stop_button.pack_forget()

	main_menu()

#-=-Debug Menu Widgets-=-#
def generate_dbg_buttons():
	pass

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#

############
#	Menu   #
############

#-=-Main Menu-=-#
def main_menu():
	#Titles#
	ma_title.pack()
	ma_title.place(relx = 0.2, rely = 0.05, anchor = N)
	ma_version.pack()
	ma_version.place(relx = 0.15, rely = 0.12, anchor = N)
	ma_save.pack()
	ma_save.place(relx = 0.3, rely = 0.3, anchor = E)
	ma_threads.pack()
	ma_threads.place(relx = 0.3, rely = 0.35, anchor = E)
	ma_target.pack()
	ma_target.place(relx = 0.3, rely = 0.4, anchor = E)
	ma_hostgrab.pack()
	ma_hostgrab.place(relx = 0.3, rely = 0.45, anchor = E)
	ma_clean.pack()
	ma_clean.place(relx = 0.3, rely = 0.5, anchor = E)
	ma_use_DB.pack()
	ma_use_DB.place(relx = 0.3, rely = 0.55, anchor = E)
	
	#Tickboxes#
	tb_save.pack()
	tb_save.place(relx = 0.3, rely = 0.3, anchor = W)	
	tb_target.pack()
	tb_target.place(relx = 0.3, rely = 0.4, anchor = W)	
	tb_hostgrab.pack()
	tb_hostgrab.place(relx = 0.3, rely = 0.45, anchor = W)	
	tb_clean.pack()
	tb_clean.place(relx = 0.3, rely = 0.5, anchor = W)	
	tb_use_DB.pack()
	tb_use_DB.place(relx = 0.3, rely = 0.55, anchor = W)
	#Buttons#
	begin_button.pack()
	begin_button.place(relx = 0.86, rely = 0.89, anchor = N)


#-=-Dbg Menu-=-#
def dbg_menu():
	pass


#-=-Main Program Loop-=-#
def ipfinderbegintrigger():
	global ipstart
	begin_button.pack()
	begin_button.pack_forget()
	stop_button.pack()
	stop_button.place(relx = 0.86, rely = 0.89, anchor = N)
	ipstart = True
	

def ipfinderendtrigger():
	global ipstart
	stop_button.pack()
	stop_button.pack_forget()
	begin_button.pack()
	begin_button.place(relx = 0.86, rely = 0.89, anchor = N)
	ipstart = False

#Checks#

def save_check():
	pass

def target_check():
	pass

def hostgrab_check():
	pass

def clean_check():
	pass

def DB_check():
	pass

def ipfinder():
	pass	


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
def end_prog():
	try:
		dbg_window.quit()
		main_window.quit()
		sys.exit(0)
	except:
		dbg_window.quit()
		main_window.quit()
		sys.exit(0)

#-=-Running Loop-=-#
if __name__ == '__main__':
	threadA = th.Thread(target = create_window_A)
	threadB = th.Thread(target = create_window_B)
	
	threadA.start()
	threadB.start()

	while True:
		if threadA.is_alive() is False or threadB.is_alive() is False:
			end_prog()
		if ipstart == True:
			ipfinder()