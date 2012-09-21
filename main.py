import os
import pygame
import math
from pygame.locals import *

import player
import npc
import config
import screen
import messenger

if __name__ == "__main__":
	pygame.init()
	pygame.display.set_caption("Cent")
	pygame.mouse.set_visible(True)

	messenger.Messenger.pc = player.Player(200, 200)
	messenger.Messenger.agents = [npc.Thug(300, 300), npc.Thug(250, 350)]
	messenger.Messenger.items = []

	screen = screen.Screen(messenger.Messenger.pc, messenger.Messenger.agents, messenger.Messenger.items)
	clock = pygame.time.Clock()
	while True:
		pc = messenger.Messenger.pc
		agents = messenger.Messenger.agents
		items = messenger.Messenger.items
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
				if event.key == K_UP: screen.y += 10
				elif event.key == K_DOWN: screen.y -= 10
				elif event.key == K_RIGHT: screen.x -= 10
				elif event.key == K_LEFT: screen.x += 10
				if event.key == K_SPACE: pc.attack(agents)
			elif event.type == MOUSEBUTTONDOWN:
				x, y = event.pos
				pc.look(x, y, screen)
			screen.draw()

