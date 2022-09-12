import pygame, random, math
from pygame import *

class start:
	
	def __init__(self):
		
		pygame.init()
		pygame.display.set_caption('Circle-Rect')
		self.win   = pygame.display.set_mode((640,480),0,32)
		self.bg    = pygame.Surface((640,480)) ; self.bg.fill((0,0,0))
		self.clock = pygame.time.Clock()
		self.rects = self.load_rects()
		self.mouse = mouse()
		
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
		
		for r in self.rects:
			
			color = r.color
			if r.intersects(self.mouse) : color = [0,255,0]
		
			pygame.draw.rect(self.win,color,[r.x,r.y,r.w,r.h])
		
		pygame.draw.circle(self.win,(0,0,255),[self.mouse.x,self.mouse.y],self.mouse.r)
			
	def get_input(self):
		
		self.mouse.x, self.mouse.y = pygame.mouse.get_pos()
		
		for event in pygame.event.get():
			
			if   event.type == QUIT : raise SystemExit
			elif event.type == KEYDOWN and event.key == K_ESCAPE : raise SystemExit

	def load_rects(self):
		
		list = []
		for num in range(100) : list.append(rectangle())
		return list

class mouse:
	
	def __init__(self):
		
		self.x = 0
		self.y = 0
		self.r = 25

class rectangle:
	
	def __init__(self):
		
		self.x = random.randrange(50,590)
		self.y = random.randrange(50,430)
		self.w = random.randrange(10,100)
		self.h = random.randrange(10,75)
		
		self.color = [random.randrange(105,255),0,0]
		
	def intersects(self,mouse):
		
		rectcenter = {'x':self.x+self.w/2, 'y':self.y+self.h/2}
		w  = self.w/2
		h  = self.h/2
		dx = abs(mouse.x-rectcenter['x'])
		dy = abs(mouse.y-rectcenter['y'])
		
		if dx > (mouse.r+w) or dy > (mouse.r+h) : return False
		
		circledistance = {'x':abs(mouse.x-self.x-w), 'y':abs(mouse.y-self.y-h)}
		
		if circledistance['x'] <= w : return True
		if circledistance['y'] <= h : return True
		
		cornerdistance = ((circledistance['x']-w)**2) + ((circledistance['y']-h)**2)
		
		return cornerdistance <= mouse.r**2

start()
