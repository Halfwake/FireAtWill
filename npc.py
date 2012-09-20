import pygame 
import weapon
import agent

class Npc(agent.Agent):
	def __init__(self, x, y, direction, health, armor, size, weapon, inventory, color):
		super(agent.Agent, self).__init__(x, y, direction, health, armor, size, weapon, inventory, color)

class Thug(Npc):
	def __init__(self, x, y):
		super(Npc, self).__init__(x, y, 0, 100, 50, 50,  weapon.GUN["pistol"], {"10mm" : 100}, pygame.Color(255, 0, 0))
