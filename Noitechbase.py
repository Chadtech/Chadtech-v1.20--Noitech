import os
import math
import random
import struct
import wave
import PIL
from PIL import Image

#.............................TONES.....................vvv



#Tonic
ONon = 100.
# Group A, Tonic * 3/2 ^ n -------------------------------------------------------------------------
#3/2
THtw = 150.
#9/8
NIei = 112.5
#27/16
NITHeitw = 168.75
#Group B, ( 1 / Group A  ) * 2
#4/3
FOth = 133.333
#16/9
EITWni = 177.778
#32/27
EIFOnith = 118.519
#Group C, 5/4 * 3/2 ^ n ------------------------------------------------------------------------------
#5/4
FIfo = 125.
#15/8
FITHei = 187.5
#45/32
NIFIeifo = 140.625
#Group D, ( 1 / Group C ) * 2 
#8/5
EIfi = 160
#16/15
EITWfith = 106.667
#64/45
EIEInifi = 142.222
#Group E, 5/4 * 4/3 ^ n
#5/3
FIth = 166.667
#10/9
FITWni = 111.111
#Group F, (1 / Group E) * 2
#6/5
SIfi = 120.
#9/5
NIfi = 180.
#Group G, 7/4 * 3/2 ^ n -----------------------------------------------------------------------------------------
#7/4
SEfo = 175.
#21/16
SETHeitw = 131.25
#63/32
NISEeifo = 196.875
#Group H, ( 1 / Group G ) * 2
#8/7
EIse = 114.286
#32/21
EIFOseth = 152.381
#64/63
EIEInise = 101.587
#Group I, 7/4 * 4/3 ^ n
#7/6
SEsi = 116.667
#14/9
SETWni = 155.556
#Group J, ( 1 / Group J ) * 2
#12/7
SITWse = 171.429
#9/7
NIse = 128.571
#Group K, 7/5 * 3/2 ^ n --------------------------------------------------------------------------------------------
#7/5
SEfi = 140.
#21/20
SETHfifo = 105.
#Group L, ( 1 / Group K ) * 2
#10/7
FITWse = 142.857
#40/21
EIFIseth = 190.476
#Group M, 7/5 * 4/3 ^ n
#28/15
SEFOfith = 186.667
#Group N, ( 1 / Group M ) * 2
#15/14
FITHsetw = 107.143

panTohns = [ONon,THtw,NIei,FOth,EITWni,EIFOnith,FIfo,FITHei,NIFIeifo,EIfi,EITWfith,EIEInifi,FIth,FITWni,SIfi,NIfi,SEfo,SETHeitw,NISEeifo,EIse,EIFOseth,EIEInise,SEsi,SETWni,SITWse,NIse,SEfi,SETHfifo,FITWse,EIFIseth,SEFOfith,FITHsetw]

botTen = [EIEInise,SETHfifo,EITWfith,FITHsetw] 
topTen = [FITHei,EIFIseth,NISEeifo,SEFOfith]
tens = [botTen,topTen] #8 tenTohns

botMov = [FITWni,NIei,EIse,SEsi]
topMov = [SITWse,SEfo,EITWni,NIfi]
movs = [botMov,topMov] #8 movTohns

botEmo = [EIFOnith,SIfi,FIfo,NIse] 
topEmo = [SETWni,EIfi,FIth,NITHeitw]
emos = [botEmo,topEmo] # 8 emoTohns

botPow = [SETHeitw,FOth,SEfi,NIFIeifo]
topPow = [EIEInifi,FITWse,THtw,EIFOseth]
pows = [botPow,topPow] #8 powTohns



#.............................................................................................

sampleRate = 44100.
amp = 32767
oneSec = 1000.
noteDiv = 12
barNum = 4
noteDur = 6000 # time length of note in thousandths of a second
noteCou = 4 #Number of notes per bar
percent = 0
speedOfSound = 340.49/sampleRate
songDur = (barNum*(noteDur/oneSec))*sampleRate
fileName = ''

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


#------------------------------Tone making


def makeTone(tone,dur): #Returns an array of a given tone, for a certain duration
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
		#print (vapp%inTone)*(2*amp), vapp, inTone, vapp%inTone
		value = (amp - (((vapp*tone)%(sampleRate))/sampleRate)*amp) - (amp/2)
		#value = (-(2*amp)/math.pi)*math.atan(1/math.tan((vapp*math.pi)/inTone))
		values[vapp]=value
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

def makeTriangleEnHarmonic(tone,dur,harmNum): #Make a Triangle Wave with enharmonics
	values = []
	inTone = float(tone)/sampleRate
	inDur = int(float(dur)*(noteDur/oneSec)*(sampleRate))
	for yit in range(inDur):
		values.append(0.)
	for harmonic in range(harmNum):
		for vapp in range(len(values)):
			values[vapp]+= amp*((-1)**(harmonic))*(math.sin((1+harmonic*(0.0013))*vapp*2*math.pi*inTone*((harmonic*2)+1))/(((harmonic*2)+1)**2))
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
		outRay.append(0)
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
	print fileName, 'is done'
	noise_output.close()

#--------------------------------Effects

def creatMany(durRay,many,space):
	outRay = []
	orig = []
	for yit in range(len(outRay)):
		orig.append(durRay[yit])
		outRay.append(durRay[yit])
	for yit in range(many*space):
		outRay.append(0.)
		print 'THIS HAPPENED', len(outRay), len(orig)
	for vapp in range(many):
		for dukh in range(len(orig)):
			outRay[dukh+(vapp*space)]+=orig[dukh]
	return outRay

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

def cutOff(durRay,volCut):
	outRay = durRay
	volCut = (volCut/1000.)*amp
	for yit in range(len(outRay)):
		if outRay[yit] > volCut:
			outRay[yit]=volCut
		if outRay[yit] < (-1*volCut):
			outRay[yit]=(-1*volCut)
	return outRay

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
			#print dur, whereAt, yit, whereAt+yit, len(inRay)
			inRay[whereAt+yit]=inRay[whereAt+yit]*(startVol+((endVol-startVol)/dur)*yit)
		for yit in range(len(inRay)-(whereAt+dur)):
			inRay[yit+dur]=inRay[yit+dur]*endVol
	return inRay

#def volProf(durRay,volProf):
#	inRay=durRay
#	for vapp in range(len(volProf)):
#		startVol, endVol, dur, whereAt = volProf[vapp]
#		whereAt = int(whereAt*(noteDur/oneSec)*sampleRate)
#		if dur==0:
#			dur = len(durRay)-whereAt
#		else:
#			dur = int(dur*(noteDur/oneSec)*sampleRate)
#		startVol = startVol/1000.
#		endVol = endVol/1000.
#		for yit in range(dur):
#			#print dur, whereAt, yit, whereAt+yit, len(inRay)
#			inRay[whereAt+yit]=inRay[whereAt+yit]*(startVol+((endVol-startVol)/dur)*yit)
#		for yit in range(len(inRay)-(whereAt+dur)):
#			inRay[yit+dur]=inRay[yit+dur]*endVol
#	return inRay



def volSlop(durRay,volSlop): # Add a volume slope to an array. The higher the volume slope, the slower the the array reaches volume zero, or even increases in volume.
	inRay = durRay
	volSlop = (volSlop/1000. + 999.)/1000.
	for vapp in range(len(durRay)):
		inRay[vapp] = inRay[vapp]*(volSlop**vapp)
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
	print 'ZETHRE COMPLETE'
	return outRay

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

def lopass(durRay,cutov):
	outRay = durRay
	for vapp in range(len(durRay)-1):
		outRay[vapp]=((outRay[vapp]+outRay[vapp+1])**(1+cutov/1000))/2
	return outRay