import pygame
import config

class Screen(object):
	def __init__(self, pc, agents, items):
		self.pc = pc
		self.agents = agents
		self.items = items

		self.x = 0
		self.y = 0

		self.screen = pygame.display.set_mode((config.screen_width, config.screen_height)) 
        	pygame.display.set_caption(config.game_name) 
        	pygame.mouse.set_visible(True)

        	self.background = pygame.Surface(self.screen.get_size())
        	self.background = self.background.convert()
        	self.background.fill((50, 50, 50))

        	self.fov = pygame.Surface(self.screen.get_size())
        	self.fov = self.fov.convert()
       	 	self.fov.set_alpha(config.cone_alpha)
	def draw(self):
          	self.screen.blit(self.fov, (0, 0))
               	self.fov.fill((0, 0, 0))
                for agent in self.agents:
                	if agent.on(self):
				agent.draw(self.screen , self.fov, self.x, self.y)
               	self.pc.draw(self.screen, self.fov, self.x, self.y)
		pygame.display.flip()
                self.screen.blit(self.background, (0, 0))
