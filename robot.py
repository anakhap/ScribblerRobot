import pygame
import sys
from pygame.locals import *
pygame.init()
from myro import *
init()

def spacecheck():
    #checks possible turning spots
    for i in range (0,3):
        turnBy(90, "deg")
	wait(2)
	if(checkobject()==0):
	    if(i==0):
                speak("YES turn left")
	    elif(i==1):
		speak("YES turn around")
	    elif(i==2):
		speak("YES turn right")
	else:
	    if(i==0):
		speak("NO turn left")
	    elif(i==1):
		speak("NO turn around")
	    elif(i==2):
		speak("NO turn right")
    turnBy(90, "deg")
    main()


def direction():
    #changes robot direction
    keys = pygame.key.get_pressed()
    if keys[K_PAGEUP]:
        speak("You are exiting the program, Goodbye")
        sys.exit()
    if keys[K_LEFT]:
        speak("Turning left")
        wait(2)
        turnBy(90, "deg")
        wait(4)
        start()
    if keys[K_RIGHT]:
        speak("Turning right")
        wait(2)
        turnBy(-90, "deg")
        wait(4)
        start()
    if keys[K_DOWN]:
        speak("Turning around")
        wait(2)
        turnBy(180, "deg")
        wait(4)
        start()
    if keys[K_UP]:
        speak("Going forward")
        start()
    if keys[K_PAGEDOWN]: 
        stop()
        main()
    
def verifyobject():
    k=1
    for b in range(0,25):
        if getObstacle(1)==0:
            k=0
    if k==0:
        #there is no object
        speak("Nevermind, I will keep going forward")
        start()
    else:
        #there really is an object
        speak("Yes, there is an object, let me tell you which ways are safe to turn")
        spacecheck()

def checkobject():
    #return 1 if there is, 0 if there isn't
    a=1
    for b in range(0,25):
        if getObstacle(1)==0:
            a=0
    return a

def start():
    a=0
    while 1:
        while checkobject()==0:
            a=0
            forward(1)
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    a=1
                    break
            if a==1: break
            if checkobject()==1:break
        if a==1:       
            speak("STOP")
            stop()
            direction()
        else:
            stop()
            speak("STOP, I think there is an obstacle in the way, let me verify")
            verifyobject()
    


def main():
    size = width, height = 600, 400
    screen = pygame.display
    screen = pygame.display.set_mode(size)

    speak("Press an arrow key to start me!")
    while 1:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                direction()
                start()
                    
    
            

        
