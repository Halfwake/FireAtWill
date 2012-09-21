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
        def draw(self, surface, fov_surface, cam_x, cam_y):
                pygame.draw.circle(surface, self.color, (self.position[0] - cam_x, self.position[1] - cam_y), self.size / 2)
                if not self.weapon:
                        end_pos = (self.x + cam_x + int(self.size * math.cos(self.direction)), self.y +cam_y- int(self.size * math.sin(self.direction)))
                        pygame.draw.line(surface, self.color, (cam_x + self.position[0], cam_y + self.position[1]), end_pos)
                else:
                        pos1 = (self.weapon.distance * math.sin((self.direction - (self.weapon.spread / 2)) + (math.pi / 2)),
                                self.weapon.distance * math.cos((self.direction - (self.weapon.spread / 2)) + (math.pi / 2)))
			pos1 = (pos1[0] + self.x, pos1[1] + self.y)

                        pos2 = (+ self.weapon.distance * math.sin((self.direction + (self.weapon.spread / 2)) + (math.pi / 2)),
                                self.weapon.distance * math.cos((self.direction + (self.weapon.spread / 2)) + (math.pi / 2)))
			pos2 = (pos2[0] + self.x, pos2[1] + self.y)

                        pygame.draw.polygon(fov_surface, (0, 255, 0 ), [(pos1[0] - cam_x, pos1[1] - cam_y), (pos2[0] - cam_x, pos2[1] - cam_y), (self.position[0] - cam_x, self.position[1] - cam_y)])

        def attack(self, targets):
                if self.weapon:
                        self.weapon.attack(self.x, self.y, self.direction, targets,  self.inventory)
	def look(self, x, y, screen):
		 if self.y - screen.y - y == 0:
                 	self.direction = 0
                 else:
                 	self.direction = math.atan(float(self.x - screen.x - x) / (self.y - screen.y - y)) - (math.pi / 2)
                 if (self.y - screen.y -  y) > 0: self.direction += math.pi
	
	def on(self, screen):
		x, y = screen.x, screen.y
		return (x <= self.x <= x + config.screen_width) and (y <= self.y <= y + config.screen_height)

