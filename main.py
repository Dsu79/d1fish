import pygame as pg

pg.init()
p = print
# init starts pygame but in this instance known as pg
p(pg.display.Info())
# "print(pg.display.Info())" this yonks the information about display from the libary pygame (pg)
# making something modular makes it easier to rtead/comprehend
#class defines an objects and decides that attrubutes the object may/can have
# self. allows access attrubutes, methods and stuff in classes
# __init__ , used for making classes
# "A constructor enables you to provide any custom initialization that must be done before any other methods can be called on an instantiated object." (Javascript)
screen_info = pg.display.Info()
p(screen_info.current_w, screen_info.current_h)
size = (width,height) =  screen_info.current_w, screen_info.current_h
#You could also do
#size = (width,height)
#width = screen_info,current_w
#length = screen_info,current_l
fish_image =  pg.image.load('fish.jpeg')
p(size)
screen = pg.display.set_mode(size)
clock = pg.time.Clock()
fish_image = pg.transform.smoothscale(fish_image , (80,80) )
fish_rect = fish_image.get_rect
fish_rect = ( width // 2, height // 2 )

def main():
  while True:
    clock.tick(60)
    screen.fill((0,0,0))
    screen.blit(fish_image, fish_rect)
    pg.display.flip()

if __name__ == "__main__":
  main()
#  checks if the language used it python and if so main() can be run
main()
