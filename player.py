import pygame
import math
import weapon
import config
import agent

class Player(agent.Agent):
	def __init__(self, x, y):
		super(Player, self).__init__(x, y, 0, 100, 0, 50, None, {}, pygame.Color(255, 0, 255, 0))
		self.new_player()
	def new_player(self):
		self.weapon = weapon.GUN["pistol"]	
		self.inventory["10mm"] = 50
