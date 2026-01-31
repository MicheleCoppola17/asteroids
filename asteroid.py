import pygame
from circleshape import CircleShape
from constants import *
from logger import *
import random

class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)
	
	def draw(self, screen):
		pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

	def split(self):
		pygame.sprite.Sprite.kill(self)
		if self.radius <= ASTEROID_MIN_RADIUS:
			return
		
		log_event("asteroid_split")
		random_angle = random.uniform(20, 50)
		new_asteroid_movement1 = pygame.math.Vector2.rotate(self.velocity, random_angle)
		new_asteroid_movement2 = pygame.math.Vector2.rotate(self.velocity, -random_angle)
		new_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
		asteroid1 = Asteroid(self.position[0], self.position[1], new_asteroid_radius)
		asteroid1.velocity = new_asteroid_movement1 * 1.2
		asteroid2 = Asteroid(self.position[0], self.position[1], new_asteroid_radius)
		asteroid2.velocity = new_asteroid_movement2 * 1.2
		

	def update(self, dt):
		self.position += self.velocity * dt
