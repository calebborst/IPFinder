import pygame
from asset_loader import button_loader
from variables import FONTS_DF, COLORS

class Button:
	def __init__(self, button_file_location, rect, mode, sound_loudness = 0.5, text = None, textinfo: list = [FONTS_DF['Ssquare'], COLORS['WHITE'], 11, 20], action = None):# mode = toggle/click/ <hold not currently functional>
		self.mode = mode
		self.action = action
		self.x, self.y, self.w, self.h = rect
		self.button_assets = button_loader(button_file_location, (self.w, self.h), sound_loudness)
		self.surface = pygame.Surface((self.w, self.h))
		self.my_font, self.textcolor, self.textw, self.texth = textinfo
		self.revtextcolor = (255 - self.textcolor[0], 255 - self.textcolor[1], 255 - self.textcolor[2])
		if text == None:
			self.text = False
			self.textpos = 0
		else:
			self.text = self.my_font.render(text, 0, self.textcolor, None)
			self.revtext = self.my_font.render(text, 0, self.revtextcolor, None)
			self.textpos = ((self.w/2) - ((self.textw * len(text) / 2)), (self.h/2) - (self.texth / 2))

		self.hovered = False
		self.selected = False
		self.new_hover = False
		self.new_dehover = False
		self.new_selection = False
		self.new_deselection = False

		self.cooldown = 0

	def check(self):
		mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
		if mouse_pos_x in range(self.x, self.x + self.w + 1):
			if mouse_pos_y in range(self.y, self.y + self.h + 1):
				if self.hovered == False:
					self.new_hover = True
				self.hovered = True
			else:
				if self.hovered == True:
					self.new_dehover = True
				self.hovered = False
		else:
			if self.hovered == True:
				self.new_dehover = True
			self.hovered = False

	def selector(self):
		if self.hovered:
			if self.mode == 'toggle':
				if self.selected == False and self.cooldown == 0:
					self.selected = True
					self.new_selection = True
				elif self.selected == True and self.cooldown == 0:
					self.selected = False
					self.new_deselection = True
				self.cooldown = 40
			elif self.mode == 'hold':
				if self.selected == False:
					self.new_selection = True
				self.selected = True
				self.cooldown = 2
			elif self.mode == 'click':
				if self.selected == False and self.cooldown == 0:
					self.new_selection = True
					self.selected = True
				self.cooldown = 5
			if self.selected == True:
				return self.action
		else:
			return None


	def draw(self, _surface):
		self.check()
		self.surface.fill(COLORS['BG_COLOR'])
		if self.hovered:
			self.surface.blit(self.button_assets['sprites']['hovering'], (0, 0))
		elif self.selected:
			self.surface.blit(self.button_assets['sprites']['selected'], (0, 0)) 
		else:
			self.surface.blit(self.button_assets['sprites']['inactive'], (0, 0))

		if self.new_hover:
			self.new_hover = False
			if not self.button_assets['sounds']['hover'] == 'N/A':
				self.button_assets['sounds']['hover'].play()
		if self.new_dehover:
			self.new_dehover = False
			if not self.button_assets['sounds']['dehover'] == 'N/A':
				self.button_assets['sounds']['dehover'].play()
		if self.new_selection:
			self.new_selection = False
			if not self.button_assets['sounds']['select'] == 'N/A':
				self.button_assets['sounds']['select'].play()
		if self.new_deselection == True:
			self.new_deselection = False
			if not self.button_assets['sounds']['deselect'] == 'N/A':
				self.button_assets['sounds']['deselect'].play()

		if self.cooldown > 0:
			self.cooldown -= 1
		if self.cooldown == 0:
			if self.mode == 'click':
				self.selected = False
			if self.mode == 'hold':
				if self.selected == True:
					self.new_deselection = True
				self.selected = False

		if self.text != False:
			if self.hovered or self.selected:
				self.surface.blit(self.revtext, self.textpos)
			else:
				self.surface.blit(self.text, self.textpos)

		_surface.blit(self.surface, (self.x,self.y))