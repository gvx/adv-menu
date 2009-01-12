#ADV-MENU 0.0
#(C) 2008 Robin Wellner
#
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#Released under GPL (see http://www.gnu.org/licenses/)

import pygame
from pygame.locals import *
import os
from sys import platform as sys_platform
if sys_platform[:3] == 'win':
    os.environ['SDL_VIDEO_CENTERED'] = '1'
from math import *

from time import sleep, time
class ABClock:
    def __init__(self):
        self.t = time()
    def tick(self, rate=-1):
        self.rate = rate
        self._stop()
        retVal = int(round((time() - self.t) * 1000, 0))
        self.t = time()
        return retVal
    def _stop(self):
        try:
            sleep_time = 1.0/self.rate - (time() - self.t)
            if sleep_time > 0:
               sleep(sleep_time)
        except IOError:
            pass

def menu(Surface, Items, Xoffset, Yoffset, itemheight, totalheight, boxwidth, Font):
    Clock = ABClock()
    focus = 0
    while True:
        Clock.tick(10)
        keystate = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                return 'exit'
            elif event.type == MOUSEBUTTONDOWN:
                if event.button==1:
                    if Xoffset < event.pos[0] < Xoffset+boxwidth and Yoffset < event.pos[1] < totalheight*len(Items):
                        clicked_item = (event.pos[1] - 20)/totalheight
                        if Items[clicked_item][2] == 'button':
                            return Items[clicked_item][1]
            elif event.type == MOUSEMOTION:
                if Xoffset < event.pos[0] < Xoffset+boxwidth and Yoffset < event.pos[1] < totalheight*len(Items):
                    focus = (event.pos[1] - Yoffset)/totalheight
            elif event.type == KEYDOWN:
                if event.key in (K_DOWN, K_RIGHT):
                    focus = (focus + 1) % len(Items)
                elif event.key in (K_UP, K_LEFT):
                    focus = (focus - 1) % len(Items)
                elif event.key in (K_RETURN, K_SPACE):
                    if Items[focus][2] == 'button':
                        return Items[focus][1]
                else:
                    pass
        Surface.fill((0,0,0))
        for n in range(len(Items)):
            draw_item = Items[n][0]
            draw_type = Items[n][2]
            if focus == n:
                if draw_type == 'button':
                    pygame.draw.rect(Surface, (255, 255, 255), (Xoffset, Yoffset + n*totalheight, boxwidth, itemheight))
                    Surface.blit(Font.render(draw_item, True, (0, 0, 0)),
                                 (Xoffset+15, Yoffset+ 5 + n*totalheight))
                elif draw_type == 'disabled':
                    pygame.draw.rect(Surface, (155, 155, 155), (Xoffset, Yoffset + n*totalheight, boxwidth, itemheight))
                    Surface.blit(Font.render(draw_item, True, (0, 0, 0)),
                                 (Xoffset+15, Yoffset+ 5 + n*totalheight))
                elif draw_type == 'slider':
                    pygame.draw.rect(Surface, (255, 255, 255), (Xoffset+boxwidth/2, Yoffset + n*totalheight, boxwidth/2, itemheight))
                    Surface.blit(Font.render(draw_item, True, (255, 255, 255)),
                                 (Xoffset+15, Yoffset+ 5 + n*totalheight))
            else:
                if draw_type == 'button':
                    pygame.draw.rect(Surface, (255, 255, 255), (Xoffset, Yoffset + n*totalheight, boxwidth, itemheight), 1)
                    Surface.blit(Font.render(draw_item, True, (255, 255, 255)),
                                 (Xoffset+15, Yoffset+ 5 + n*totalheight))
                elif draw_type == 'disabled':
                    pygame.draw.rect(Surface, (155, 155, 155), (Xoffset, Yoffset + n*totalheight, boxwidth, itemheight), 1)
                    Surface.blit(Font.render(draw_item, True, (155, 155, 155)),
                                 (Xoffset+15, Yoffset+ 5 + n*totalheight))
                elif draw_type == 'slider':
                    pygame.draw.rect(Surface, (255, 255, 255), (Xoffset+boxwidth/2, Yoffset + n*totalheight, boxwidth/2, itemheight), 1)
                    Surface.blit(Font.render(draw_item, True, (255, 255, 255)),
                                 (Xoffset+15, Yoffset+ 5 + n*totalheight))
        pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("ADV-MENU Test")
    icon = pygame.Surface((1,1)); icon.set_alpha(0); pygame.display.set_icon(icon)
    Surface = pygame.display.set_mode((640,480))#, SCR_FULL and FULLSCREEN)
    Font = pygame.font.Font("mksanstallx.ttf",14)
    Items = [('Abc', 'abc', 'button'),
             ('Do something', 'x', 'slider'),
             ('Test', 'name', 'disabled'),
             ('Quit', 'exit', 'button'),
            ]
    menu(Surface, Items, 30, 30, 30, 50, 200, Font)
    pygame.quit()
