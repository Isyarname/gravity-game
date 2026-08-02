from math import sin, cos, pi

def maximizeBrightness(rgb):
	k = 255 - max(rgb)
	r = rgb[0] + k
	g = rgb[1] + k
	b = rgb[2] + k
	return (r,g,b)

def redcos(x):
	if 0 <= x <= pi/2:
		return cos(x)
	elif pi/2 <= x <= pi:
		return 0
	elif pi <= x <= 3*pi/2:
		return cos(x + pi/2)

def poss(x):
	if x > 0:
		return x
	else:
		return 0

def genColor1(i, maxNumber, minNumber=0, bright=True):
	n = (maxNumber-minNumber)//1.75
	arg = pi*i/n
	r = poss(cos(arg))
	g = poss(sin(arg))
	b = poss(cos(pi-arg))
	color = [round((255*x)%256) for x in (r,g,b)]
	if bright:
		color = maximizeBrightness(color)
	return color

def genColor2(i, maxNumber, minNumber=0, bright=True):
	n = (maxNumber-minNumber)//1.25
	per = 3*pi/2
	arg = pi*i/n
	r = redcos(arg%per)
	g = redcos((arg-pi/2)%per)
	b = redcos((arg-pi)%per)
	color = [round(255*x) for x in (r,g,b)]
	if bright:
		color = maximizeBrightness(color)
	return color

def genColors1(maxNumber, minNumber=0, length=0):
	if length == 0:
		length = (maxNumber-minNumber)
	length = length*4/7
	colors = []
	for i in range(0, maxNumber-minNumber+1):
		arg = pi*i/length
		r = poss(cos(arg))
		g = poss(sin(arg))
		b = poss(cos(pi-arg))
		colors.append([round((255*x)%256) for x in (r,g,b)])
	return colors

def genColors2(maxNumber, minNumber=0, length=0):
	if length == 0:
		length = (maxNumber-minNumber)
	length = length*4/5
	per = 3*pi/2
	colors = []
	for i in range(0, maxNumber-minNumber+1):
		arg = pi*i/length
		r = redcos(arg%per)
		g = redcos((arg-pi/2)%per)
		b = redcos((arg-pi)%per)
		colors.append([round(255*x) for x in (r,g,b)])
	return colors

def genColors(maxNumber, minNumber=0, length=0, bright=True, type_=2):
	if type_ == 1:
		colors = genColors1(maxNumber, minNumber, length)
	elif type_ == 2:
		colors = genColors2(maxNumber, minNumber, length)
	if bright:
		colors = [maximizeBrightness(c) for c in colors]
	cd = {}
	for i, e in enumerate(range(minNumber, maxNumber+1)):
		cd[e] = colors[i]
	return cd