import pygame
import math
import random

import messenger
import item

class Weapon(object):
	def __init__(self, damage, distance, spread):
		self._damage = damage
		self._distance = distance
		self.spread = spread
	@property
	def damage(self):
		return self._damage
	@property
	def distance(self):
		return self._distance
	def attack(self, x, y, direction, targets):
		for target in targets:
			if float(target.x - x) / (target.y - y) <= self.distance:
				target.health -= damage

class Gun(Weapon):
	def __init__(self, damage, distance, spread, ammo, burst):
		super(Gun, self).__init__(damage, distance, spread)	
		self.ammo = ammo
		self.burst = burst
	def attack(self,x, y, direction, targets, inventory):
		if self.ammo in inventory and inventory[self.ammo] > 0:
			shots = []
			for i in xrange(self.burst):
				slope = math.tan(random.uniform(float(direction) - self.spread, float(direction) + self.spread))
				shot = item.GunShot(x, y, slope)
				messenger.Messenger.addItem(shot)
				shots.append(shot)
			if inventory[self.ammo]:
				inventory[self.ammo] -= self.burst
				for target in targets:
					distance = math.sqrt(float(target.y - y) ** 2 + (target.x - x) ** 2)
					slope = (target.y - y) / (target.x - x)
					if distance <= self.distance + target.size:
						for shot in shots:
							messenger.Messenger.addItem(shot)
							if math.atan(slope) - self.spread < math.atan(shot.slope) < math.atan(slope.slope) + self.spread:
								target.health -= damage 
								
			else:
				pass

GUN = {"pistol" : Gun(10, 400, math.pi / 32, "10mm", 1)}
