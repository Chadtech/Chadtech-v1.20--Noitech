# -------------------------- Pixel Reading

def whatTone(topColON,topColTW,botColON,botColTW):
	cols = [topColON,topColTW,botColON,botColTW]
	print cols
	for yit in range(len(cols)):
		if cols[yit]==(255,255,255):
			cols[yit]=1
		if cols[yit]==(255,0,0):
			cols[yit]=3
		if cols[yit]==(0,0,255):
			cols[yit]=5
		if cols[yit]==(255,128,128):
			cols[yit]=6
		if cols[yit]==(0,255,0):
			cols[yit]=7
		if cols[yit]==(128,0,0):
			cols[yit]=9
	frac = 0
	frac = (cols[0]*cols[1])/(cols[2]*cols[3])
	print frac, 'COLS', cols
	while frac < 1:
		frac = frac*2
	frac = frac*25.
	return frac

def readPix(score):
	score=Image.open(score)
	xCou = 0
	xi,yi = score.size
	xv,yv = 16,60
	voiHeight = 200
	voiNum = yi/voiHeight #200 is the height of my 'jusBars' image (an image of just four bars)
	print voiNum
	voiss = []
	voiBarMarg = 50
	thisSong=makeSong((xi-voiBarMarg)/144)
	for nink in range(voiNum):
		thisHarmProf = []
		rOct,gOct,bOct = score.getpixel((1,(126+(voiHeight*nink))))
		whichOct = 2**bOct
		if score.getpixel((xv,yv+(voiHeight*nink)))==(0,255,0):
			for rkk in range(5):
				harmNoom, bigVol, smallVol = score.getpixel(2+(3*rkk),60+(nink*voiHeight))
				harmDeen, volSlop, doesExist = score.getpixel(2+(3*rkk),63+(nink*voiHeight))
				if doesExist>0:
					thisHarmProf.append((float(harmNoom/harmDeen),((bigVol*256)+smallVol),float(800+volSlop)))
		for vapp in range(5): # The number of 'spaces' in the upper octave of a bar
			theFreq = 100.
			yitCou=0
			for yit in range(xi-voiBarMarg):
				if yitCou==0:
					if score.getpixel((yit+voiBarMarg,53+(vapp*10)+(nink*voiHeight)))!=(0,0,0) and score.getpixel((yit+voiBarMarg,53+(vapp*10)+(nink*voiHeight)))!=(64,64,64):
						print 'happen'
						print 'YIT', yit, 'VAPP', vapp, 'NINK', nink
						theFreq=whichOct*2*(whatTone(score.getpixel((yit+voiBarMarg,53+(vapp*10)+(nink*voiHeight))),score.getpixel((yit+voiBarMarg,53+1+(vapp*10)+(nink*voiHeight))),score.getpixel((yit+voiBarMarg,53+2+(vapp*10)+(nink*voiHeight))),score.getpixel((yit+voiBarMarg,53+3+(vapp*10)+(nink*voiHeight)))))
						while score.getpixel((yit+voiBarMarg+yitCou,53+(vapp*10)+(nink*voiHeight)))!=(0,0,0) and score.getpixel((yit+voiBarMarg+yitCou,53+(vapp*10+(nink*voiHeight))))!=(64,64,64):
							yitCou+=1
						if score.getpixel((xv,yv+(nink*voiHeight)))!=(0,0,0):
							if score.getpixel((xv,yv+(nink*voiHeight)))==(255,0,0):
								putd = makeTone(theFreq,yitCou/144.)
							if score.getpixel((xv,yv+(nink*voiHeight)))==(0,255,0):
								putd = harmize(theFreq,thisHarmProf,yitCou/144.)
						for qzy in range(10):
							if score.getpixel((xv,yv+6+(6*qzy)+(nink*voiHeight)))!=(0,0,0):
								if score.getpixel((xv,yv+6+(6*qzy)+(nink*voiHeight)))==(255,0,0):
									howMany,whocares,thisvariabledoesntmatter = score.getpixel(2,60+(6*qzy)+(nink*voiHeight))
									spaceSize,stilldoesntmatter,thisvariablewontbeused = score.getpixel(2,63+(6*qzy)+(nink*voiHeight))
									putd = creatMany(putd,howMany,spaceSize)
								if score.getpixel((xv,yv+6+(6*qzy)+(nink*voiHeight)))==(0,255,0):
									howDivs,whocares,thisvariabledoesntmatter = score.getpixel(2,60+(6*qzy)+(nink*voiHeight))
									putd = bitReduc(putd,howDivs)
								if score.getpixel((xv,yv+6+(6*qzy)+(nink*voiHeight)))==(0,0,255):
									howCutOff,whocares,thisvariabledoesntmatter = score.getpixel(2,60+(6*qzy)+(nink*voiHeight))
									putd = cutOff(putd,howCutOff)
						print yit/144., len(putd)/144., len(thisSong)/144., theFreq, yitCou
						buildSong(yit/144.,putd,thisSong,250.)
				else:
					yitCou-=1
		for vapp in range(5): # The number of 'lines' in the upper octave of a bar
			theFreq = 100.
			yitCou=0
			for yit in range(xi-voiBarMarg):
				if yitCou==0:
					if score.getpixel((yit+voiBarMarg,57+(vapp*10)+(nink*voiHeight)))!=(0,0,0) and score.getpixel((yit+voiBarMarg,57+(vapp*10)+(nink*voiHeight)))!=(64,64,64):
						print 'happen'
						print 'YIT', yit, 'VAPP', vapp, 'NINK', nink
						theFreq=whichOct*2*(whatTone(score.getpixel((yit+voiBarMarg,57+(vapp*10)+(nink*voiHeight))),score.getpixel((yit+voiBarMarg,57+1+(vapp*10)+(nink*voiHeight))),score.getpixel((yit+voiBarMarg,57+4+(vapp*10)+(nink*voiHeight))),score.getpixel((yit+voiBarMarg,57+5+(vapp*10)+(nink*voiHeight)))))
						while score.getpixel((yit+voiBarMarg+yitCou,57+(vapp*10)+(nink*voiHeight)))!=(0,0,0) and score.getpixel((yit+voiBarMarg+yitCou,57+(vapp*10)+(nink*voiHeight)))!=(64,64,64):
							yitCou+=1
						if score.getpixel((xv,yv+(nink*voiHeight)))!=(0,0,0):
							if score.getpixel((xv,yv+(nink*voiHeight)))==(255,0,0):
								putd = makeTone(theFreq,yitCou/144.)
							if score.getpixel((xv,yv+(nink*voiHeight)))==(0,255,0):
								putd = harmize(theFreq,thisHarmProf,yitCou/144.)
						for qzy in range(10):
							if score.getpixel((xv,yv+6+(6*qzy)+(nink*voiHeight)))!=(0,0,0):
								if score.getpixel((xv,yv+6+(6*qzy)+(nink*voiHeight)))==(255,0,0):
									howMany,whocares,thisvariabledoesntmatter = score.getpixel(2,60+(6*qzy)+(nink*voiHeight))
									spaceSize,stilldoesntmatter,thisvariablewontbeused = score.getpixel(2,63+(6*qzy)+(nink*voiHeight))
									putd = creatMany(putd,howMany,spaceSize)
								if score.getpixel((xv,yv+6+(6*qzy)+(nink*voiHeight)))==(0,255,0):
									howDivs,whocares,thisvariabledoesntmatter = score.getpixel(2,60+(6*qzy)+(nink*voiHeight))
									putd = bitReduc(putd,howDivs)
								if score.getpixel((xv,yv+6+(6*qzy)+(nink*voiHeight)))==(0,0,255):
									howCutOff,whocares,thisvariabledoesntmatter = score.getpixel(2,60+(6*qzy)+(nink*voiHeight))
									putd = cutOff(putd,howCutOff)
						print yit/144., len(putd)/144., len(thisSong)/144., theFreq, yitCou
						buildSong(yit/144.,putd,thisSong,250.)
				else:
					yitCou-=1
		for vapp in range(5): # The number of 'spaces' in the lower octave of a bar
			theFreq = 100.
			yitCou=0
			for yit in range(xi-voiBarMarg):
				if yitCou==0:
					if score.getpixel((yit+voiBarMarg,103+(vapp*10)+(nink*voiHeight)))!=(0,0,0) and score.getpixel((yit+voiBarMarg,103+(vapp*10)+(nink*voiHeight)))!=(64,64,64):
						print 'happen'
						print 'YIT', yit, 'VAPP', vapp, 'NINK', nink
						theFreq=whichOct*(whatTone(score.getpixel((yit+voiBarMarg,103+(vapp*10)+(nink*voiHeight))),score.getpixel((yit+voiBarMarg,103+1+(vapp*10)+(nink*voiHeight))),score.getpixel((yit+voiBarMarg,103+2+(vapp*10)+(nink*voiHeight))),score.getpixel((yit+voiBarMarg,103+3+(vapp*10)+(nink*voiHeight)))))
						while score.getpixel((yit+voiBarMarg+yitCou,103+(vapp*10)+(nink*voiHeight)))!=(0,0,0) and score.getpixel((yit+voiBarMarg+yitCou,103+(vapp*10)+(nink*voiHeight)))!=(64,64,64):
							yitCou+=1
						if score.getpixel((xv,yv+(nink*voiHeight)))!=(0,0,0):
							if score.getpixel((xv,yv+(nink*voiHeight)))==(255,0,0):
								putd = makeTone(theFreq,yitCou/144.)
							if score.getpixel((xv,yv+(nink*voiHeight)))==(0,255,0):
								putd = harmize(theFreq,thisHarmProf,yitCou/144.)
						for qzy in range(10):
							if score.getpixel((xv,yv+6+(6*qzy)+(nink*voiHeight)))!=(0,0,0):
								if score.getpixel((xv,yv+6+(6*qzy)+(nink*voiHeight)))==(255,0,0):
									howMany,whocares,thisvariabledoesntmatter = score.getpixel(2,60+(6*qzy)+(nink*voiHeight))
									spaceSize,stilldoesntmatter,thisvariablewontbeused = score.getpixel(2,63+(6*qzy)+(nink*voiHeight))
									putd = creatMany(putd,howMany,spaceSize)
								if score.getpixel((xv,yv+6+(6*qzy)+(nink*voiHeight)))==(0,255,0):
									howDivs,whocares,thisvariabledoesntmatter = score.getpixel(2,60+(6*qzy)+(nink*voiHeight))
									putd = bitReduc(putd,howDivs)
								if score.getpixel((xv,yv+6+(6*qzy)+(nink*voiHeight)))==(0,0,255):
									howCutOff,whocares,thisvariabledoesntmatter = score.getpixel(2,60+(6*qzy)+(nink*voiHeight))
									putd = cutOff(putd,howCutOff)
						print yit/144., len(putd)/144., len(thisSong)/144., theFreq, yitCou
						buildSong(yit/144.,putd,thisSong,250.)
				else:
					yitCou-=1
		for vapp in range(5): # The number of 'line' in the lower octave of a bar
			theFreq = 100.
			yitCou=0
			for yit in range(xi-voiBarMarg):
				if yitCou==0:
					if score.getpixel((yit+voiBarMarg,107+(vapp*10)+(nink*voiHeight)))!=(0,0,0) and score.getpixel((yit+voiBarMarg,107+(vapp*10)+(nink*voiHeight)))!=(64,64,64):
						print 'happen'
						print 'YIT', yit, 'VAPP', vapp, 'NINK', nink
						theFreq=whichOct*(whatTone(score.getpixel((yit+voiBarMarg,107+(vapp*10)+(nink*voiHeight))),score.getpixel((yit+voiBarMarg,107+1+(vapp*10)+(nink*voiHeight))),score.getpixel((yit+voiBarMarg,107+4+(vapp*10)+(nink*voiHeight))),score.getpixel((yit+voiBarMarg,107+5+(vapp*10)+(nink*voiHeight)))))
						while score.getpixel((yit+voiBarMarg+yitCou,107+(vapp*10)+(nink*voiHeight)))!=(0,0,0) and score.getpixel((yit+voiBarMarg+yitCou,107+(vapp*10)+(nink*voiHeight)))!=(64,64,64):
							yitCou+=1
						if score.getpixel((xv,yv+(nink*voiHeight)))!=(0,0,0):
							if score.getpixel((xv,yv+(nink*voiHeight)))==(255,0,0):
								putd = makeTone(theFreq,yitCou/144.)
							if score.getpixel((xv,yv+(nink*voiHeight)))==(0,255,0):
								putd = harmize(theFreq,thisHarmProf,yitCou/144.)
						for qzy in range(10):
							if score.getpixel((xv,yv+6+(6*qzy)+(nink*voiHeight)))!=(0,0,0):
								if score.getpixel((xv,yv+6+(6*qzy)+(nink*voiHeight)))==(255,0,0):
									howMany,whocares,thisvariabledoesntmatter = score.getpixel(2,60+(6*qzy)+(nink*voiHeight))
									spaceSize,stilldoesntmatter,thisvariablewontbeused = score.getpixel(2,63+(6*qzy)+(nink*voiHeight))
									putd = creatMany(putd,howMany,spaceSize)
								if score.getpixel((xv,yv+6+(6*qzy)+(nink*voiHeight)))==(0,255,0):
									howDivs,whocares,thisvariabledoesntmatter = score.getpixel(2,60+(6*qzy)+(nink*voiHeight))
									putd = bitReduc(putd,howDivs)
								if score.getpixel((xv,yv+6+(6*qzy)+(nink*voiHeight)))==(0,0,255):
									howCutOff,whocares,thisvariabledoesntmatter = score.getpixel(2,60+(6*qzy)+(nink*voiHeight))
									putd = cutOff(putd,howCutOff)
						print yit/144., len(putd)/144., len(thisSong)/144., theFreq, yitCou
						buildSong(yit/144.,putd,thisSong,250.)
				else:
					yitCou-=1
	buildFile(thisSong)

def onthre(durRay,source,ear,room,loss,howMuchNoise,aftaNoise,allpass): #How durRay sounds, when it bounces off each wall once, in a given room
	inRay = durRay
	outRay = []
	xs,ys,zs=source#Location of sound source
	xe,ye,ze=ear#Location of ear
	xr,yr,zr=room#Size of room
	dist=(((xe-xs)**2)+((ye-ys)**2)+((ze-zs)**2))**(0.5)

	RRx = ((dist**2)-((xs-xe)**2))**(0.5) 
	RRy = ((dist**2)-((ys-ye)**2))**(0.5)
	RRz = ((dist**2)-((zs-ze)**2))**(0.5)

	if RRx !=0:
		xOnFirsre = RRx*((xr-xs)/(xr-xe))
		xOnSecre = RRx*((xr-xe)/(xr-xs))
		xTwFirsre = RRx*(xs/xe)
		xTwSecre = RRx*(xe/xs)
	else:
		xOnFirsre = (xr)-dist
		xOnSecre = (xr)-dist
		xTwFirsre = (xr)-dist
		xTwSecre = (xr)-dist

	if RRy !=0:
		yOnFirsre = RRy*((yr-ys)/(yr-ye))
		yOnSecre = RRy*((yr-ye)/(yr-ys))
		yTwFirsre = RRy*(ys/ye)
		yTwSecre = RRy*(ye/ys)
	else:
		yOnFirsre = (yr)-dist
		yOnSecre = (yr)-dist
		yTwFirsre = (yr)-dist
		yTwSecre = (yr)-dist

	if RRz !=0:
		zOnFirsre = RRz*((zr-zs)/(zr-ze))
		zOnSecre = RRz*((zr-ye)/(zr-zs))
		zTwFirsre = RRz*(zs/ze) 
		zTwSecre = RRz*(ze/zs)
	else:
		zOnFirsre = (zr)-dist
		zOnSecre = (zr)-dist
		zTwFirsre = (zr)-dist
		zTwSecre = (zr)-dist

	xOnLag = (xOnFirsre+xOnSecre)/speedOfSound
	xTwLag = (xTwFirsre+xTwSecre)/speedOfSound
	yOnLag = (yOnFirsre+yOnSecre)/speedOfSound
	yTwLag = (yTwFirsre+yTwSecre)/speedOfSound
	zOnLag = (zOnFirsre+zOnSecre)/speedOfSound
	zTwLag = (zTwFirsre+zTwSecre)/speedOfSound

	percent = 0
	lags = [xOnLag,xTwLag,yOnLag,yTwLag,zOnLag,zTwLag]
	for yit in range(len(inRay)+int(max(lags))+1):
		outRay.append(0.)

	for gno in range(len(inRay)):
		if gno > max(lags):
			for vapp in range(10):
				outRay[gno+(int(min(lags)))+random.randint(1,10)] += random.randint(-3276,3276)*aftaNoise*inRay[gno-int(max(lags))]/10000

		outRay[gno+int(xOnLag)]+=(inRay[gno])/((1+xOnFirsre)**2)
		outRay[gno+int(xOnLag)]+=((inRay[gno])/((1+xOnSecre)**2))*(loss/1000)
		outRay[gno+int(xTwLag)]+=(inRay[gno])/((1+xTwFirsre)**2)
		outRay[gno+int(xTwLag)]+=((inRay[gno])/((1+xTwSecre)**2))*(loss/1000)

		for vapp in range(allpass):
			outRay[gno+(int(xOnLag)/(2*vapp+2))]+=((inRay[gno])/((1+xOnFirsre)**3))+(aftaNoise*(howMuchNoise/10000.)*(random.randint(-32767,32767))*(inRay[gno]))
			outRay[gno+(int(xOnLag)/(2*vapp+2))]+=(((inRay[gno])/((1+xOnSecre)**3))*(loss/1000))+(aftaNoise*(howMuchNoise/10000.)*(random.randint(-32767,32767))*(inRay[gno]))
			outRay[gno+(int(xTwLag)/(2*vapp+2))]+=((inRay[gno])/((1+xTwFirsre)**3))+(aftaNoise*(howMuchNoise/10000.)*(random.randint(-32767,32767)))
			outRay[gno+(int(xTwLag)/(2*vapp+2))]+=(((inRay[gno])/((1+xTwSecre)**3))*(loss/1000))+(aftaNoise*(howMuchNoise/10000.)*(random.randint(-32767,32767))*(inRay[gno]))
			if gno > (int(xOnLag)/(vapp+2)) and gno > (int(xTwLag)/(vapp+2)):
				outRay[gno-(int(xOnLag)/(2*vapp+2))]+=((inRay[gno])/((1+xOnFirsre)**3))+(aftaNoise*(howMuchNoise/10000.)*(random.randint(-32767,32767))*(inRay[gno]))
				outRay[gno-(int(xOnLag)/(2*vapp+2))]+=(((inRay[gno])/((1+xOnSecre)**3))*(loss/1000))+(aftaNoise*(howMuchNoise/10000.)*(random.randint(-32767,32767))*(inRay[gno]))
				outRay[gno-(int(xTwLag)/(2*vapp+2))]+=((inRay[gno])/((1+xTwFirsre)**3))+(aftaNoise*(howMuchNoise/10000.)*(random.randint(-32767,32767))*(inRay[gno]))
				outRay[gno-(int(xTwLag)/(2*vapp+2))]+=(((inRay[gno])/((1+xTwSecre)**3))*(loss/1000))+(aftaNoise*(howMuchNoise/10000.)*(random.randint(-32767,32767))*(inRay[gno]))


		outRay[gno+int(yOnLag)]+=(inRay[gno])/((1+yOnFirsre)**2)
		outRay[gno+int(yOnLag)]+=((inRay[gno])/((1+yOnSecre)**2))*(loss/1000)
		outRay[gno+int(yTwLag)]+=(inRay[gno])/((1+yTwFirsre)**2)
		outRay[gno+int(yTwLag)]+=((inRay[gno])/((1+yTwSecre)**2))*(loss/1000)

		for vapp in range(allpass):
			outRay[gno+(int(yOnLag)/(2*vapp+2))]+=((inRay[gno])/((1+yOnFirsre)**3))+(aftaNoise*(howMuchNoise/10000.)*(random.randint(-32767,32767))*(inRay[gno]))
			outRay[gno+(int(yOnLag)/(2*vapp+2))]+=(((inRay[gno])/((1+yOnSecre)**3))*(loss/2000))+(aftaNoise*(howMuchNoise/10000.)*(random.randint(-32767,32767))*(inRay[gno]))
			outRay[gno+(int(yTwLag)/(2*vapp+2))]+=((inRay[gno])/((1+yTwFirsre)**3))+(aftaNoise*(howMuchNoise/10000.)*(random.randint(-32767,32767))*(inRay[gno]))
			outRay[gno+(int(yTwLag)/(2*vapp+2))]+=(((inRay[gno])/((1+yTwSecre)**3))*(loss/2000))+(aftaNoise*(howMuchNoise/10000.)*(random.randint(-32767,32767))*(inRay[gno]))
			if gno > (int(yOnLag)/(vapp+2)) and gno > (int(yTwLag)/(vapp+2)):
				outRay[gno-(int(yOnLag)/(2*vapp+2))]+=((inRay[gno])/((1+yOnFirsre)**3))+(aftaNoise*(howMuchNoise/10000.)*(random.randint(-32767,32767))*(inRay[gno]))
				outRay[gno-(int(yOnLag)/(2*vapp+2))]+=(((inRay[gno])/((1+yOnSecre)**3))*(loss/2000))+(aftaNoise*(howMuchNoise/10000.)*(random.randint(-32767,32767))*(inRay[gno]))
				outRay[gno-(int(yTwLag)/(2*vapp+2))]+=((inRay[gno])/((1+yTwFirsre)**3))+(aftaNoise*(howMuchNoise/10000.)*(random.randint(-32767,32767))*(inRay[gno]))
				outRay[gno-(int(yTwLag)/(2*vapp+2))]+=(((inRay[gno])/((1+yTwSecre)**3))*(loss/2000))+(aftaNoise*(howMuchNoise/10000.)*(random.randint(-32767,32767))*(inRay[gno]))

		outRay[gno+int(zOnLag)]+=(inRay[gno])/((1+zOnFirsre)**2)
		outRay[gno+int(zOnLag)]+=((inRay[gno])/((1+zOnSecre)**2))*(loss/1000)
		outRay[gno+int(zTwLag)]+=(inRay[gno])/((1+zTwFirsre)**2)
		outRay[gno+int(zTwLag)]+=((inRay[gno])/((1+zTwSecre)**2))*(loss/1000)

		for vapp in range(allpass):
			outRay[gno+(int(zOnLag)/(2*vapp+2))]+=((inRay[gno])/((1+zOnFirsre)**3))+(aftaNoise*(howMuchNoise/10000.)*(random.randint(-32767,32767))*(inRay[gno]))
			outRay[gno+(int(zOnLag)/(2*vapp+2))]+=(((inRay[gno])/((1+zOnSecre)**3))*(loss/2000))+(aftaNoise*(howMuchNoise/10000.)*(random.randint(-32767,32767))*(inRay[gno]))
			outRay[gno+(int(zTwLag)/(2*vapp+2))]+=((inRay[gno])/((1+zTwFirsre)**3))*(aftaNoise*(howMuchNoise/10000.)*(random.randint(-32767,32767))*(inRay[gno]))
			outRay[gno+(int(zTwLag)/(2*vapp+2))]+=(((inRay[gno])/((1+zTwSecre)**3))*(loss/2000))+(aftaNoise*(howMuchNoise/10000.)*(random.randint(-32767,32767))*(inRay[gno]))
			if gno > (int(zOnLag)/(vapp+2)) and gno > (int(zTwLag)/(vapp+2)):
				outRay[gno-(int(zOnLag)/(2*vapp+2))]+=((inRay[gno])/((1+zOnFirsre)**3))+(aftaNoise*(howMuchNoise/10000.)*(random.randint(-32767,32767)))
				outRay[gno-(int(zOnLag)/(2*vapp+2))]+=(((inRay[gno])/((1+zOnSecre)**3))*(loss/2000))+(aftaNoise*(howMuchNoise/10000.)*(random.randint(-32767,32767))*(inRay[gno]))
				outRay[gno-(int(zTwLag)/(2*vapp+2))]+=((inRay[gno])/((1+zTwFirsre)**3))+(aftaNoise*(howMuchNoise/10000.)*(random.randint(-32767,32767))*(inRay[gno]))
				outRay[gno-(int(zTwLag)/(2*vapp+2))]+=(((inRay[gno])/((1+zTwSecre)**3))*(loss/2000))+(aftaNoise*(howMuchNoise/10000.)*(random.randint(-32767,32767))*(inRay[gno]))

		if gno%((int(len(inRay)))/100)==0:
			percent += 1
			print percent, '%', 'ONTHRE'
	return outRay

def twthre(durRay,source,ear,room,loss,howMuchNoise,aftaNoise,allpass): #How durRay sounds, when it bounces off two walls
	inRay = durRay
	outRay = []
	xs,ys,zs=source#Location of sound source
	xe,ye,ze=ear#Location of ear
	xr,yr,zr=room#Size of room
	dist=(((xe-xs)**2)+((ye-ys)**2)+((ze-zs)**2))**(0.5)

	if zs==ze:
		xDistang=ys-ye
	else:
		xDistang=(((ys-ye)**2)+((zs-ze)**2))**(0.5)

	xouratan=math.atan(((2*xr)+xe-xs)/(xDistang))
	xOnFirsre=(xr-xs)/math.sin(xouratan)
	xOnSecre=(xr)/math.sin(xouratan)
	xOnThire=(xe)/math.sin(xouratan)

	if zs==ze:
		yDistang=xs-xe
	else:
		yDistang=(((xs-xe)**2)+((zs-ze)**2))**(0.5)

	youratan=math.atan(((2*yr)+ye-ys)/(yDistang))
	yOnFirsre=(yr-ys)/math.sin(youratan)
	yOnSecre=(yr)/math.sin(youratan)
	yOnThire=(ye)/math.sin(youratan)

	xLag = (xOnFirsre+xOnSecre+xOnThire)/speedOfSound
	yLag = (yOnFirsre+yOnSecre+yOnThire)/speedOfSound

	percent = 0
	lags = [xLag,yLag]
	for yit in range(len(inRay)+int(max(lags))+1):
		outRay.append(0.)
	for gno in range(len(inRay)):
		if gno > max(lags):
			for vapp in range(10):
				outRay[gno+(int(min(lags)))+random.randint(1,10)] += random.randint(-3276,3276)*aftaNoise*inRay[gno-int(max(lags))]/10000

		outRay[gno+int(xLag)]+=(inRay[gno])/((1+xOnFirsre)**2)
		outRay[gno+int(xLag)]+=((inRay[gno])/((1+xOnSecre)**2))*(loss/1000)
		outRay[gno+int(xLag)]+=((inRay[gno])/((1+xOnThire)**2))*((loss/1000)**2)
		outRay[gno+int(xLag)]+=(inRay[gno])/((1+xOnThire)**2)
		outRay[gno+int(xLag)]+=((inRay[gno])/((1+xOnSecre)**2))*(loss/1000)
		outRay[gno+int(xLag)]+=((inRay[gno])/((1+xOnFirsre)**2))*((loss/1000)**2)

		for vapp in range(allpass):
			outRay[gno+(int(xLag)/(2*vapp+2))]+=((inRay[gno])/((1+xOnFirsre)**3))+(aftaNoise*(howMuchNoise/10000.)*(random.randint(-32767,32767))*(inRay[gno]))
			outRay[gno+(int(xLag)/(2*vapp+2))]+=(((inRay[gno])/((1+xOnSecre)**3))*(loss/1000))+(aftaNoise*(howMuchNoise/10000.)*(random.randint(-32767,32767))*(inRay[gno]))
			outRay[gno+(int(xLag)/(2*vapp+2))]+=(((inRay[gno])/((1+xOnThire)**3))*((loss/1000)**2))+(aftaNoise*(howMuchNoise/10000.)*(random.randint(-32767,32767))*(inRay[gno]))
			outRay[gno+(int(xLag)/(2*vapp+2))]+=((inRay[gno])/((1+xOnThire)**3))+(aftaNoise*(howMuchNoise/10000.)*(random.randint(-32767,32767))*(inRay[gno]))
			outRay[gno+(int(xLag)/(2*vapp+2))]+=(((inRay[gno])/((1+xOnSecre)**3))*(loss/1000))+(aftaNoise*(howMuchNoise/10000.)*(random.randint(-32767,32767))*(inRay[gno]))
			outRay[gno+(int(xLag)/(2*vapp+2))]+=(((inRay[gno])/((1+xOnFirsre)**3))*((loss/1000)**2))+(aftaNoise*(howMuchNoise/10000.)*(random.randint(-32767,32767))*(inRay[gno]))

			if gno > (int(xLag)/(vapp+2)) and gno:
				outRay[gno-(int(xLag)/(2*vapp+2))]+=((inRay[gno])/((1+xOnFirsre)**3))+(aftaNoise*(howMuchNoise/10000.)*(random.randint(-32767,32767))*(inRay[gno]))
				outRay[gno-(int(xLag)/(2*vapp+2))]+=(((inRay[gno])/((1+xOnSecre)**3))*(loss/1000))+(aftaNoise*(howMuchNoise/10000.)*(random.randint(-32767,32767))*(inRay[gno]))
				outRay[gno-(int(xLag)/(2*vapp+2))]+=(((inRay[gno])/((1+xOnThire)**3))*((loss/1000)**2))+(aftaNoise*(howMuchNoise/10000.)*(random.randint(-32767,32767))*(inRay[gno]))
				outRay[gno-(int(xLag)/(2*vapp+2))]+=((inRay[gno])/((1+xOnThire)**3))+(aftaNoise*(howMuchNoise/10000.)*(random.randint(-32767,32767))*(inRay[gno]))
				outRay[gno-(int(xLag)/(2*vapp+2))]+=(((inRay[gno])/((1+xOnSecre)**3))*(loss/1000))+(aftaNoise*(howMuchNoise/10000.)*(random.randint(-32767,32767))*(inRay[gno]))
				outRay[gno-(int(xLag)/(2*vapp+2))]+=(((inRay[gno])/((1+xOnFirsre)**3))*((loss/1000)**2))+(aftaNoise*(howMuchNoise/10000.)*(random.randint(-32767,32767))*(inRay[gno]))

		outRay[gno+int(yLag)]+=(inRay[gno])/((1+yOnFirsre)**2)
		outRay[gno+int(yLag)]+=((inRay[gno])/((1+yOnSecre)**2))*(loss/1000)
		outRay[gno+int(yLag)]+=((inRay[gno])/((1+yOnThire)**2))*((loss/1000)**2)
		outRay[gno+int(yLag)]+=(inRay[gno])/((1+yOnThire)**2)
		outRay[gno+int(yLag)]+=((inRay[gno])/((1+yOnSecre)**2))*(loss/1000)
		outRay[gno+int(yLag)]+=((inRay[gno])/((1+yOnFirsre)**2))*((loss/1000)**2)

		for vapp in range(allpass):
			outRay[gno+(int(yLag)/(2*vapp+2))]+=((inRay[gno])/((1+xOnFirsre)**3))+(aftaNoise*(howMuchNoise/10000.)*(random.randint(-32767,32767))*(inRay[gno]))
			outRay[gno+(int(yLag)/(2*vapp+2))]+=(((inRay[gno])/((1+xOnSecre)**3))*(loss/1000))+(aftaNoise*(howMuchNoise/10000.)*(random.randint(-32767,32767))*(inRay[gno]))
			outRay[gno+(int(yLag)/(2*vapp+2))]+=(((inRay[gno])/((1+xOnThire)**3))*((loss/1000)**2))+(aftaNoise*(howMuchNoise/10000.)*(random.randint(-32767,32767))*(inRay[gno]))
			outRay[gno+(int(yLag)/(2*vapp+2))]+=((inRay[gno])/((1+xOnThire)**3))+(aftaNoise*(howMuchNoise/10000.)*(random.randint(-32767,32767))*(inRay[gno]))
			outRay[gno+(int(yLag)/(2*vapp+2))]+=(((inRay[gno])/((1+xOnSecre)**3))*(loss/1000))+(aftaNoise*(howMuchNoise/10000.)*(random.randint(-32767,32767))*(inRay[gno]))
			outRay[gno+(int(yLag)/(2*vapp+2))]+=(((inRay[gno])/((1+xOnFirsre)**3))*((loss/1000)**2))+(aftaNoise*(howMuchNoise/10000.)*(random.randint(-32767,32767))*(inRay[gno]))

			if gno > (int(yLag)/(vapp+2)):
				outRay[gno-(int(yLag)/(2*vapp+2))]+=((inRay[gno])/((1+yOnFirsre)**3))+(aftaNoise*(howMuchNoise/10000.)*(random.randint(-32767,32767))*(inRay[gno]))
				outRay[gno-(int(yLag)/(2*vapp+2))]+=(((inRay[gno])/((1+yOnSecre)**3))*(loss/1000))+(aftaNoise*(howMuchNoise/10000.)*(random.randint(-32767,32767))*(inRay[gno]))
				outRay[gno-(int(yLag)/(2*vapp+2))]+=(((inRay[gno])/((1+yOnThire)**3))*((loss/1000)**2))+(aftaNoise*(howMuchNoise/10000.)*(random.randint(-32767,32767))*(inRay[gno]))
				outRay[gno-(int(yLag)/(2*vapp+2))]+=((inRay[gno])/((1+yOnThire)**3))+(aftaNoise*(howMuchNoise/10000.)*(random.randint(-32767,32767))*(inRay[gno]))
				outRay[gno-(int(yLag)/(2*vapp+2))]+=(((inRay[gno])/((1+yOnSecre)**3))*(loss/1000))+(aftaNoise*(howMuchNoise/10000.)*(random.randint(-32767,32767))*(inRay[gno]))
				outRay[gno-(int(yLag)/(2*vapp+2))]+=(((inRay[gno])/((1+yOnFirsre)**3))*((loss/1000)**2))+(aftaNoise*(howMuchNoise/10000.)*(random.randint(-32767,32767))*(inRay[gno]))

		if gno%((int(len(inRay)))/100)==0:
			percent += 1
			print percent, '%', 'TWTHRE'
	return outRay