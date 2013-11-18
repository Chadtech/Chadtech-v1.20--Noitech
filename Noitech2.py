import os
import math
import random
import struct
import wave
import pygame

sampleRate = 44100.
amp = 32767
oneSec = 1000.
noteDiv = 12
barNum = 4
noteDur = 1782. # time length of note in thousandths of a second
noteCou = 4 #Number of notes per bar
percent = 0
speedOfSound = 340.49/sampleRate
songDur = (barNum*(noteDur/oneSec))*sampleRate
fileName = ''

#------------------------------Tone making

def putTone(tone,dur): #Returns an array of a given tone, over a certain time, at a certain decay rate. Decay rate of 1000 does not decay. 999 decays very quickly.
	values = []
	inTone = float(tone)/sampleRate
	inDur = int(float(dur)*(noteDur/oneSec)*(sampleRate))
	for yit in range(inDur):
		values.append(0.)
	for vapp in range(inDur):
		value = math.sin((vapp*2*math.pi*inTone))*amp
		values[vapp] = value
	return values

def harmize(tone,harmRay,dur):
	values = []
	inTone = float(tone)/sampleRate
	inDur = int(float(dur)*(noteDur/oneSec)*(sampleRate))
	for yit in range(inDur):
		values.append(0.)
	for vapp in range(len(harmRay)):
		harmH, harmVol = harmRay[vapp]
		inTone = float(tone*harmH)/sampleRate
		for  quoo in range(inDur):
			value = (math.sin((quoo*2*math.pi*inTone))*amp)
			value = value*(harmVol/1000.)
			values[quoo] += value
	return values

#--------------------------------Building

def makeSong(dur): # Makes an empty array with the length given (dur) in notes of time length noteDur and sample length of noteDur/1000 * sampleRate
	outRay = []
	inDur = int(float(dur)*(noteDur/oneSec)*(sampleRate))
	for vapp in range(inDur):
		outRay.append(0)
	return outRay

def givDur(barNum,noteDur,notePbar): #Returns the duration in samples, given the number of bars, number of notes per bar, and time duration of each note
	return (noteDur/oneSec*sampleRate)*notePbar*barNum

def buildSong(whereAt,durRay,songRay): #whereAt is (WhichBar, which of noteDiv*barNum in whichbar), function adds input array to song array starting at whereAt. 
#	whichBarIn, whichNoteIn = whereAt
#	whereAtIn = (sampleRate*(noteDur/oneSec))*noteCou*(barNum*whichBarIn)
	whereAtIn = whereAt*(noteDur/oneSec)*sampleRate
	for vapp in range(len(durRay)):
		songRay[vapp+int(whereAtIn)] += durRay[vapp]

def openFile(fileName):
	outRay = []
	vss = wave.open(fileName)
	numFrams = vss.getnframes()
	vssstr = vss.readframes(numFrams)
#	for yit in range(numFrams):
#		firsSam = ord(vssstr[yit*2])
#		secSam = ord(vssstr[1+(yit*2)])
#		firsSam = firsSam*256
#		sample = (firsSam+secSam)
	samples = struct.unpack_from('%dh'%numFrams,vssstr)
	#outRay.append(int(sample))
	for yit in samples:
		outRay.append(yit)
	return outRay

def buildFile(song): #Turns input 'song' into .wav file.
	print 'Name the File:'
	fileName = raw_input()
	noise_output = wave.open(fileName, 'w')
	noise_output.setparams((1, 2, sampleRate, 0, 'NONE', 'not compressed'))	
	percent = 0
	for yit in range(len(song)):
		if song[yit] < 32767 and song[yit] > -32767:
			packed_value = struct.pack('h', (song[yit]))
			noise_output.writeframes(packed_value)
			if yit%(int(len(song))/100)==0:
				percent += 1
				print percent, '%', song[yit]
		else:
			if song[yit] >= 32767:
				packed_value = struct.pack('h', 32767)
				noise_output.writeframes(packed_value)
				if yit%(int(len(song))/100)==0:
					percent += 1
					print percent, '%', song[yit]
			if song[yit] <= -32767:
				packed_value = struct.pack('h', -32767)
				noise_output.writeframes(packed_value)
				if yit%(int(len(song))/100)==0:
					percent += 1
					print percent, '%', song[yit]
	noise_output.close()

#--------------------------------Effects

def volSlop(durRay,volSlop):
	inRay = durRay
	volSlop = (volSlop/1000. + 999.)/1000.
	for vapp in range(len(durRay)):
		inRay[vapp] = inRay[vapp]*(volSlop**vapp)
	return inRay

def volDrop(durRay,volPert):
	inRay = durRay
	volPert = volPert/1000.
	for vapp in range(len(inRay)):
		inRay[vapp] = inRay[vapp]*volPert
	return inRay

def reverse(durRay):
	inRay = []
	for vapp in range(len(durRay)):
		inRay.append(0.)
	for vapp in range(len(durRay)):
		inRay[vapp] = durRay[len(durRay)-vapp]

def zethre(durRay,source,ear):
	inRay = durRay
	outRay = []
	xs,ys,zs=source
	xe,ye,ze=ear
	dist=(((xe-xs)**2)+((ye-ys)**2)+((ze-zs)**2))**(0.5) #Distance from the sound source to the ear
	lag=dist/speedOfSound
	for yit in range(int(lag)+1):
		inRay.append(0.)
	for vapp in range(len(inRay)):
		outRay.append(0.)
	print lag, len(outRay)	
	for gno in range(len(outRay)-int(lag)):
		outRay[gno+int(lag)]=(4*inRay[gno])/(1+dist)
	return outRay

def onthre(durRay,source,ear,room,loss,howMuchNoise,aftaNoise,allpass):
	inRay = durRay
	outRay = []
	xs,ys,zs=source#Location of sound source
	xe,ye,ze=ear#Location of ear
	xr,yr,zr=room#Size of room
	dist=(((xe-xs)**2)+((ye-ys)**2)+((ze-zs)**2))**(0.5)
	#print 'xe-xs**2', (xe-xs)**2, 'ye-ys**2', (ye-ys)**2, 'ze-zs**2', (ze-zs)**2 

	RRx = ((dist**2)-((xs-xe)**2))**(0.5) 
	#print 'x',RRx, xr, xs, xe
	RRy = ((dist**2)-((ys-ye)**2))**(0.5)
	#print 'y',RRy, yr, ys, ye
	RRz = ((dist**2)-((zs-ze)**2))**(0.5)
	#print 'z',RRz, zr, zs, ze

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

#	print dist, 'x', xOnFirsre+xOnSecre, xTwFirsre+xTwSecre, 'y', ys, ye, yr, yTwFirsre, yTwSecre, 'z', zOnFirsre, zOnSecre
	percent = 0
	lags = [xOnLag,xTwLag,yOnLag,yTwLag,zOnLag,zTwLag]
	print lags
	print 'PART A'
	for yit in range(len(inRay)+int(max(lags))+1):
		outRay.append(0.)
	for gno in range(len(inRay)):
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
			print percent, '%'
	return outRay

def Twthre(durRay,source,ear,room,loss,howMuchNoise,aftaNoise):
	inRay = durRay
	outRay = []
	xs,ys,zs=source#Location of sound source
	xe,ye,ze=ear#Location of ear
	xr,yr,zr=room#Size of room
	dist=(((xe-xs)**2)+((ye-ys)**2)+((ze-zs)**2))**(0.5)

	if RRx !=0:
		xOnFirsre = dist*(xr-xs)/(xs-xe)
		xOnSecre = dist*(((xOnFirsre)*2)**(0.5))/(ys-ye)
		xOnThire = dist*ye/(ys-ye)
		#xTwFirsre = dist*(yr-ys)/
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

#	print dist, 'x', xOnFirsre+xOnSecre, xTwFirsre+xTwSecre, 'y', ys, ye, yr, yTwFirsre, yTwSecre, 'z', zOnFirsre, zOnSecre
	percent = 0
	lags = [xOnLag,xTwLag,yOnLag,yTwLag,zOnLag,zTwLag]
	print lags
	print 'PART A'
	for yit in range(len(inRay)+int(max(lags))+1):
		outRay.append(0.)
	for gno in range(len(inRay)):
		outRay[gno+int(xOnLag)]+=(inRay[gno])/((1+xOnFirsre)**2)
		outRay[gno+int(xOnLag)]+=((inRay[gno])/((1+xOnSecre)**2))*(loss/1000)
		outRay[gno+int(xTwLag)]+=(inRay[gno])/((1+xTwFirsre)**2)
		outRay[gno+int(xTwLag)]+=((inRay[gno])/((1+xTwSecre)**2))*(loss/1000)

		outRay[gno+int(yOnLag)]+=(inRay[gno])/((1+yOnFirsre)**2)
		outRay[gno+int(yOnLag)]+=((inRay[gno])/((1+yOnSecre)**2))*(loss/1000)
		outRay[gno+int(yTwLag)]+=(inRay[gno])/((1+yTwFirsre)**2)
		outRay[gno+int(yTwLag)]+=((inRay[gno])/((1+yTwSecre)**2))*(loss/1000)

		outRay[gno+int(zOnLag)]+=(inRay[gno])/((1+zOnFirsre)**2)
		outRay[gno+int(zOnLag)]+=((inRay[gno])/((1+zOnSecre)**2))*(loss/1000)
		outRay[gno+int(zTwLag)]+=(inRay[gno])/((1+zTwFirsre)**2)
		outRay[gno+int(zTwLag)]+=((inRay[gno])/((1+zTwSecre)**2))*(loss/1000)
		if gno%((int(len(inRay)))/100)==0:
			percent += 1
			print percent, '%'

	return outRay

goty = openFile('GOTYYY.wav')
hslroom = (16,30,15)
gotyZeth = zethre(goty,(1,20,10),(15,15,2))
gotyOnth = onthre(goty,(1,20,10),(15,15,2),hslroom,30,0.5,False,8)
gotyOnth = volDrop(gotyOnth,150)

buildSong(0,gotyZeth,gotyOnth)
buildFile(gotyOnth)