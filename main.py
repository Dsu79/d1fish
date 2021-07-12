import pygame as pg

pg.init()
# init starts pygame but in this instance known as pg
print(pg.display.Info())
# "print(pg.display.Info())" this yonks the information about display from the libary pygame (pg)
# making something modular makes it easier to rtead/comprehend
#class defines an objects and decides that attrubutes the object may/can have
# self. allows access attrubutes, methods and stuff in classes
# __init__ , used for making classes
# "A constructor enables you to provide any custom initialization that must be done before any other methods can be called on an instantiated object." (Javascript)
screen_info = pg.display.Info()
print(screen_info.current_w, screen_info.current_h)
size = screen_info.current_w, screen_info.current_h
fish_image =  pg.image.load('download.html')
print(size)
screen = pg.display.set_mode(size)
clock = pg.time.Clock()
def main():
  while True:
    clock.tick(60)
    screen.fill((0,0,0))
    pg.display.flip()
    screen.blit(fish_image, fish_rect)
if __name__ == "__main__":
  main()
main()
