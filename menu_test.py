#ADV-MENU TEST 1.1
#(C) 2008 Robin Wellner
#
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#Released under GPL (see http://www.gnu.org/licenses/)

from menu import menu, pygame
pygame.init()
pygame.display.set_caption("ADV-MENU Test")
icon = pygame.Surface((1,1)); icon.set_alpha(0); pygame.display.set_icon(icon)
Surface = pygame.display.set_mode((640,480))

Font = pygame.font.Font("mksanstallx.ttf",14)

Items = [('Abc', 'abc', 'button'),
         ('Do something', 'x', 'slider', (2, 0, 10)),
         ('Done', 'p', 'checkbox', True),
         ('Test', 'name', 'disabled'),
         ('Cancel', 'cancel', 'cancelbutton'),
         ('Quit', 'exit', 'button'),
         ('Useless button 1', 'btn', 'button'),
         ('Useless button 2', 'btn', 'button'),
         ('Useless button 3', 'btn', 'button'),
         ('Useless button 4', 'btn', 'button'),
         ('Useless button 5', 'btn', 'button'),
         ('Useless button 6', 'btn', 'button'),
         ('Useless button 7', 'btn', 'button'),
         ('Useless button 8', 'btn', 'button'),
        ]
result = menu(Surface, Items, 30, 200, 30, 30, 50, 300, Font)

if result[0] in ('cancel', 'exit'):
    print "User quitted"
elif result[0] == 'abc':
    print "User chose Abc"
elif result[0] == 'name':
    print "User chose Test"
print "Slider index:",
print result[1]['x'].index
print "Checkbox checked:",
print result[1]['p'].checked
pygame.quit()
