import os
import math
import random
import struct
import wave
import PIL
from PIL import Image

#.............................................................................................

sampleRate = 44100.
amp = 32767
oneSec = 1000.
noteDiv = 12
barNum = 4
noteDur = 350 # time length of note in thousandths of a second
noteCou = 4 #Number of notes per bar
percent = 0
speedOfSound = 340.49/sampleRate
songDur = (barNum*(noteDur/oneSec))*sampleRate
fileName = ''

#------------------------------Tone making

def makeTone(tone,dur): #Returns an array of a sine wave tone, for the input duration duration
	values = []
	inTone = float(tone)/sampleRate
	inDur = int(float(dur)*(noteDur/oneSec)*(sampleRate))
	for yit in range(inDur):
		values.append(0.)
	for vapp in range(inDur):
		value = math.sin((vapp*2*math.pi*inTone))*amp
		values[vapp] = value
	return values

def MakeToneModulus(tone,dur): #Returns an array of a given tone, over a certain time, at a certain decay rate. Decay rate of 1000 does not decay. 999 decays very quickly.
	values = []
	onePeriod = []
	inTone = float(tone)/sampleRate
	inDur = int(float(dur)*(noteDur/oneSec)*(sampleRate))
	for yit in range(inDur):
		values.append(0.)
		onePeriod.append(0.)
	for vapp in range(int(sampleRate/float(tone))):
		value = math.sin((vapp*2*math.pi*inTone))*amp
		onePeriod[vapp] = value
	for gno in range(inDur):
		values[gno]=onePeriod[gno%len(onePeriod)]
	return values

def makeSaw(tone,dur): #Make a saw tooth wave
	values = []
	inTone = float(tone)/sampleRate
	inDur = int(float(dur)*(noteDur/oneSec)*(sampleRate))
	for yit in range(inDur):
		values.append(0.)
	for vapp in range(inDur):
		value = (amp - (((vapp*tone)%(sampleRate))/sampleRate)*amp) - (amp/2)
		values[vapp]=value
	return values

def makeSawTrig(tone,dur,harmNum): #Make a saw tooth wave
	values = []
	inTone = float(tone)/sampleRate
	inDur = int(float(dur)*(noteDur/oneSec)*(sampleRate))
	for yit in range(inDur):
		values.append(0.)
	for harmonic in range(1,harmNum):
		for vapp in range(len(values)):
			values[vapp]+= amp*((-1)**(harmonic))*(math.sin(vapp*2*math.pi*inTone*harmonic)/harmonic)
	return values

def makeSawTrigEnharmonic(tone,dur,harmNum,enharmonicity=0.0007): #Make a saw tooth wave
	values = []
	inTone = float(tone)/sampleRate
	inDur = int(float(dur)*(noteDur/oneSec)*(sampleRate))
	for yit in range(inDur):
		values.append(0.)
	for harmonic in range(1,harmNum):
		for vapp in range(len(values)):
			values[vapp]+= amp*((-1)**(harmonic))*(math.sin(vapp*2*math.pi*inTone*harmonic*enharmonicity)/harmonic)
	return values

def makeSawTrigMitDecayCompressed(tone,dur,harmNum,decayRate=8481.): #Make a saw tooth wave
	values = []
	inTone = float(tone)/sampleRate
	inDur = int(float(dur)*(noteDur/oneSec)*(sampleRate))
	for yit in range(inDur):
		values.append(0.)
	for harmonic in range(1,harmNum):
		for vapp in range(len(values)):
			if harmonic>1:
				values[vapp]+= (decayRate/((decayRate/20.)+(vapp*(harmNum))))*amp*((-1)**(harmonic))*(math.sin(vapp*2*math.pi*inTone*harmonic)/harmonic)
			else:
				values[vapp]+= (1-(decayRate/(decayRate+(harmNum*3*vapp))))*amp*((-1)**(harmonic))*(math.sin(vapp*2*math.pi*inTone*harmonic)/harmonic)
	return values

def makeTriangle(tone,dur): #Make a Triangle wave
	values = []
	inTone = float(tone/2)/sampleRate
	inDur = int(float(dur)*(noteDur/oneSec)*(sampleRate))
	for yit in range(inDur):
		values.append(0.)
	for vapp in range(inDur):
		value = (amp - ((((vapp*(tone/2))%(sampleRate))/sampleRate)*amp) - (amp/2))
		values[vapp]=value
	for gno in range(len(values)):
		values[gno]=math.fabs(values[gno])
	for brs in range(len(values)):
		values[brs] = (values[brs]*2) - (amp/2)
	return values

def makeSquareTrig(tone,dur,harmNum):
	values = []
	inTone = float(tone)/sampleRate
	inDur = int(float(dur)*(noteDur/oneSec)*(sampleRate))
	for yit in range(inDur):
		values.append(0.)
	for harmonic in range(1,harmNum):
		for vapp in range(len(values)):
			values[vapp]+= amp*(math.sin(vapp*2*math.pi*inTone*((harmonic*2)-1))/(((harmonic*2)-1)))
	return values

def makeTriangleTrig(tone,dur,harmNum): #Make a Triangle Wave with trigonometry
	values = []
	inTone = float(tone)/sampleRate
	inDur = int(float(dur)*(noteDur/oneSec)*(sampleRate))
	for yit in range(inDur):
		values.append(0.)
	for harmonic in range(harmNum):
		for vapp in range(len(values)):
			values[vapp]+= amp*((-1)**(harmonic))*(math.sin(vapp*2*math.pi*inTone*((harmonic*2)+1))/(((harmonic*2)+1)**2))
	return values

def makeTriangleEnharmonic(tone,dur,harmNum): #Make a Triangle Wave with enharmonics
	values = []
	inTone = float(tone)/sampleRate
	inDur = int(float(dur)*(noteDur/oneSec)*(sampleRate))
	for yit in range(inDur):
		values.append(0.)
	for harmonic in range(harmNum):
		for vapp in range(len(values)):
			values[vapp]+= amp*((-1)**(harmonic))*(math.sin((1+harmonic*(0.0013))*vapp*2*math.pi*inTone*((harmonic*2)+1))/(((harmonic*2)+1)**2))
	return values

def makeTriangleEnharmonicMitDecay(tone,dur,harmNum): #Make a Triangle Wave with enharmonics
	values = []
	inTone = float(tone)/sampleRate
	inDur = int(float(dur)*(noteDur/oneSec)*(sampleRate))
	for yit in range(inDur):
		values.append(0.)
	for harmonic in range(harmNum):
		for vapp in range(len(values)):
			values[vapp]+= (4410/(4410+(vapp*harmNum)))*amp*((-1)**(harmonic))*(math.sin((1+harmonic*(0.0013))*vapp*2*math.pi*inTone*((harmonic*2)+1))/(((harmonic*2)+1)**2))
	return values

def makeTriangleEnharmonicMitDecayCompressed(tone,dur,harmNum): #Make a Triangle Wave with enharmonics
	values = []
	inTone = float(tone)/sampleRate
	inDur = int(float(dur)*(noteDur/oneSec)*(sampleRate))
	for yit in range(inDur):
		values.append(0.)
	for harmonic in range(harmNum):
		for vapp in range(len(values)):
			if harmonic>0:
				values[vapp]+= ((8481./(481.+(vapp*(harmNum))))*2*amp*((-1)**(harmonic))*(math.sin((1+(harmonic*(0.00007)))*vapp*2*math.pi*inTone*((harmonic*2)+1))/(((harmonic*2)+1)**2)))
			else:
				values[vapp]+= ((1-(8481./(8481.+(harmNum*3*vapp))))*amp*((-1)**(harmonic))*(math.sin((1+(harmonic*(0.00007)))*vapp*2*math.pi*inTone*((harmonic*2)+1))/(((harmonic*2)+1)**2)))
	return values

def harmize(tone,harmRay,dur): #Returns an array of a given tone, with a certain set of harmonics. The harmonics come in an array where each element is (harmonic, relativel Volume, volSlop)
	outRay=[]
	tempoRay=[]
	inTone = float(tone)/sampleRate
	inDur = int(float(dur)*(noteDur/oneSec)*(sampleRate))
	percent = 0
	for yit in range(inDur):
		outRay.append(0.)
		tempoRay.append(0.)
	for vapp in range(len(harmRay)):
		harmH, harmVol, volSlop = harmRay[vapp]
		inTone = float(tone*harmH)/sampleRate
		volSlop = (volSlop/1000. + 999.)/1000.
		for  quoo in range(inDur):
			value = (math.sin((quoo*2*math.pi*inTone))*amp)
			value = value*(harmVol/1000.)
			tempoRay[quoo] = value
		for  gno in range(len(tempoRay)):
			tempoRay[gno]=tempoRay[gno]*(volSlop**gno)
		percent = 0
		for dukh in range(inDur):
			outRay[dukh]+=tempoRay[dukh]
	return outRay

	for vapp in range(len(durRay)):
		inRay[vapp] = inRay[vapp]*(volSlop**vapp)

#--------------------------------Building

def makeSong(dur): # Makes an empty array with the length given (dur) in notes of time length noteDur and sample length of noteDur/1000 * sampleRate
	outRay = []
	inDur = int(float(dur)*(noteDur/oneSec)*(sampleRate))
	for vapp in range(inDur):
		outRay.append(0.)
	return outRay

def givDur(barNum,dur): #Returns the duration in samples, given the number of bars, number of notes per bar, and time duration of each note
	return (noteDur/oneSec*sampleRate)*dur

def buildSong(whereAt,durRay,songRay,level): #whereAt is (WhichBar, which of noteDiv*barNum in whichbar), function adds input array to song array starting at whereAt. 
	whereAtIn = whereAt*(noteDur/oneSec)*sampleRate
	for vapp in range(len(durRay)):
		songRay[vapp+int(whereAtIn)] += durRay[vapp] *(level/1000.)

def openFile(fileName): # If you have a .wav file you want to manipulate it, you can load it into an array with this function
	outRay = []
	vss = wave.open(fileName)
	numFrams = vss.getnframes()
	vssstr = vss.readframes(numFrams)
	samples = struct.unpack_from('%dh'%numFrams,vssstr)
	for yit in samples:
		outRay.append(yit)
	return outRay

def buildFile(song,fileName): #Turns input 'song' into .wav file.
	noise_output = wave.open(fileName, 'w')
	noise_output.setparams((1, 2, sampleRate, 0, 'NONE', 'not compressed'))	
	percent = 0
	for yit in range(len(song)):
		if song[yit] < 32767 and song[yit] > -32767:
			packed_value = struct.pack('h', (song[yit]))
			noise_output.writeframes(packed_value)
			if yit%(int(len(song))/100)==0:
				percent += 1
				print percent, '%', song[yit], fileName
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
	print fileName, 'is done'
	noise_output.close()

#--------------------------------Effects

###### Copy the sound file, and add it back to itself MANY times, spaced apart in SPACE intervals
def createMany(durRay,many,space):
	outRay = []
	orig = []
	for yit in range(len(outRay)):
		orig.append(durRay[yit])
		outRay.append(durRay[yit])
	for yit in range(many*space):
		outRay.append(0.)
	for vapp in range(many):
		for dukh in range(len(orig)):
			outRay[dukh+(vapp*space)]+=orig[dukh]
	return outRay

###### No clue what this one does
def triReduc(durRay,divs):
	outRay=[]
	for yit in range(len(durray)):
		outRay.append(durRay[yit])
	incre = 0
	for yit in range(divs-(len(outRay)%divs)):
		outRay.append(0.)
	for vapp in range(len(outray)/divs):
		for gno in range(divs):
			incre = (outRay[vapp]-outRay[vapp+divs])/divs
			for dukh in range(divs-2):
				outRay[vapp+1] = outRay[vapp+1]+(incre*yit)
	return outRay

##### Reduce the "resolution" of the file. Kind of like reducing the frame rate
def bitReduc(durRay,divs):
	outRay = durRay
	ave = 0
	for yit in range(divs-(len(outRay)%divs)):
		outRay.append(0.)
	for vapp in range(len(outRay)/divs):
		for gno in range(divs):
			ave+=outRay[(vapp*divs)+gno]
		ave=ave/divs
		for gno in range(divs):
			outRay[(vapp*divs)+gno]=ave
	return outRay

##### If Cap the volume off at a the value volCut. This will create clipping
def cutOff(durRay,volCut):
	outRay = durRay
	volCut = (volCut/1000.)*amp
	for yit in range(len(outRay)):
		if outRay[yit] > volCut:
			outRay[yit]=volCut
		if outRay[yit] < (-1*volCut):
			outRay[yit]=(-1*volCut)
	return outRay

##### volSlop reduces the volume of the sound over time
##### the input 'volSlop' is a number. The lower the number the faster the volume reduces (1000. is no drop, higher than 1000. is a volume increase)
def volSlop(durRay,volSlop):
	inRay = durRay
	volSlop = (volSlop/1000. + 999.)/1000.
	for vapp in range(len(durRay)):
		inRay[vapp] = inRay[vapp]*(volSlop**vapp)
	return inRay

#### this is a very complicated version of volSlop (below).
#### The input 'volProf' is an array, whos elements are quadtuples. Where the elements in their order is (the starting volume, the ending volume, the duration of the change in volume, where the reduction starts)
def volProf(durRay,volProf):
	inRay=durRay
	for vapp in range(len(volProf)):
		startVol, endVol, dur, whereAt = volProf[vapp]
		whereAt = int(whereAt*(noteDur/oneSec)*sampleRate)
		if dur==0:
			dur = len(durRay)-whereAt
		else:
			dur = int(dur*(noteDur/oneSec)*sampleRate)
		startVol = startVol/1000.
		endVol = endVol/1000.
		for yit in range(dur):
			inRay[whereAt+yit]=inRay[whereAt+yit]*(startVol+((endVol-startVol)/dur)*yit)
		for yit in range(len(inRay)-(whereAt+dur)):
			inRay[yit+dur]=inRay[yit+dur]*endVol
	return inRay

def volDrop(durRay,volPert): #Change the volume for an array as a whole values less than 1000 will lower the volume
	inRay = durRay
	outRay = []
	volPert = volPert/1000.
	percent = 0
	for vapp in range(len(inRay)):
		outRay.append(inRay[vapp]*volPert)
		if vapp%((int(len(inRay)))/100)==0:
			percent += 1
			print percent, '%', 'volDrop'
	return outRay

def reverse(durRay): #Reverse the array
	inRay = []
	for vapp in range(len(durRay)):
		inRay.append(0.)
	for vapp in range(len(durRay)):
		inRay[vapp] = durRay[len(durRay)-vapp]

def zethre(durRay,source,ear): # Add the '0th reflection', ie, simulate how it will sound by traveling the disances between the source and the ear, which are (x,y,z) corrdinates in a room
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
	for gno in range(len(outRay)-int(lag)):
		outRay[gno+int(lag)]=(4*inRay[gno])/(1+dist)
	return outRay

def halfSpeed(durRay):
	outRay =[]
	for moment in range(len(durRay)):
		outRay.append(0.)
		outRay.append(0.)
	for moment in range(len(durRay)):
		outRay[(moment*2)]=durRay[moment]
	for moment in range((len(outRay)/2)-1):
		outRay[(moment*2)+1]=outRay[moment*2]-((outRay[(moment*2)]-outRay[(moment*2)+2])/2.)
	return outRay

def doubleSpeed(durRay):
	outRay=[]
	for moment in range((len(durRay)/2)):
		outRay.append(0.)
	for moment in range(len(outRay)):
		outRay[moment]=(durRay[moment*2]+durRay[(moment*2)+1])/2
	return outRay

def multiplySpeed(durRay,multiples):
	outRay=[]
	for moment in range(len(durRay)/multiples):
		outRay.append(0.)
	for moment in range(len(outRay)):
		value = 0
		for time in range(multiples):
			value+=durRay[(moment*multiples)+time]
		value = value/multiples
		outRay[moment]=value
	return outRay

def divideSpeed(durRay,divisions):
	outRay=[]
	for moment in range(len(durRay)):
		for times in range(divisions):
			outRay.append(0.)
	for moment in range(len(durRay)):
		outRay[moment*divisions]=durRay[moment]
	for moment in range((len(outRay)/divisions)-1):
		difference=outRay[moment*divisions]-outRay[(moment*divisions)+divisions]
		difference=difference/divisions
		for gap in range((divisions)-1):
			outRay[moment+(gap+1)]=outRay[moment*divisions]-(difference*(gap+1))
	return outRay




##### This one doesnt work
def lopass(durRay,cutov):
	outRay = durRay
	for vapp in range(len(durRay)-1):
		outRay[vapp]=((outRay[vapp]+outRay[vapp+1])**(1+cutov/1000))/2
	return outRay