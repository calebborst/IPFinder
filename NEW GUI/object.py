import pygame

class Object(pygame.sprite.Sprite):
	def __init__(self, surface, init_pos, sprite_dimentions, mode = 'single'):
		super(Object, self).__init__()

		self.w, self.h = sprite_dimentions
		self.x, self.y = init_pos
		self.surface = surface
		self.change_angle = 0
		self.mode = mode
		self.angle = 0

		self.BASE_TEXTURE = pygame.transform.smoothscale(pygame.image.load(self.sprite).convert(), (self.w, self.h))
		self.texture = self.base_texture
		self.rect = self.surf.get_rect(center = (self.w / 2, self.y / 2))

	def rotate(self):
		self.texture = pygame.transform.rotate(self.BASE_TEXTURE, self.angle)
		self.angle += self.change_angle
		self.angle = self.angle % 360
		self.rect = self.surf.get_rect(center = self.rect.center)

	def move(self, movement_info):
		directions, ammount = movement_info
		if 'up' in directions:
			self.y += amount
		elif'down' in directions:
			self.y -= amount

		if 'right' in directions:
			self.x += amount
		elif direction == 'left':
			self.x -= amount

		self.change_angle = 0
		if direction == 'rot_left':
			self.change_angle = 10
		elif direction == 'rot_right':
			self.change_angle = -10
			obj.rot()

	def draw(self):
		self.texture.blit(self.surface, (self.x, self.y))