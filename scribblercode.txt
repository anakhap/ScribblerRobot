def main():
	a=1
	while(a!=0):
		command = input("What way do you want to go?")
		if(command ==1):
			turnBy(90, "deg")
			wait(2)
			while(getObstacle(1)<1100):
				try:
					forward(1,1)
				except KeyboardInterrupt:
					stop()
					break
			if(getObstacle(1)>1000):
				for i in range (0,3):
					turnBy(90, "deg")
					wait(2)
					if(getObstacle(1)<100):
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
		elif(command ==5):
			while(getObstacle(1)<1100):
				try:
					forward(1,1)
				except KeyboardInterrupt:
					stop()
					break
			if(getObstacle(1)>1000):
				for i in range (0,3):
					turnBy(90, "deg")
					wait(2)
					if(getObstacle(1)<100):
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
					
		elif(command ==3):
			turnBy(-90, "deg")
			wait(2)
			while(getObstacle(1)<1100):
				try:
					forward(1,1)
				except KeyboardInterrupt:
					stop()
					break
			if(getObstacle(1)>1000):
				for i in range (0,3):
					turnBy(90, "deg")
					wait(2)
					if(getObstacle(1)<100):
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
		elif(command ==2):
			backward(1,1)
			wait(2)
			turnBy(180, "deg")
			wait(4)
			while(getObstacle(1)<1100):
				try:
					forward(1,1)
				except KeyboardInterrupt:
					stop()
					break
			if(getObstacle(1)>1000):
				for i in range (0,3):
					turnBy(90, "deg")
					wait(2)
					if(getObstacle(1)<100):
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
		else:
			speak("That is not part of the controls, you are ending your trip")
			break