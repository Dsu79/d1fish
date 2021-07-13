import pygame as pg
import random as rd
import sys as ss
from pygame.locals import *
pg.init()
p = print
p(pg.display.Info())
screen_info = pg.display.Info()
size = (width,height) =  screen_info.current_w, screen_info.current_h
screen = pg.display.set_mode(size)
clock = pg.time.Clock()
fish_image =  pg.image.load('fish.png')
fish_image = pg.transform.smoothscale(fish_image , (120,120))
fish_rect = fish_image.get_rect()
fish_rect.center = ( width // 2, height // 2 )

speed = pg.math.Vector2(0,10)
rotation = rd.randint (0, 360 )
speed.rotate_ip(rotation)
fish_image =  pg.transform.rotate(fish_image, 180 - rotation )

def move_fish() :
  global fish_image
  current_info = pg.display.Info()
  fish_rect.move_ip(speed)
  if fish_rect.left < 0 or fish_rect.right > current_info.current_w :
    speed[0] *= -1
    fish_image = pg.transform.flip (fish_image, True, False)
    fish_rect.move_ip(speed[0],0)
  if  fish_rect.top < 0 or fish_rect.bottom > current_info.current_h:
    speed[1] *= -1
    fish_image = pg.transform.flip (fish_image, False, True)
    fish_rect.move_ip(0,speed[1])
     
  
def main():
  while True:
    clock.tick(60)
    move_fish()
    for event in pg.event.get():
      if event.type == QUIT:
        ss.exit(0)
    screen.fill((11,176,240))
    screen.blit(fish_image, fish_rect)
    pg.display.flip()
if __name__ == "__main__":
  main()


