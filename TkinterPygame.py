Tkinter
=======
# respond to a key without the need to press enter
import Tkinter as tk
def keypress(event):
    if event.keysym == 'Escape':
        root.destroy()
    x = event.char
    if x == "w":
        print "blaw blaw blaw"
    elif x == "a":
        print "blaha blaha blaha"
    elif x == "s":
        print "blash blash blash"
    elif x == "d":
        print "blad blad blad"
    else:
        print x


root = tk.Tk()
print "Press a key (Escape key to exit):"
root.bind_all('<Key>', keypress)
# don't show the tk window
root.withdraw()
root.mainloop()

Pygame
=======
# The necessities to input pygame (MIGHT BE MORE/LESS NOT SURE)

import pygame, sys
from pygame.locals import *
pygame.init()

# Main part; Note 'events' can be keypresses or mouse clicks

while True:
for event in pygame.event.get() :
  if event.type == pygame.KEYDOWN :
    	if event.key == pygame.K_SPACE :
      		print "Space bar pressed down."
   	 elif event.key == pygame.K_ESCAPE :
      		print "Escape key pressed down."
  elif event.type == pygame.KEYUP :
    		if event.key == pygame.K_SPACE :
      			print "Space bar released."
    		elif event.key == pygame.K_ESCAPE :
     			 pygame.quit()
     			 sys.exit()