import pygame
import math
import config

class Agent(object):
        def __init__(self, x, y, direction, health, armor, size, weapon, inventory, color):
                self.color = color

                self.direction = direction
                self.x = x
                self.y = y

                self.health = health
                self.armor = armor
                self.size = size

                self.weapon= weapon
                self.inventory = inventory

        @property
        def position(self):
                return (self.x, self.y)
        def turn(self, direction):
                self.direction = direction
        def draw(self, surface, fov_surface, x, y):
                pygame.draw.circle(surface, self.color, self.position, self.size / 2)
                if not self.weapon:
                        end_pos = (self.x + x + int(self.size * math.cos(self.direction)), self.y + y - int(self.size * math.sin(self.direction)))
                        pygame.draw.line(surface, self.color, self.position, end_pos)
                else:
                        pos1 = (x + self.x + self.weapon.distance * math.sin((self.direction - (self.weapon.spread / 2)) + (math.pi / 2)),
                                y + self.y + self.weapon.distance * math.cos((self.direction - (self.weapon.spread / 2)) + (math.pi / 2)))
                        pos2 = (x + self.x + self.weapon.distance * math.sin((self.direction + (self.weapon.spread / 2)) + (math.pi / 2)),
                                y + self.y + self.weapon.distance * math.cos((self.direction + (self.weapon.spread / 2)) + (math.pi / 2)))
                        pos3 = (x + self.x + self.weapon.distance * math.sin(self.direction),
                                y + self.y + self.weapon.distance * math.cos(self.direction))
                        pygame.draw.polygon(fov_surface, (0, 255, 0 ), [pos1, pos2, self.position])

        def attack(self, targets):
                if self.weapon:
                        self.weapon.attack(targets, self.x, self.y, self.direction, self.inventory)
	def look(self, x, y):
		 if self.y - y == 0:
                 	self.direction = 0
                 else:
                 	self.direction = math.atan(float(self.x - x) / (self.y - y)) - (math.pi / 2)
                 if (self.y - y) > 0: self.direction += math.pi
	
	def on(self, screen):
		x, y = screen.x, screen.y
		return (x <= self.x <= x + config.screen_width) and (y <= self.y <= y + config.screen_height)

