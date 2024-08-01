import json
import pygame
from variables import ESSENTIAL_ASSETS

MISSING_TEXTURE = ESSENTIAL_ASSETS['texture_not_found']

def image_loader(image_location, wh, colorkey = (69, 0, 69), is_alpha_enabled = False):
	if not is_alpha_enabled:
		try:
			image = pygame.image.load(image_location).convert()
		except:
			image = MISSING_TEXTURE
		image.set_colorkey(colorkey)
		image = pygame.transform.scale(image, wh)
	else:
		try:
			image = pygame.image.load(image_location).convert_alpha()
		except:
			image = MISSING_TEXTURE
		image = pygame.transform.scale(image, wh)
	return image

def animation_loader(file_location, desired_wh, frames_info):
		frame_list = []
		desired_w, desired_h = desired_wh
		def_frame_name, number_of_frames = frames_info
		sprite_sheet = pygame.image.load(file_location).convert()
		meta_data = file_location.replace('png', 'json')
		with open(meta_data) as f:
			data = json.load(f)
			f.close()
		while x <= number_of_frames:
			frame_name = def_frame_name + str(x)
			sprite = data['frames'][frame_name]['frame']
			x, y, w, h = sprite["x"], sprite["y"], sprite["w"], sprite["h"]
			frame = pygame.Surface((w, h))
			frame.set_colorkey(COLORS['BLACK'])
			frame.blit(sprite_sheet, (0, 0), (x, y, w, h)).convert()
			frame = pygame.transform.scale(frame, (desired_w, desired_h))
			frame_list.append(frame)
		return frame_list

def font_loader(font, size, _type = 'freetype'):
	if _type == 'freetype':
		return pygame.freetype.Font(font, size)
	elif _type == 'normal':
		return pygame.font.Font(font, size)
	else:
		print('_type Error')
		raise ValueError
	
def sound_loader(sound_location):
	return pygame.mixer.Sound(sound_location)

def button_loader(button_location, button_wh, sound_loudness):
	sound_location = button_location.replace('textures', 'sounds')
	inactive_button = image_loader(button_location, button_wh)
	hovered_button = image_loader(button_location.replace('_A', '_B'), button_wh)
	try:
		selected_button = image_loader(button_location.replace('_A', '_C'), button_wh)
	except FileNotFoundError:
		selected_button = hovered_button

	try:
		select_button_sound = sound_loader(sound_location.replace('_A.png', '_select.wav'))
		select_button_sound.set_volume(sound_loudness)
	except FileNotFoundError:
		select_button_sound = 'N/A'
	try:
		deselect_button_sound = sound_loader(sound_location.replace('_A.png', '_deselect.wav'))
		deselect_button_sound.set_volume(sound_loudness)
	except FileNotFoundError:
		deselect_button_sound = select_button_sound
	try:
		hover_button_sound = sound_loader(sound_location.replace('_A.png', '_hover.wav'))
		hover_button_sound.set_volume(sound_loudness)
	except FileNotFoundError:
		hover_button_sound = 'N/A'
	try:
		dehover_button_sound = sound_loader(sound_location.replace('_A.png', '_dehover.wav'))
		dehover_button_sound.set_volume(sound_loudness)
	except FileNotFoundError:
		dehover_button_sound = 'N/A'

	button = {
			'sprites': {
					'inactive': inactive_button,
					'hovering': hovered_button,
					'selected': selected_button
				},
			'sounds': {
					'select': select_button_sound,
					'deselect': deselect_button_sound,
					'hover': hover_button_sound,
					'dehover': dehover_button_sound
				}
		}

	return button