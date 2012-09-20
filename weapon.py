import math

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
	def attack(self, x, y, direction, targets, inventory):
		if self.ammo in inventory and inventory[self.ammo] > 0:
			shots = []
			for i in xrange(busts):
				shots += math.tan(random.randrange(direction - self.spread, direction + self.spread))
			if ammo:
				self.ammo -= self.burst
				for target in targets:
					distance = math.sqrt(float(target.y - y) ** 2 + (target.x - x) ** 2)
					slope - (target.y - y) / (target.x - x)
					if distance <= self.distance + target.size:
						for shot in shots:
							pyglet.draw.line((0, 255, 255), (self.x, self.y), (self.x + (slope * self.distance), self.y + (slope * self.distance)))
							if atan(slope) - self.spread < atan(shot) < atan(slope) + self.spread:
								target.health -= damage 
								
			else:
				pass

GUN = {"pistol" : Gun(10, 400, math.pi / 32, "10mm", 1)}
