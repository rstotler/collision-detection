import pygame, random, math
from pygame import *
class start:
	
	def __init__(self):
		
		pygame.init()
		pygame.display.set_caption('Circle-Circle')
		self.win     = pygame.display.set_mode((640,480),0,32)
		self.bg      = pygame.Surface((640,480)) ; self.bg.fill((0,0,0))
		self.clock   = pygame.time.Clock()
		self.circles = self.load_circles()
		self.mouse   = mouse()
		
		pygame.mouse.set_visible(False)
		self.main()
		
	def main(self):
		
		while True:
			
			self.clock.tick(60)
			self.get_input()
			self.update()
			pygame.display.update()
	
	def update(self):
		
		self.win.blit(self.bg,(0,0))
		
		for c in self.circles:
			import math
			dx = c.x - self.mouse.x
			dy = c.y - self.mouse.y
			dr = math.sqrt((dx**2)+(dy**2))
			
			color = c.color
			if dr <= c.size + self.mouse.size : color = [0,255,0]
			
			pygame.draw.circle(self.win,color,[c.x,c.y],c.size)
		
		pygame.draw.circle(self.win,(0,0,255),[self.mouse.x,self.mouse.y],self.mouse.size)
			
	def get_input(self):
		
		self.mouse.x, self.mouse.y = pygame.mouse.get_pos()
		
		for event in pygame.event.get():
			
			if   event.type == QUIT : raise SystemExit
			elif event.type == KEYDOWN and event.key == K_ESCAPE : raise SystemExit

	def load_circles(self):
		
		list = []
		
		for num in range(250):
			loc  = [random.randrange(50,590),random.randrange(50,430)]
			size = random.randrange(10,30)
			list.append(circ(loc,size))
		
		return list

class mouse:
	
	def __init__(self):
		
		self.x = 0
		self.y = 0
		
		self.size = 25

class circ:
	
	def __init__(self,loc,size):
		
		self.x     = loc[0]
		self.y     = loc[1]
		self.size  = size
		self.color = [random.randrange(105,255),0,0]

start()
