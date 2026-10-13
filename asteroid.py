import pygame
from circleshape import *
from constants import LINE_WIDTH
from constants import ASTEROID_MIN_RADIUS
from logger import log_event
import random

class Asteroid(CircleShape):
  def __init__(self, x: float, y: float, radius: float) -> None:
    super().__init__(x, y, radius)

  def draw(self, screen: pygame.Surface) -> None:
    pygame.draw.circle(
      screen,
      "white",
      self.position,
      self.radius,
      LINE_WIDTH
    )

  def update(self, dt: float) -> None:
    self.position += (self.velocity * dt)

  def split(self) -> None:
    self.kill()

    if(self.radius <= ASTEROID_MIN_RADIUS):
      return
    else:
      log_event("asteroid_split")

      random_angle = random.uniform(20,50)

      spawn_vector_one = self.velocity.rotate(random_angle)
      spanw_vector_two = self.velocity.rotate(-random_angle)

      spawn_radius = self.radius - ASTEROID_MIN_RADIUS

      spawn_asteroid_one = Asteroid(self.position.x, self.position.y, spawn_radius)
      spawn_asteroid_two = Asteroid(self.position.x, self.position.y, spawn_radius)

      spawn_asteroid_one.velocity = spawn_vector_one * 1.2
      spawn_asteroid_two.velocity = spanw_vector_two * 1.2 
      
