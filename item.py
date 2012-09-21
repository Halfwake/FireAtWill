import pygame
import math
import config

class Item(object):
	def __init__(self, x, y, direction):
		self.x = x
		self.y = y
		self.direction = direction
	def draw(self, surface, fov_surface, cam_x, cam_y):
		pass

class GunShot(Item):
	def __init__(self, x, y, slope, distance):
		self.x = x
		self.y = y
		self.slope = slope
		self.distance = distance
	def draw(self, surface, fov_surface, cam_x, cam_y):
		x = self.x
		y = self.y
		pygame.draw.line(surface, (0, 255, 255), (x, y), (x + (self.slope * self.distance), y + (self.slope * self.distance)))
	def on(self, screen):
                x, y = screen.x, screen.y
                return (x <= self.x <= x + config.screen_width) and (y <= self.y <= y + config.screen_height)

