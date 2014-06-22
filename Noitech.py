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
	for time in [0]*dur:
		outRay.append(0.)
	for index in range(dur):
		value = math.sin((index*2*math.pi*tone))*amp
		outRay[index] = value
	return outRay

def makeSaw(tone,dur,harmNum): #Make a saw tooth wave, at frequency TONE, for duration DUR. A saw tooth is a construction of harmonics, which approaches infinitely the saw tooth wave form. harmNum is how many of those harmonics to generate
	outRay = []
	inTone = float(tone)/sampleRate
	for yit in range(dur):
		outRay.append(0.)
	for harmonic in range(1,harmNum):
		for vapp in range(len(outRay)):
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

def concatenate(durRay0,durRay1):
	outRay=[]
	for moment in range(len(durRay0)):
		outRay.append(durRay0[moment])
	for moment in range(len(durRay1)):
		outRay.append(durRay1[moment])
	return outRay


def makeEmptyArray(dur): # Makes an empty array with the length given (dur) in notes of time length noteDur and sample length of noteDur/1000 * sampleRate
	return dur*[0]

def givDur(barNum,dur): #Returns the duration in samples, given the number of bars, number of notes per bar, and time duration of each note
	return (noteDur/oneSec*sampleRate)*dur

def addTo(durRay,canvasRay,whereAt=0,level=1000.): #whereAt is (WhichBar, which of noteDiv*barNum in whichbar), function adds input array to song array starting at whereAt. 
	outRay=[]
	for moment in [0]*len(canvasRay):
		outRay.append(0.)
	for moment in range(len(canvasRay)):
		outRay[moment]=canvasRay[moment]
	for moment in range(len(durRay)):
		outRay[moment+int(whereAt)]+=int((durRay[moment]*(level/1000.)))
	return outRay

def removeFrom(whereAt,durRay,canvasRay,level=1000.): #whereAt is (WhichBar, which of noteDiv*barNum in whichbar), function adds input array to song array starting at whereAt. 
	whereAtIn = whereAt*(noteDur/oneSec)*sampleRate
	for vapp in range(len(durRay)):
		canvasRay[vapp+int(whereAtIn)] -= durRay[vapp] *(level/1000.)

def openFile(fileName): # If you have a .wav file you want to manipulate, you can load it into an array with this function
	outRay = []
	wavFile = wave.open(fileName)
	numberOfFrames = wavFile.getnframes()
	readAllTheFrames = wavFile.readframes(numberOfFrames)
	samples = struct.unpack_from('%dh'%numberOfFrames,readAllTheFrames)
	for sample in samples:
		outRay.append(sample)
	return outRay

def buildFileSlow(fileName,firstChannel,secondChannel=''): #Turns input 'song' into .wav file.
	if not fileName.endswith('.wav'):
		fileName=fileName+'.wav'
	percent = 0
	output = wave.open(fileName, 'w')
	if type(secondChannel)==str:
		output.setparams((1, 2, sampleRate, 0, 'NONE', 'not compressed'))	
		for moment in range(len(firstChannel)):
			if firstChannel[moment] > 32767:
				value = 32767
			elif firstChannel[moment] < -32767:
				value = -32767
			else:
				value = firstChannel[moment]
			packed_value = struct.pack('h', value)
			output.writeframes(packed_value)
			if moment%(int(len(firstChannel))/100.)==0:
				percent += 1
				print percent, '%', firstChannel[moment], fileName
		print fileName, 'is done'
		output.close()
	elif type(secondChannel)==list:
		output.setparams((2, 2, sampleRate, 0, 'NONE', 'not compressed'))
		durationAdjustedFirstChannel =[]
		durationAdjustedSecondChannel=[]
		##### The channels need to be the same length, otherwise there will be problems
		if len(firstChannel)!=len(secondChannel):
			##### If one channel is longer than the other, we create two new channels and fill them with the old ones, but fill in the end of the second one with silence
			if len(firstChannel)>len(secondChannel):
				for moment in range(len(secondChannel)):
					durationAdjustedFirstChannel.append(firstChannel[moment])
					durationAdjustedSecondChannel.append(secondChannel[moment])
				for moment in range(int(math.fabs(len(firstChannel)-len(secondChannel)))):
					durationAdjustedFirstChannel.append(firstChannel[moment+(len(firstChannel)-(int(math.fabs(len(firstChannel)-len(secondChannel)))))])
					durationAdjustedSecondChannel.append(0)
			else:
				for moment in range(len(firstChannel)):
					durationAdjustedFirstChannel.append(firstChannel[moment])
					durationAdjustedSecondChannel.append(secondChannel[moment])
				for moment in range(int(math.fabs(len(firstChannel)-len(secondChannel)))):
					durationAdjustedSecondChannel.append(secondChannel[moment+(len(secondChannel)-(int(math.fabs(len(firstChannel)-len(secondChannel)))))])
					durationAdjustedFirstChannel.append(0)
			##### Make sure the amplitudes of the channels are within the range 2 bytes
			for channel in [durationAdjustedFirstChannel,durationAdjustedSecondChannel]:
				for moment in range(len(channel)):
					if channel[moment] > 32767:
						channel[moment]=32767
					elif channel[moment] < -32767:
						channel[moment]=-32767
			##### Put the chanels in the file
			for moment in range(len(durationAdjustedFirstChannel)):
				packedValue = struct.pack('h', durationAdjustedFirstChannel[moment])
				output.writeframes(packedValue)
				packedValue = struct.pack('h', durationAdjustedSecondChannel[moment])
				output.writeframes(packedValue)
				if moment%(int(len(durationAdjustedFirstChannel))/100.)==0:
					percent += 1
					print percent, '%', durationAdjustedFirstChannel[moment], fileName
			print fileName, 'is done'
			output.close()
		else:
			for channel in [firstChannel,secondChannel]:
				for moment in range(len(channel)):
					if channel[moment] > 32767:
						channel[moment]=32767
					elif channel[moment] < -32767:
						channel[moment]=-32767
			##### Put the chanels in the file
			for moment in range(len(firstChannel)):
				packedValue = struct.pack('h', firstChannel[moment])
				output.writeframes(packedValue)
				packedValue = struct.pack('h', secondChannel[moment])
				output.writeframes(packedValue)
				if moment%(int(len(firstChannel))/100.)==0:
					percent += 1
					print percent, '%', firstChannel[moment], fileName
			print fileName, 'is done'
			output.close()

def buildFile(fileName,firstChannel,secondChannel=''): #Turns input 'song' into .wav file.
	if not fileName.endswith('.wav'):
		fileName=fileName+'.wav'
	percent = 0
	output = wave.open(fileName, 'w')
	if type(secondChannel)==str:
		output.setparams((1, 2, sampleRate, 0, 'NONE', 'not compressed'))	
		for moment in range(len(firstChannel)):
			if firstChannel[moment] > 32767:
				value = 32767
			elif firstChannel[moment] < -32767:
				value = -32767
			else:
				value = firstChannel[moment]
			packed_value = struct.pack('h', value)
			output.writeframesraw(packed_value)
			if moment%(int(len(firstChannel))/100.)==0:
				percent += 1
				print percent, '%', firstChannel[moment], fileName
		print fileName, 'is done'
		output.close()
	elif type(secondChannel)==list:
		output.setparams((2, 2, sampleRate, 0, 'NONE', 'not compressed'))
		durationAdjustedFirstChannel =[]
		durationAdjustedSecondChannel=[]
	##### The channels need to be the same length, otherwise there will be problems
		if len(firstChannel)!=len(secondChannel):
	##### If one channel is longer than the other, we create two new channels and fill them with the old ones, but fill in the end of the second one with silence
			if len(firstChannel)>len(secondChannel):
				for moment in range(len(secondChannel)):
					durationAdjustedFirstChannel.append(firstChannel[moment])
					durationAdjustedSecondChannel.append(secondChannel[moment])
				for moment in range(int(math.fabs(len(firstChannel)-len(secondChannel)))):
					durationAdjustedFirstChannel.append(firstChannel[moment+(len(firstChannel)-(int(math.fabs(len(firstChannel)-len(secondChannel)))))])
					durationAdjustedSecondChannel.append(0)
			else:
				for moment in range(len(firstChannel)):
					durationAdjustedFirstChannel.append(firstChannel[moment])
					durationAdjustedSecondChannel.append(secondChannel[moment])
				for moment in range(int(math.fabs(len(firstChannel)-len(secondChannel)))):
					durationAdjustedSecondChannel.append(secondChannel[moment+(len(secondChannel)-(int(math.fabs(len(firstChannel)-len(secondChannel)))))])
					durationAdjustedFirstChannel.append(0)
	##### Make sure the amplitudes of the channels are within the range 2 bytes
			for channel in [durationAdjustedFirstChannel,durationAdjustedSecondChannel]:
				for moment in range(len(channel)):
					if channel[moment] > 32767:
						channel[moment]=32767
					elif channel[moment] < -32767:
						channel[moment]=-32767
	##### Put the chanels in the file
			for moment in range(len(durationAdjustedFirstChannel)):
				packedValue = struct.pack('h', durationAdjustedFirstChannel[moment])
				output.writeframesraw(packedValue)
				packedValue = struct.pack('h', durationAdjustedSecondChannel[moment])
				output.writeframesraw(packedValue)
				if moment%(int(len(durationAdjustedFirstChannel))/100.)==0:
					percent += 1
					print percent, '%', durationAdjustedFirstChannel[moment], fileName
			print fileName, 'is done'
			output.close()
		else:
			for channel in [firstChannel,secondChannel]:
				for moment in range(len(channel)):
					if channel[moment] > 32767:
						channel[moment]=32767
					elif channel[moment] < -32767:
						channel[moment]=-32767
	##### Put the chanels in the file
			for moment in range(len(firstChannel)):
				packedValue = struct.pack('h', firstChannel[moment])
				output.writeframesraw(packedValue)
				packedValue = struct.pack('h', secondChannel[moment])
				output.writeframesraw(packedValue)
				if moment%(int(len(firstChannel))/100.)==0:
					percent += 1
					print percent, '%', firstChannel[moment], fileName
			print fileName, 'is done'
			output.close()


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
	return outRay

def fadeOut(durRay,beginning=0,ending=''):
	if type(ending)!=int or ending>len(durRay):
		ending=len(durRay)
	outRay=[]
	for time in range(len(durRay)):
		outRay.append(durRay[time])
	for time in range((ending-beginning)):
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

def standardDeviation(durRay):
	averageValue=0
	for index in range(len(durRay)):
		averageValue+=durRay[index]
	averageValue/=float(len(durRay))
	differences =[]
	for index in range(len(durRay)):
		differences.append((durRay[index]-averageValue)**2)
	differenceAverage=0
	for difference in (range(len(differences))):
		differenceAverage+=differences[difference]
	differenceAverage/=float(len(differences))
	return (differenceAverage)**(0.5)

def covariance(firstRay,seconRay):
	firstAve = 0
	seconAve = 0	
	if len(firstRay)==len(seconRay):
		for sample in range(len(firstRay)):
			firstAve+=firstRay[sample]
			seconAve+=seconRay[sample]
		firstAve/=float(len(firstRay))
		seconAve/=float(len(seconRay))
		variance = 0
		for sample in range(len(firstRay)):
			variance+=(firstRay[sample]-firstAve)*(seconRay[sample]-seconAve)
		variance*=(1/float((len(firstRay)-1)))
		return variance
	else:
		print 'Chadtech ERROR CODE 0: Array Arguments must be same length (and they arent)'

def correlation(firstRay,seconRay):
	return covariance(firstRay,seconRay)/(standardDeviation(firstRay)*standardDeviation(seconRay))

def transform(durRay,harmonic):
	fourierSummation = 0
	for moment in range(len(durRay)):
		fourierSummation += (durRay[harmonic]*(math.e**((2*math.pi*harmonic*moment)/len(durRay)))).real*44100
	return fourierSummation

def fastFourierTransform(durRay):
	length = len(durRay)
	if length <= 1:
		return durRay
	even = fastFourierTransform(durRay[0::2])
	odd = fastFourierTransform(durRay[0::1])


def fourierTransform(durRay,harmonic=''):
	if type(harmonic)==str:
		fourierray = []
		for harmonic in range(len(durRay)):
			fourierray.append(transform(durRay,harmonic))
		return fourierray
	elif type(harmonic)==int:
		return transform(durRay,harmonic)

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

def grainSynth(durRay,freqInc,grainLength,fade=True):
	grainLength=int(grainLength)
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
	if fade:
		for grain in range(len(grains)):
			if len(grains[grain]):
				if len(grains[grain])>30:
					grains[grain]=changeSpeed(grains[grain],freqInc)
					grains[grain]=fadeOut(grains[grain],beginning=(len(grains[grain])-30))
					grains[grain]=fadeIn(grains[grain],ending=30)
				else:
					grains[grain]=changeSpeed(grains[grain],freqInc)
					grains[grain]=fadeOut(grains[grain])
					grains[grain]=fadeIn(grains[grain])
	else:
		for grain in range(len(grains)):
			if len(grains[grain]):
				grains[grain]=changeSpeed(grains[grain],freqInc)
	outRay=[]
	for grain in grains:
		for moment in grain:
			outRay.append(moment)
	return outRay

def grainMake(durRay,freqInc,grainLength,grainRate,fade=True):
	grainLength=int(grainLength)
	grains=[]
	for time in range(len(durRay)/grainRate):
		grain = []
		spot = time*grainRate
		distance = 0
		while (len(durRay)-1)>(spot+distance) and distance<grainLength:
			grain.append(durRay[(time*grainRate)+distance])
			distance+=1
		grains.append(grain)
	if fade:
		for grain in range(len(grains)):
			if len(grains[grain]):
				if len(grains[grain])>30:
					grains[grain]=changeSpeed(grains[grain],freqInc)
					grains[grain]=fadeOut(grains[grain],beginning=(len(grains[grain])-30))
					grains[grain]=fadeIn(grains[grain],ending=30)
				else:
					grains[grain]=changeSpeed(grains[grain],freqInc)
					grains[grain]=fadeOut(grains[grain])
					grains[grain]=fadeIn(grains[grain])
	else:
		for grain in range(len(grains)):
			if len(grains[grain]):
				grains[grain]=changeSpeed(grains[grain],freqInc)
	outRay=[]
	for time in [0]*len(durRay):
		outRay.append(0.)
	for grainIndex in range(len(grains)):
		for moment in range(len(grains[grainIndex])):
			outRay[(grainIndex*grainRate)+moment]+=grains[grainIndex][moment]
	return outRay

def grabGrain(durRay,beginning,end):
	return durRay[beginning:end]

def countEveryZero(durRay,zero=0):
	numberOfZeroes=0
	for element in durRay:
		if math.fabs(element)<=zero:
			numberOfZeroes+=1
	return numberOfZeroes

def cutUpEveryGrain(durRay,amplitudeThreshold):
	grains=[]
	beginning=0
	ending=''
	for moment in range(1,len(durRay)):
		if math.fabs(durRay[moment])<=amplitudeThreshold:
			ending=moment
			grains.append(durRay[beginning:ending])
			beginning=moment
	return grains

def grabSample(durRay,sampleLength):
	sampleLength=int(sampleLength)
	outRay=[]
	if sampleLength<len(durRay):
		whichPart = random.randint(0,len(durRay)-sampleLength)
	for moment in range(sampleLength):
		outRay.append(durRay[whichPart+moment])
	return outRay

def pixelate0(durRay,fileName):
	width = 1000
	heigh = 750
	wavImage = Image.new('RGB',(width,heigh),(0,0,0))
	for moment in range(len(durRay)):
		value = durRay[moment]+32767
		first, secon, third,fourt, fifth = 0,0,0,0,0
		first+=value%16
		secon+=(value/16)%16
		third+=(value/256)%16
		fourt+=(value/4096)%16
		wavImage.putpixel((moment%width,moment/width),(0,(fourt*16)+third,(secon*16)+first))
	wavImage.save(fileName+'.PNG','png')

def pixelate1(durRay,fileName):
	values = []
	for moment in range(len(durRay)):
		sampleValue = durRay[moment]+32767
		first, secon, third,fourt, fifth = 0,0,0,0,0
		first+=sampleValue%16
		secon+=(sampleValue/16)%16
		third+=(sampleValue/256)%16
		fourt+=(sampleValue/4096)%16
		values.append(first)
		values.append(secon)
		values.append(third)
		values.append(fourt)
	width = 1000
	heigh = 750
	wavImage = Image.new('RGB',(width,heigh),(0,0,0))
	pixel=0
	for value in range(len(values)):
		if value%6==0:
			redDatum,greenDatum,blueDatum = 0,0,0
			redDatum+=values[value]*16
		elif value%6==1:
			redDatum+=values[value]
		elif value%6==2:
			greenDatum+=values[value]*16
		elif value%6==3:
			greenDatum+=values[value]
		elif value%6==4:
			blueDatum+=values[value]*16
		elif value%6==5:
			blueDatum+=values[value]
			wavImage.putpixel((pixel%width,pixel/width),(redDatum,greenDatum,blueDatum))
			pixel+=1
	wavImage.putpixel((pixel%width,pixel/width),(redDatum,greenDatum,blueDatum))
	wavImage.save(fileName+'.PNG','png')

def waviate(imageFile):
	score = Image.open(imageFile)
	width,heigh = score.size
	pixelValueArray = []
	for pixel in range((width*heigh)-1):
		redDatum,greenDatum,blueDatum = score.getpixel((pixel%width,pixel/width))
		pixelValueArray.append(redDatum/16)
		pixelValueArray.append(redDatum%16)
		pixelValueArray.append(greenDatum/16)
		pixelValueArray.append(greenDatum%16)
		pixelValueArray.append(blueDatum/16)
		pixelValueArray.append(blueDatum%16)
	sample=0
	sampleValues = []
	for value in range(len(pixelValueArray)):
		if value%4==0:
			sample=0
			sample+=pixelValueArray[value]
		elif value%4==1:
			sample+=pixelValueArray[value]*16
		elif value%4==2:
			sample+=pixelValueArray[value]*256
		elif value%4==3:
			sample+=pixelValueArray[value]*4096
			sampleValues.append(sample)
	for moment in range(len(sampleValues)):
		sampleValues[moment]=sampleValues[moment]-32767
	return sampleValues

def reverbBackPass(durRay,dK):
	manyRays=[]
	delays=[1116,1188,1356,1277,1422,1491,1617,1557]
	for time in 8*[0]:
		manyRays.append([])
		for sample in range(len(durRay)):
			manyRays[len(manyRays)-1].append(durRay[sample])
	for array in range(len(manyRays)):
		for extraSpace in delays[array]*[0]:
			manyRays[array].append(0)
		manyRays[array].append(0)
		for moment in range(len(durRay)):
			manyRays[array][moment+delays[array]]+=manyRays[array][moment]*dK
	outRay=[0]*(max(delays)+len(durRay)+1)
	for array in range(len(manyRays)):
		for moment in range(len(manyRays[array])):
			outRay[moment]+=manyRays[array][moment]/float(len(manyRays))
	return outRay

def reverbForwardPass(durRay):


def reverb(durRay,dK,passes):
	for time in [0]*passes:
		durRay=reverbPass(durRay,dK)
	return durRay

def intoTxt(txtName,wavToOpen):
	durRay=openFile(wavToOpen)
	wavTxt = open(txtName,'w')
	for moment in durRay:
		wavTxt.write(str(moment)+'\n')
	wavTxt.close()

def declip(durRay,margin=30):
	return fadeIn(fadeOut(durRay,len(durRay)-margin,len(durRay)),0,margin)


