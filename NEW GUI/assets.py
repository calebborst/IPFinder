from variables import COLORS, FONTS_DF, FONTS_FT, SOUNDS, SCREEN_SIZE_x, SCREEN_SIZE_y 
from sprite import Sprite, InfoBox, DisplayBox
from output import Output
from button import Button
from text import Text, TextBox

button_offset = 40
w = SCREEN_SIZE_x - 20
h = SCREEN_SIZE_y - 10 - button_offset 
hh = SCREEN_SIZE_y - 20

output_size = (10, 10, w, h)
check_size = (10, 50, w, h)

ASSETS = {
	'ts_title': Text((20, 40), 'IP Finder', FONTS_FT['square'], shadow = True, mode = 'freetype'),
	'ts_offline': Text((135, 35), 'OFFLINE', FONTS_DF['ssquare'], COLORS['RED'], 25),
	'os_output': Output(output_size, (20, 20, 20)),
	'ts_scan': Button('program_files/textures/menu_button/button_A.png', (20, 110, 100, 60), 'click', text = 'Scan'),
	'ts_check': Button('program_files/textures/menu_button/button_A.png', (20, 190, 100, 60), 'click', text = 'Check'),
	#'os_back': Button('program_files/textures/back_button/back_button_A.png', (((SCREEN_SIZE_x / 2) - 30, (SCREEN_SIZE_y - 10) - button_offset)), (60, button_offset), 'click'),	
	's_b_GO': Button('program_files/textures/GO_button/GO_button_A.png', (640, 340, 50, 50), 'click', 0.3),
	's_b_save_to_file': Button('program_files/textures/tickbox/tickbox_A.png', (20, 41, 30, 30), 'toggle'),
	's_b_host': Button('program_files/textures/tickbox/tickbox_A.png', (20, 71, 30, 30), 'toggle'),
	's_b_hidden': Button('program_files/textures/tickbox/tickbox_A.png', (20, 101, 30, 30), 'toggle'),
	's_b_clean': Button('program_files/textures/tickbox/tickbox_A.png', (20, 161, 30, 30), 'toggle'),
	's_t_save_to_file': Text((60, 48), 'Save IPs:', FONTS_DF['Ssquare'], COLORS['WHITE']),
	's_t_host': Text((60, 78), 'Grab Host', FONTS_DF['Ssquare'], COLORS['WHITE']),
	's_t_hidden': Text((60, 108), 'Filter Scary Stuff', FONTS_DF['Ssquare'], COLORS['WHITE']),
	's_t_thread': Text((60, 138), 'Threadcount', FONTS_DF['Ssquare'], COLORS['WHITE']),
	's_t_clean': Text((60, 168), 'Clean Output', FONTS_DF['Ssquare'], COLORS['WHITE']),
	's_t_keepc': Text((60, 198), 'Keep Specific', FONTS_DF['Ssquare'], COLORS['WHITE']),
	's_i_save_to_file': InfoBox((395, 76), 'Save:\nSave to a file Yes/No\n(Optional) Path to file, eg: output/an_file.txt', COLORS['LGREY']),
	's_i_host': InfoBox((450, 52), 'Grab Host:\nDisplays and Saves (if selected) the ISP of Scanned IP', COLORS['LGREY']),
	's_i_hidden': InfoBox((400, 76), 'Filter:\nFilters out Tor, Government and Proxy (VPN) IPs\nBetter for reliable data', COLORS['LGREY']),
	's_i_thread': InfoBox((410, 110), 'Threads:\nMaximum allowed active threads\nlower = less memory usage\nDefault = 1\nIf set 0 there will be no limit (use at own risk)', COLORS['LGREY']),
	's_i_clean': InfoBox((200, 52), 'Clean:\nOnly Display Online IPs', COLORS['LGREY']),
	's_i_keepc': InfoBox((300, 134), 'Keep Specific\nOnly keep IPs from X country\nCountry signified by country code:\nEg: US or UK\nOnly one country can be used\nLeft blank setting is off', COLORS['LGREY']),
	's_p_save_to_file': TextBox(-1, (150, 46, 400, 26), COLORS['BG_COLOR'], 'output/foundips.txt'),
	's_p_thread': TextBox(4, (8, 131, 44, 34), COLORS['BG_COLOR'], '1'),
	's_p_keepc': TextBox(3, (8, 191, 44, 34), COLORS['BG_COLOR']),
	'cs_start_button': Button('program_files/textures/GO_button/GO_button_A.png', (SCREEN_SIZE_x - 40, 10, 30, 30), 'click', 0.3),
	'cs_output': Output(check_size, (20, 20, 20)),
	'cs_file': TextBox(-1, (10, 10, 300, 30), COLORS['BG_COLOR'], 'output/foundips.txt')
}