import os
import pygame
import math
from pygame.locals import *

import player
import npc
import config
import screen

if __name__ == "__main__":
	pygame.init()
	pygame.display.set_caption("Cent")
	pygame.mouse.set_visible(True)
	pc = player.Player(200, 200)
	agents = [npc.Thug(300, 300), npc.Thug(250, 350)]
	items = {}
	screen = screen.Screen(pc, agents, items)
	clock = pygame.time.Clock()
	while True:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				quit()	
			elif event.type == KEYDOWN:
				if event.key == K_w: pc.y -= 10
				elif event.key == K_s: pc.y += 10
				elif event.key == K_d: pc.x += 10
				elif event.key == K_a: pc.x -= 10
				if event.key == K_UP: screen.y -= 10
			elif event.type == MOUSEBUTTONDOWN:
				x, y = event.pos
				pc.look(x, y)
			screen.draw()

