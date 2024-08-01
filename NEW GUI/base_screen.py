import pygame.freetype
from variables import COLORS, ESSENTIAL_ASSETS

class BaseScreen:
	def __init__(self, next_context, base_class):
		self.prog_class = base_class
		self.next_context = next_context
		
		self.show_fps = self.prog_class.show_fps
		self.clock = self.prog_class.clock
		self.MAX_FPS = self.prog_class.MAX_FPS
		self.layers = self.prog_class.layers

		self.display_layer = self.layers['display_layer']['layer']
		
		self.font =	ESSENTIAL_ASSETS['fps']

		self.prog_end = False
		self.go_to_next = False

	def update(self, events):		
		#To Be Overridden#
		pass

	def render(self):
		#To Be Overridden#
		pass

	def render_start(self, color = COLORS['BG_COLOR']):
		self.display_layer.fill(color)

	def render_finish(self):
		pass

	def check_dead(self):
		if self.prog_end:
			return True
		else:
			pass

	def switch_screen(self, screen_switch, _type_ = 'normal'):
		self.prog_class.switch_context(_type_, screen_switch, self.prog_class)