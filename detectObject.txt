def try201():
	a=0
	b=0
	c=0
	while getObstacle(1)<1100:
		forward(0.5,1)
	turnBy(-90,"deg")
	wait(2)
	while a<2:
		c=0
		forward(1,1)
		if a==0:
			b+=1
		wait(2)
		turnBy(90,"deg")
		wait(2)
		while c<5:
			if getObstacle(1)<50:
				c=0
				break
			else:
				c+=1
			
		
		if c==0:
			a+=1
		else:
			if getObstacle(1)>1111:
				backward(1,0.5)
			turnBy(-90,"deg")
			wait(2)
	for x in range (0,b):
		forward(1,1)
	wait(2)
	turnBy(-90,"deg")
	wait(2)
	forward(1,1)