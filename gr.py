import pygame
import sys
from screeninfo import get_monitors
from color_generator import *
import random
from math import sqrt, cos, atan
from itertools import chain, combinations
from vector import Vector

clock = pygame.time.Clock()
pygame.init()
monitors = get_monitors()
while monitors == []: # так надо, не трогать
	monitors = get_monitors()

Width = 1400#monitors[0].width
Height = 1400#monitors[0].height // 1.1
center = Vector([Width//2, Height//2])
scale = 1
body_radius = 5
G = 6

surface = pygame.display.set_mode((Width, Height))

class Body:
	def __init__(self, color, pos, v):
		self.color = color
		self.pos = pos
		self.v = v
		self.r = body_radius
		self.m = 3.14 * self.r**2
		self.F = Vector()
		self.track_points = []
	def draw(self):
		self.v += self.F / self.m
		self.pos += self.v
		self.F.set([0,0])
		pos = ((self.pos * scale).round() + center).coords()
		r = round(self.r * scale)
		r = 1 if r<1 else r
		pygame.draw.circle(surface, self.color, pos, r)
		self.track_points.append(pos)
		if len(self.track_points)/2 >= 60:
			self.track_points.pop(0)
		i = 0
		if len(self.track_points) >= 4:
			while i+1 < len(self.track_points):
				start = self.track_points[i]
				end = self.track_points[i+1]
				pygame.draw.aaline(surface, self.color, start, end, True)
				i += 2

bodies = []
colors = genColors(1000, length=10)

def _quit():
	pygame.quit()
	sys.exit()

def events():
	global scale
	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN:
			global pos1
			pos1 = Vector(event.pos)
		elif event.type == pygame.MOUSEBUTTONUP:
			pos2 = Vector(event.pos)
			index = len(bodies)
			v = (pos1-pos2) / 20
			pos = (pos1 - center) / scale
			bodies.append(Body(colors[index], pos, v))
		elif event.type == pygame.QUIT:
			_quit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				scale /= 1.1
			elif event.key == pygame.K_DOWN:
				scale *= 1.1

def F(b1, b2):
	r2 = (b2.pos - b1.pos).r2()
	return G * b1.m*b2.m / r2

def gravity():
	merge_pair = ()
	for idx, body1 in enumerate(bodies):
		for body2 in bodies[idx + 1:]:
			ds = body2.pos - body1.pos
			R2 = ds.r2()
			if sqrt(R2) >= body1.r + body2.r:
				F = ds.normalize()
				F *= G * body1.m*body2.m / R2
				body1.F += F
				body2.F -= F
			else:
				merge_pair = (body1, body2)
	return merge_pair

def merge(merge_pair):
	b1, b2 = merge_pair
	m = b1.m + b2.m
	v = (b1.v*b1.m + b2.v*b2.m) / m
	b1.m, b1.v = m, v
	b1.r = sqrt(b1.m / 3.14)
	bodies.remove(b2)
	
while True:
	surface.fill((20,40,80))
	events()
	merge_pair = gravity()
	if len(merge_pair) == 2:
		merge(merge_pair)
	for body in bodies:
		E = body.m * body.v.length()**2 / 2
		F = body.F.length()
		body.draw()
	

	clock.tick(60)
	pygame.display.set_caption(str(clock)+"  bodies:"+str(len(bodies))+"  scale:"+str(scale))
	pygame.display.update()
	pygame.display.flip()