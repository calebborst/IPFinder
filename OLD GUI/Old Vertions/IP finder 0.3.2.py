try:
    import Tkinter as tk
    from Tkinter import *
except:
    import tkinter as tk
    from tkinter import *
import threading as th
import sys
import os

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#

#################
#	Variables   #
#################

#-=-Changable-=-#

#Window Creation#
title_A = "IPFinder: 0.3.2"#		<-- Title of Customization Window
title_B = "Debug Menu"#				<-- Title of Debug (Output) Window
A_sx_sy_px_py = "600x600+50+50"#	<-- The X and Y Size Followed by the X and Y Position of Creation of Window A 
B_sx_sy_px_py = "600x600+750+50"#	<-- The X and Y Size Followed by the X and Y Position of Creation of Window B
#Widgets#
button_text_1 = "Find Me IP's"
button_text_2 = "Stop!"
#Colors#
fg_style  = "#E9DFF0"#				<-- (Hex) Defult Forground Color of any Widget
actv_fg_style = "#925856"#			<-- (Hex) Defult Active Forground Color of any Widget 
bg_style = "#1C1A19"#				<-- (Hex) Defult Background Colorof any Widget
actv_bg_style = "#584855"#			<-- (Hex) Defult Active Background Colorof any Widget
sp_fg_style = "#9418EA"#			<-- (Hex) Special Forground Color of any Widget
actv_sp_fg_style = "#80C370"#		<-- (Hex) Special Active Forground Color of any Widget
sp_bg_style = "#A4EA18"#			<-- (Hex) Special Background Colorof any Widget
actv_sp_bg_style = "#729256"#		<-- (Hex) Special Active Background Colorof any Widget

#-=-DO NOT CHANGE-=-#
ipstart = False#					<-- Defines Whether the IpFinder is On Start of Program {True = On, False = Off}

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#

###############
#	Buttons   #
###############

#-=-Main Buttons-=-#
def generate_buttons():
	global begin_button
	global stop_button

#todo
# - 6 tick Boxes
# - 2 text boxes
# - 7 titles



#-=-Buttons-=-# 
	#Begin Button (Starts the IPFinder)
	begin_button = tk.Button(main_window, 
						text = button_text_1, 
						fg = fg_style, 
						bg = bg_style, 
						activeforeground = actv_fg_style, 
						activebackground = actv_bg_style, 
						command = ipfinderbegintrigger)
	begin_button.config(height = "2", width = "10")
	
	#Stop Button (Stops the Program)
	stop_button = tk.Button(main_window, 
						text = button_text_2, 
						fg = fg_style, 
						bg = bg_style, 
						activeforeground = actv_fg_style, 
						activebackground = actv_bg_style, 
						command = ipfinderendtrigger)
	stop_button.config(height = "2", width = "10")

	begin_button.pack()
	stop_button.pack()

	begin_button.pack_forget()
	stop_button.pack_forget()

	main_menu()

#-=-Dbg Buttons-=-#
def generate_dbg_buttons():
	pass


############
#	Menu   #
############

#-=-Main Menu-=-#
def main_menu():
	begin_button.pack()
	begin_button.place(relx = 0.9, rely = 0.9, anchor = N)


#-=-Dbg Menu-=-#
def dbg_menu():
	pass


#-=-Main Program Loop-=-#
def ipfinderbegintrigger():
	global ipstart
	begin_button.pack()
	begin_button.pack_forget()
	stop_button.pack()
	stop_button.place(relx = 0.9, rely = 0.9, anchor = N)
	ipstart = True
	

def ipfinderendtrigger():
	global ipstart
	stop_button.pack()
	stop_button.pack_forget()
	begin_button.pack()
	begin_button.place(relx = 0.9, rely = 0.9, anchor = N)
	ipstart = False

def ipfinder():
	print('aa1b')


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