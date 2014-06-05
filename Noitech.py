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
noteDur = 150 # time length of note in thousandths of a second
noteCou = 4 #Number of notes per bar
percent = 0
speedOfSound = 340.49/sampleRate
songDur = (barNum*(noteDur/oneSec))*sampleRate
fileName = ''

######## 'Dur' is short for 'Duration'
######## 'inDur' is the duration converted into samples
####

class Noitech():
	def __init__(self,sampleRate=44100,amplitude=32767,noteLength=400.):
		self.sampleRate=sampleRate
		self.amplitude=ampltitude
		self.noteLength=noteLength

#------------------------------Tone making

def makeTone(tone,dur): #Returns an array of a sine wave with frequency TONE, for duration DUR.
	outRay = []
	inTone = float(tone)/sampleRate
	inDur = int(float(dur)*(noteDur/oneSec)*(sampleRate))
	for time in [0]*inDur:
		outRay.append(0.)
	for index in range(inDur):
		value = math.sin((index*2*math.pi*inTone))*amp
		outRay[index] = value
	return outRay

def makeSaw(tone,dur,harmNum): #Make a saw tooth wave, at frequency TONE, for duration DUR. A saw tooth is a construction of harmonics, which approaches infinitely the saw tooth wave form. harmNum is how many of those harmonics to generate
	outRay = []
	inTone = float(tone)/sampleRate
	inDur = int(float(dur)*(noteDur/oneSec)*(sampleRate))
	for yit in range(inDur):
		outRay.append(0.)
	for harmonic in range(1,harmNum):
		for vapp in range(len(values)):
			outRay[vapp]+= amp*((-1)**(harmonic))*(math.sin(vapp*2*math.pi*inTone*harmonic)/harmonic)
	return outRay

def makeSawEnharmonic(tone,dur,harmNum,enharmonicity=0.0007): #Make a saw tooth wave, but increase the frequency of the harmonics a small amount that scales with rhe harmonic number.
	outRay = []
	inTone = float(tone)/sampleRate
	inDur = int(float(dur)*(noteDur/oneSec)*(sampleRate))
	for time in [0]*inDur:
		values.append(0.)
	for harmonic in range(1,harmNum):
		for moment in range(len(outRay)):
			outRay[vapp]+= amp*((-1)**(harmonic))*(math.sin(moment*2*math.pi*inTone*harmonic*enharmonicity)/harmonic)
	return moment

def makeSawMitDecay(tone,dur,harmNum,decayRate=8481.): #Make a saw tooth wave, but make it so the harmonics decay in volume, and the tonic increases in volume
	outRay = []
	inTone = float(tone)/sampleRate
	inDur = int(float(dur)*(noteDur/oneSec)*(sampleRate))
	for time in [0]*inDur:
		outRay.append(0.)
	for harmonic in range(1,harmNum):
		for moment in range(len(outRay)):
			if harmonic>1:
				outRay[moment]+= (decayRate/((decayRate/20.)+(moment*(harmNum))))*amp*((-1)**(harmonic))*(math.sin(moment*2*math.pi*inTone*harmonic)/harmonic)
			else:
				outRay[moment]+= (1-(decayRate/(decayRate+(harmNum*3*moment))))*amp*((-1)**(harmonic))*(math.sin(vapp*2*math.pi*inTone*harmonic)/harmonic)
	return outRay

def makeSquare(tone,dur,harmNum): #Make a square wave with frequency TONE, for duration DUR
	values = []
	inTone = float(tone)/sampleRate
	inDur = int(float(dur)*(noteDur/oneSec)*(sampleRate))
	for yit in range(inDur):
		values.append(0.)
	for harmonic in range(1,harmNum):
		for vapp in range(len(values)):
			values[vapp]+= amp*(math.sin(vapp*2*math.pi*inTone*((harmonic*2)-1))/(((harmonic*2)-1)))
	return values

def makeTriangle(tone,dur,harmNum): #Make a triangle wave, with frequency TONE, for duration DUR
	outRay = []
	inTone = float(tone)/sampleRate
	inDur = int(float(dur)*(noteDur/oneSec)*(sampleRate))
	for time in [0]*inDur:
		outRay.append(0.)
	for harmonic in range(harmNum):
		for moment in range(len(outRay)):
			outRay[moment]+= amp*((-1)**(harmonic))*(math.sin(moment*2*math.pi*inTone*((harmonic*2)+1))/(((harmonic*2)+1)**2))
	return outRay

def makeTriangleEnharmonic(tone,dur,harmNum): #Make a Triangle Wave with enharmonics
	outRay = []
	inTone = float(tone)/sampleRate
	inDur = int(float(dur)*(noteDur/oneSec)*(sampleRate))
	for time in [0]*inDur:
		outRay.append(0.)
	for harmonic in range(harmNum):
		for moment in range(len(outRay)):
			outRay[moment]+= amp*((-1)**(harmonic))*(math.sin((1+harmonic*(0.0013))*moment*2*math.pi*inTone*((harmonic*2)+1))/(((harmonic*2)+1)**2))
	return outRay

def makeTriangleEnharmonicMitDecay(tone,dur,harmNum): #Make a Triangle Wave with enharmonics, and with harmonic decay
	outRay = []
	inTone = float(tone)/sampleRate
	inDur = int(float(dur)*(noteDur/oneSec)*(sampleRate))
	for time in [0]*inDur:
		outRay.append(0.)
	for harmonic in range(harmNum):
		for moment in range(len(outRay)):
			outRay[moment]+= (4410/(4410+(moment*harmNum)))*amp*((-1)**(harmonic))*(math.sin((1+harmonic*(0.0013))*moment*2*math.pi*inTone*((harmonic*2)+1))/(((harmonic*2)+1)**2))
	return outRay

def makeTriangleEnharmonicMitDecayCompressed(tone,dur,harmNum): #Make a Triangle Wave with enharmonics
	outRay = []
	inTone = float(tone)/sampleRate
	inDur = int(float(dur)*(noteDur/oneSec)*(sampleRate))
	for time in [0]*inDur:
		values.append(0.)
	for harmonic in range(harmNum):
		for moment in range(len(outRay)):
			if harmonic>0:
				outRay[moment]+= ((8481./(481.+(moment*(harmNum))))*2*amp*((-1)**(harmonic))*(math.sin((1+(harmonic*(0.00007)))*moment*2*math.pi*inTone*((harmonic*2)+1))/(((harmonic*2)+1)**2)))
			else:
				outRay[moment]+= ((1-(8481./(8481.+(harmNum*3*moment))))*amp*((-1)**(harmonic))*(math.sin((1+(harmonic*(0.00007)))*moment*2*math.pi*inTone*((harmonic*2)+1))/(((harmonic*2)+1)**2)))
	return outRay

def harmize(tone,harmRay,dur): #Returns an array of a given tone, with a certain set of harmonics. The harmonics come in an array where each element is (harmonic, relativel Volume, volSlop)
	outRay=[]
	tempoRay=[]
	inTone = float(tone)/sampleRate
	inDur = int(float(dur)*(noteDur/oneSec)*(sampleRate))
	percent = 0
	for yit in range(inDur):
		outRay.append(0.)
		tempoRay.append(0.)
	for parameters in range(len(harmRay)):
		harmH, harmVol, volSlop = harmRay[parameters]
		inTone = float(tone*harmH)/sampleRate
		volSlop = (volSlop/1000. + 999.)/1000.
		for  moment in range(inDur):
			value = (math.sin((moment*2*math.pi*inTone))*amp)
			value = value*(harmVol/1000.)
			tempoRay[moment] = value
		for  moment in range(len(tempoRay)):
			tempoRay[moment]=tempoRay[moment]*(volSlop**moment)
		percent = 0
		for moment in range(inDur):
			outRay[moment]+=tempoRay[moment]
	return outRay

#--------------------------------Building

def makeDur(dur): # Makes an empty array with the length given (dur) in notes of time length noteDur and sample length of noteDur/1000 * sampleRate
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

def tenTimesRate(durRay):
	outRay=[]
	for moment in range(len(durRay)*10):
		outRay.append(0.)
	for moment in range(len(durRay)):
		outRay[moment*10]=durRay[moment]
	for moment in range(len(durRay)-1):
		decileSize = durRay[moment]-durRay[moment+1]
		decileSize = decileSize/10
		for decile in range(10):
			outRay[(moment*10)+decile]= durRay[moment]-(decileSize*decile)
	for lastMoment in range(10):
		outRay[len(outRay)-lastMoment]=outRay[len(outRay)-10]-(decileSize*lastMoment)
	return outRay

def tenthRate(durRay):
	outRay=[]
	for moment in range(len(durRay)/10):
		outRay.append(0.)
	for moment in range(len(outRay)):
		value = 0
		for decile in range(10):
			value+=durRay[(moment*10)+decile]
			value=value/10
		outRay[moment]=value



def openFile(fileName): # If you have a .wav file you want to manipulate, you can load it into an array with this function
	outRay = []
	vss = wave.open(fileName)
	numFrams = vss.getnframes()
	vssstr = vss.readframes(numFrams)
	samples = struct.unpack_from('%dh'%numFrams,vssstr)
	for yit in samples:
		outRay.append(yit)
	return outRay

def buildFile(song,fileName): #Turns input 'song' into .wav file.
	if not fileName.endswith('.wav'):
		fileName=fileName+'.wav'
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

def fadeOut(durRay,beginning=0,ending=''):
	if type(ending)!=int or ending>len(durRay):
		ending=len(durRay)
	outRay=[]
	for time in range(len(durRay)):
		outRay.append(durRay[time])
	for time in range(ending-beginning):
		outRay[time+beginning]*=(((ending-beginning)-time)/float((ending-beginning)))
	return outRay

def fadeIn(durRay,beginning=0,ending=''):
	if type(ending)!=int:
		ending=len(durRay)
	else:
		if ending>len(durRay):
			ending=len(durRay)
	outRay=[]
	for time in range(len(durRay)):
		outRay.append(durRay[time])
	for time in range(ending-beginning):
		outRay[time+beginning]*=(1-(((ending-beginning)-time)/float((ending-beginning))))
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
	print 'halfSpeed INPUT length', len(durRay)
	outRay =[]
	for moment in range(len(durRay)):
		outRay.append(0.)
		outRay.append(0.)
	for moment in range(len(durRay)):
		outRay[(moment*2)]=durRay[moment]
	for moment in range(len(durRay)-1):
		value = durRay[moment]+durRay[moment+1]
		value /= 2.
		outRay[(moment*2)+1]=value
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
	for moment in range(len(durRay)*divisions):
		outRay.append(0.)
	for moment in range(len(durRay)-1):
		difference=durRay[moment]-durRay[moment+1]
		difference/=float(divisions)
		for gap in range(divisions):
			outRay[(moment*divisions)+gap]=durRay[moment]+(difference*gap)
	return outRay

def factorize(fraction):
	numeratorFactors,denominatorFactors=[],[]
	wholeNumberEr=1
	fraction=float(fraction)
	while not (fraction*wholeNumberEr).is_integer():
		wholeNumberEr+=1
	denominator=wholeNumberEr
	numerator=fraction*denominator
	denominator,numerator=float(denominator),float(numerator)
	factorCandidate = 2.
	notDoneFactoring =True
	while notDoneFactoring:
		if (denominator/factorCandidate).is_integer():
			denominator=denominator/factorCandidate
			denominatorFactors.append(factorCandidate)
			factorCandidate=2.
		else:
			factorCandidate+=1
		if factorCandidate>denominator:
			notDoneFactoring=False
	factorCandidate = 2.
	notDoneFactoring =True
	while notDoneFactoring:
		if (numerator/factorCandidate).is_integer():
			numerator=numerator/factorCandidate
			numeratorFactors.append(factorCandidate)
			factorCandidate=2.
		else:
			factorCandidate+=1
		if factorCandidate>numerator:
			notDoneFactoring=False
	return [numeratorFactors,denominatorFactors]

def changeSpeed(durRay,speedChange):
	numerators,denominators=factorize(speedChange)
	multiply=1
	divide=1
	for number in numerators:
		multiply=multiply*number
	for number in denominators:
		divide=divide*number
	return multiplySpeed(divideSpeed(durRay,int(divide)),int(multiply))

def shiftSamples(durRay,shiftMag): #shiftMag must be between -1 and 1
	outRay=[]
	dimRay=[]
	if shiftMag>0:
		shiftDirection = True
	else:
		shiftDirection = False
	shiftMag=math.fabs(shiftMag)
	for time in range(len(durRay)):
		outRay.append(0.)
		dimRay.append(durRay[time])
	for moment in range(len(dimRay)):
		dimRay[moment]/=1000.
	if shiftDirection:
		for moment in range(len(outRay)-1):
			outRay[moment]=((1-shiftMag)*durRay[moment])+(durRay[moment+1]*shiftMag)
	else:
		for moment in range(len(outRay)-1):
			outRay[moment]=((1-shiftMag)*durRay[moment+1])+(durRay[moment]*shiftMag)
	return outRay

def grainSynth(durRay,freqInc,grainLength):
	inputLength=len(durRay)
	freqAdjGrainLength=freqInc*grainLength
	grains=[]
	for section in range(len(durRay)/grainLength):
		grain=[]
		for moment in range(int(freqAdjGrainLength)):
			if len(durRay)>((section*grainLength)+moment):
				grain.append(durRay[(section*grainLength)+moment])
		grains.append(grain)
	grain=[]
	for moment in range(len(durRay)-((len(durRay)/grainLength)*grainLength)):
		grain.append(durRay[moment+((len(durRay)/grainLength)*grainLength)])
	grains.append(grain)
	for grain in range(len(grains)):
		if len(grains[grain]):
			grains[grain]=changeSpeed(grains[grain],freqInc)
			grains[grain]=fadeOut(grains[grain],beginning=(len(grains[grain])-30))
			grains[grain]=fadeIn(grains[grain],ending=30)
	outRay=[]
	for grain in grains:
		for moment in grain:
			outRay.append(moment)
	return outRay

def randomAdd(durRay,distance=30,magnitude=1.):
	outRay=[]
	for moment in durRay:
		outRay.append(moment)
	for moment in distance*[0]:
		outRay.append(0.)
	for moment in range(len(durRay)):
		outRay[moment+distance]+=durRay[moment]*(magnitude*(float(random.randint(0,100))/100.))
	return outRay

##### This one doesnt work
def lopass(durRay,cutov):
	outRay = durRay
	for vapp in range(len(durRay)-1):
		outRay[vapp]=((outRay[vapp]+outRay[vapp+1])**(1+cutov/1000))/2
	return outRay