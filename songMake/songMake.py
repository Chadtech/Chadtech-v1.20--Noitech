print 'songMake Initialized'
execfile('Noitechbase.py')
print 'finished importing Noitechbase'

tones = [
1.0, #      1/1
1.05, #     21/20
1.11111, #  10/9
1.16667, #  7/6
1.2, #      6/5
1.25, #     5/4
1.28571, #  9/7
1.3125, #   21/16
1.42857, #  10/7
1.48148, #  40/27
1.55556, #  14/9
1.6, #      8/5
1.66667, #  5/3
1.71429, #  12/7
1.8, #      9/5
1.90476, #  15/8
]

note = {
	'0':tones[0]*400,
	'1':tones[1]*400,
	'2':tones[2]*400,
	'3':tones[3]*400,
	'4':tones[4]*400,
	'5':tones[5]*400,
	'6':tones[6]*400,
	'7':tones[7]*400,
	'8':tones[8]*400,
	'9':tones[9]*400,
	'A':tones[10]*400,
	'B':tones[11]*400,
	'C':tones[12]*400,
	'D':tones[13]*400,
	'E':tones[14]*400,
	'F':tones[15]*400
}

thisSongL = makeSong(400)
thisSongR = makeSong(400)
thisSong = makeSong(400)

snare = openFile('NP_snare.wav')
kick = openFile('NP_kick.wav')

##########################################################
##########################################################
## VOICE 0

beat = 0

v0Dur=0.75
v0Dec=750.
v0Vol=1000.

print 'channeled complete, composition commence'

while beat<40:

	buildSong(beat,volSlop(makeTone(note['C'],v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(note['8'],v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(note['5'],v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(note['5'],v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(note['5'],v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1

	buildSong(beat,volSlop(makeTone(note['C'],v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(note['8'],v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(note['5'],v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(note['5'],v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(note['5'],v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1

	buildSong(beat,volSlop(makeTone(note['C'],v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(note['8'],v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(note['5'],v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(note['5'],v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(note['5'],v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1

	buildSong(beat,volSlop(makeTone(note['C'],v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(note['8'],v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(note['C'],v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=3

while beat<80:

	buildSong(beat,volSlop(makeTone(note['F'],v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(note['9'],v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(note['8'],v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(note['8'],v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(note['8'],v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1

	buildSong(beat,volSlop(makeTone(note['F'],v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(note['9'],v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(note['F'],v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=3

	buildSong(beat,volSlop(makeTone(note['F'],v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(note['9'],v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(note['8'],v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(note['8'],v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(note['8'],v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1

	buildSong(beat,volSlop(makeTone(note['F'],v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=2
	buildSong(beat,volSlop(makeTone(note['9'],v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=2
	buildSong(beat,volSlop(makeTone(note['8'],v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1

while beat<120:

	buildSong(beat,volSlop(makeTone(note['0']*2,v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(note['0']*2,v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(note['2']*2,v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(note['0']*2,v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=2

	buildSong(beat,volSlop(makeTone(note['F'],v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(note['0']*2,v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=2
	buildSong(beat,volSlop(makeTone(note['2']*2,v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(note['0']*2,v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1

	buildSong(beat,volSlop(makeTone(note['F'],v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(note['0']*2,v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(note['2']*2,v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(note['0']*2,v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=2

	buildSong(beat,volSlop(makeTone(note['0']*2,v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(note['8'],v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(note['0']*2,v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=3

while beat<160:

	buildSong(beat,volSlop(makeTone(note['5']*2,v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(note['2']*2,v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(note['0']*2,v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(note['0']*2,v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(note['0']*2,v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1

	buildSong(beat,volSlop(makeTone(note['5']*2,v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(note['2']*2,v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(note['0']*2,v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(note['0']*2,v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(note['0']*2,v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1

	buildSong(beat,volSlop(makeTone(note['5']*2,v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(note['2']*2,v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(note['0']*2,v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(note['0']*2,v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(note['0']*2,v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1

	buildSong(beat,volSlop(makeTone(note['5']*2,v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(note['2']*2,v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(note['5']*2,v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=3

beat = 200

while beat<240:

	buildSong(beat,volSlop(makeTone(note['F']*2,v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=3
	buildSong(beat,volSlop(makeTone(note['9']*2,v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(note['8']*2,v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1

	buildSong(beat,volSlop(makeTone(note['F']*2,v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(note['9']*2,v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(note['F']*2,v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=3

	buildSong(beat,volSlop(makeTone(note['F']*2,v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=3
	buildSong(beat,volSlop(makeTone(note['9']*2,v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(note['8']*2,v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1

	buildSong(beat,volSlop(makeTone(note['F']*2,v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=2
	buildSong(beat,volSlop(makeTone(note['9']*2,v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=2
	buildSong(beat,volSlop(makeTone(note['8']*2,v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1

while beat<280:

	buildSong(beat,volSlop(makeTone(note['5']*4,v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=3
	buildSong(beat,volSlop(makeTone(note['2']*4,v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(note['0']*4,v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1

	buildSong(beat,volSlop(makeTone(note['5']*4,v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(note['2']*4,v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(note['0']*4,v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=3

	buildSong(beat,volSlop(makeTone(note['5']*4,v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=3
	buildSong(beat,volSlop(makeTone(note['2']*4,v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(note['0']*4,v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1

	buildSong(beat,volSlop(makeTone(note['5']*4,v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=2
	buildSong(beat,volSlop(makeTone(note['2']*4,v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=2
	buildSong(beat,volSlop(makeTone(note['0']*4,v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1

while beat<320:

	buildSong(beat,volSlop(makeTone(note['5']*4,v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=3
	buildSong(beat,volSlop(makeTone(note['2']*4,v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(note['0']*4,v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1

	buildSong(beat,volSlop(makeTone(note['5']*4,v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(note['2']*4,v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(note['0']*4,v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=3

	buildSong(beat,volSlop(makeTone(note['5']*4,v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=3
	buildSong(beat,volSlop(makeTone(note['2']*4,v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(note['0']*4,v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1

	buildSong(beat,volSlop(makeTone(note['5']*4,v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=2
	buildSong(beat,volSlop(makeTone(note['2']*4,v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=2
	buildSong(beat,volSlop(makeTone(note['0']*4,v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1

while beat<360:

	buildSong(beat,volSlop(makeTone(note['0']*4,v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=3
	buildSong(beat,volSlop(makeTone(note['0']*4,v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(note['0']*4,v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1

	buildSong(beat,volSlop(makeTone(note['0']*4,v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(note['0']*4,v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(note['0']*4,v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=3

	buildSong(beat,volSlop(makeTone(note['0']*4,v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=3
	buildSong(beat,volSlop(makeTone(note['0']*4,v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(note['0']*4,v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1

	buildSong(beat,volSlop(makeTone(note['0']*4,v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=2
	buildSong(beat,volSlop(makeTone(note['0']*4,v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=2
	buildSong(beat,volSlop(makeTone(note['0']*4,v0Dur),v0Dec),thisSongL,v0Vol)
	beat+=1

##########################################################
##########################################################
## VOICE 1

beat = 0
phaseOff = 0.17

v1Dur=0.75
v1Dec=750.
v1Vol=250.

while beat<40:

	buildSong(beat,volSlop(makeTone(2.013*note['5'],v1Dur),v1Dec),thisSongR,v1Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(2.013*note['8'],v1Dur),v1Dec),thisSongR,v1Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(2.013*note['C'],v1Dur),v1Dec),thisSongR,v1Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(2.013*note['C'],v1Dur),v1Dec),thisSongR,v1Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(2.013*note['C'],v1Dur),v1Dec),thisSongR,v1Vol)
	beat+=1

	buildSong(beat,volSlop(makeTone(2.013*note['5'],v1Dur),v1Dec),thisSongR,v1Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(2.013*note['8'],v1Dur),v1Dec),thisSongR,v1Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(2.013*note['C'],v1Dur),v1Dec),thisSongR,v1Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(2.013*note['C'],v1Dur),v1Dec),thisSongR,v1Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(2.013*note['C'],v1Dur),v1Dec),thisSongR,v1Vol)
	beat+=1

	buildSong(beat,volSlop(makeTone(2.013*note['5'],v1Dur),v1Dec),thisSongR,v1Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(2.013*note['8'],v1Dur),v1Dec),thisSongR,v1Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(2.013*note['C'],v1Dur),v1Dec),thisSongR,v1Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(2.013*note['C'],v1Dur),v1Dec),thisSongR,v1Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(2.013*note['C'],v1Dur),v1Dec),thisSongR,v1Vol)
	beat+=1

	buildSong(beat,volSlop(makeTone(2.013*note['5'],v1Dur),v1Dec),thisSongR,v1Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(2.013*note['8'],v1Dur),v1Dec),thisSongR,v1Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(2.013*note['5'],v1Dur),v1Dec),thisSongR,v1Vol)
	beat+=3

while beat<80:

	buildSong(beat,volSlop(makeTone(2.013*note['0'],v1Dur),v1Dec),thisSongR,v1Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(2.013*note['0'],v1Dur),v1Dec),thisSongR,v1Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(2.013*note['0'],v1Dur),v1Dec),thisSongR,v1Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(2.013*note['0'],v1Dur),v1Dec),thisSongR,v1Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(2.013*note['0'],v1Dur),v1Dec),thisSongR,v1Vol)
	beat+=1

	buildSong(beat,volSlop(makeTone(2.013*note['0'],v1Dur),v1Dec),thisSongR,v1Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(2.013*note['0'],v1Dur),v1Dec),thisSongR,v1Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(2.013*note['0'],v1Dur),v1Dec),thisSongR,v1Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(2.013*note['0'],v1Dur),v1Dec),thisSongR,v1Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(2.013*note['0'],v1Dur),v1Dec),thisSongR,v1Vol)
	beat+=1

	buildSong(beat,volSlop(makeTone(2.013*note['0'],v1Dur),v1Dec),thisSongR,v1Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(2.013*note['0'],v1Dur),v1Dec),thisSongR,v1Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(2.013*note['0'],v1Dur),v1Dec),thisSongR,v1Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(2.013*note['0'],v1Dur),v1Dec),thisSongR,v1Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(2.013*note['0'],v1Dur),v1Dec),thisSongR,v1Vol)
	beat+=1

	buildSong(beat,volSlop(makeTone(2.013*note['0'],v1Dur),v1Dec),thisSongR,v1Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(2.013*note['0'],v1Dur),v1Dec),thisSongR,v1Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(2.013*note['0'],v1Dur),v1Dec),thisSongR,v1Vol)
	beat+=3

while beat<120:

	buildSong(beat,volSlop(makeTone(2.013*note['0'],v1Dur),v1Dec),thisSongR,v1Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(2.013*note['9'],v1Dur),v1Dec),thisSongR,v1Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(2.013*note['9'],v1Dur),v1Dec),thisSongR,v1Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(2.013*note['9'],v1Dur),v1Dec),thisSongR,v1Vol)
	beat+=2

	buildSong(beat,volSlop(makeTone(2.013*note['9'],v1Dur),v1Dec),thisSongR,v1Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(2.013*note['0'],v1Dur),v1Dec),thisSongR,v1Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(2.013*note['0'],v1Dur),v1Dec),thisSongR,v1Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(2.013*note['0'],v1Dur),v1Dec),thisSongR,v1Vol)
	beat+=2

	buildSong(beat,volSlop(makeTone(2.013*note['9'],v1Dur),v1Dec),thisSongR,v1Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(2.013*note['0'],v1Dur),v1Dec),thisSongR,v1Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(2.013*note['0'],v1Dur),v1Dec),thisSongR,v1Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(2.013*note['0'],v1Dur),v1Dec),thisSongR,v1Vol)
	beat+=2

	buildSong(beat,volSlop(makeTone(2.013*note['0'],v1Dur),v1Dec),thisSongR,v1Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(2.013*note['0'],v1Dur),v1Dec),thisSongR,v1Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(2.013*note['0'],v1Dur),v1Dec),thisSongR,v1Vol)
	beat+=3

while beat<160:
	buildSong(beat,volSlop(makeTone(note['0']*2.013,v0Dur),v0Dec),thisSongR,v0Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(note['2']*2.013,v0Dur),v0Dec),thisSongR,v0Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(note['5']*2.013,v0Dur),v0Dec),thisSongR,v0Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(note['5']*2.013,v0Dur),v0Dec),thisSongR,v0Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(note['5']*2.013,v0Dur),v0Dec),thisSongR,v0Vol)
	beat+=1

	buildSong(beat,volSlop(makeTone(note['0']*2.013,v0Dur),v0Dec),thisSongR,v0Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(note['2']*2.013,v0Dur),v0Dec),thisSongR,v0Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(note['5']*2.013,v0Dur),v0Dec),thisSongR,v0Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(note['5']*2.013,v0Dur),v0Dec),thisSongR,v0Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(note['5']*2.013,v0Dur),v0Dec),thisSongR,v0Vol)
	beat+=1

	buildSong(beat,volSlop(makeTone(note['0']*2.013,v0Dur),v0Dec),thisSongR,v0Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(note['2']*2.013,v0Dur),v0Dec),thisSongR,v0Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(note['5']*2.013,v0Dur),v0Dec),thisSongR,v0Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(note['5']*2.013,v0Dur),v0Dec),thisSongR,v0Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(note['5']*2.013,v0Dur),v0Dec),thisSongR,v0Vol)
	beat+=1

	buildSong(beat,volSlop(makeTone(note['0']*2.013,v0Dur),v0Dec),thisSongR,v0Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(note['2']*2.013,v0Dur),v0Dec),thisSongR,v0Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(note['0']*2.013,v0Dur),v0Dec),thisSongR,v0Vol)
	beat+=3

beat = 200

while beat<240:

	buildSong(beat+((beat%10)*(1./4.)),volSlop(makeTone(note['8']*4,v1Dur),v1Dec),thisSongL,v1Vol)
	beat+=3
	buildSong(beat+((beat%10)*(1./4.)),volSlop(makeTone(note['9']*4,v1Dur),v1Dec),thisSongL,v1Vol)
	beat+=1
	buildSong(beat+((beat%10)*(1./4.)),volSlop(makeTone(note['9']*4,v1Dur),v1Dec),thisSongL,v1Vol)
	beat+=1

	buildSong(beat+((beat%10)*(1./4.)),volSlop(makeTone(note['8']*4,v1Dur),v1Dec),thisSongL,v1Vol)
	beat+=1
	buildSong(beat+((beat%10)*(1./4.)),volSlop(makeTone(note['8']*4,v1Dur),v1Dec),thisSongL,v1Vol)
	beat+=1
	buildSong(beat+((beat%10)*(1./4.)),volSlop(makeTone(note['8']*4,v1Dur),v1Dec),thisSongL,v1Vol)
	beat+=3

	buildSong(beat+((beat%10)*(1./4.)),volSlop(makeTone(note['8']*4,v1Dur),v1Dec),thisSongL,v1Vol)
	beat+=3
	buildSong(beat+((beat%10)*(1./4.)),volSlop(makeTone(note['9']*4,v1Dur),v1Dec),thisSongL,v1Vol)
	beat+=1
	buildSong(beat+((beat%10)*(1./4.)),volSlop(makeTone(note['9']*4,v1Dur),v1Dec),thisSongL,v1Vol)
	beat+=1

	buildSong(beat+((beat%10)*(1./4.)),volSlop(makeTone(note['8']*4,v1Dur),v1Dec),thisSongL,v1Vol)
	beat+=2
	buildSong(beat+((beat%10)*(1./4.)),volSlop(makeTone(note['8']*4,v1Dur),v1Dec),thisSongL,v1Vol)
	beat+=2
	buildSong(beat+((beat%10)*(1./4.)),volSlop(makeTone(note['8']*4,v1Dur),v1Dec),thisSongL,v1Vol)
	beat+=1

while beat<280:

	buildSong(beat+((beat%10)*(1./4.)),volSlop(makeTone(note['0']*8,v1Dur),v1Dec),thisSongL,v1Vol)
	beat+=3
	buildSong(beat+((beat%10)*(1./4.)),volSlop(makeTone(note['2']*8,v1Dur),v1Dec),thisSongL,v1Vol)
	beat+=1
	buildSong(beat+((beat%10)*(1./4.)),volSlop(makeTone(note['2']*8,v1Dur),v1Dec),thisSongL,v1Vol)
	beat+=1

	buildSong(beat+((beat%10)*(1./4.)),volSlop(makeTone(note['2']*8,v1Dur),v1Dec),thisSongL,v1Vol)
	beat+=1
	buildSong(beat+((beat%10)*(1./4.)),volSlop(makeTone(note['2']*8,v1Dur),v1Dec),thisSongL,v1Vol)
	beat+=1
	buildSong(beat+((beat%10)*(1./4.)),volSlop(makeTone(note['2']*8,v1Dur),v1Dec),thisSongL,v1Vol)
	beat+=3

	buildSong(beat+((beat%10)*(1./4.)),volSlop(makeTone(note['0']*8,v1Dur),v1Dec),thisSongL,v1Vol)
	beat+=3
	buildSong(beat+((beat%10)*(1./4.)),volSlop(makeTone(note['2']*8,v1Dur),v1Dec),thisSongL,v1Vol)
	beat+=1
	buildSong(beat+((beat%10)*(1./4.)),volSlop(makeTone(note['2']*8,v1Dur),v1Dec),thisSongL,v1Vol)
	beat+=1

	buildSong(beat+((beat%10)*(1./4.)),volSlop(makeTone(note['0']*8,v1Dur),v1Dec),thisSongL,v1Vol)
	beat+=2
	buildSong(beat+((beat%10)*(1./4.)),volSlop(makeTone(note['0']*8,v1Dur),v1Dec),thisSongL,v1Vol)
	beat+=2
	buildSong(beat+((beat%10)*(1./4.)),volSlop(makeTone(note['2']*8,v1Dur),v1Dec),thisSongL,v1Vol)
	beat+=1

while beat<320:

	buildSong(beat+((beat%10)*(1./4.)),volSlop(makeTone(note['0']*8,v1Dur),v1Dec),thisSongL,v1Vol)
	beat+=3
	buildSong(beat+((beat%10)*(1./4.)),volSlop(makeTone(note['5']*8,v1Dur),v1Dec),thisSongL,v1Vol)
	beat+=1
	buildSong(beat+((beat%10)*(1./4.)),volSlop(makeTone(note['5']*8,v1Dur),v1Dec),thisSongL,v1Vol)
	beat+=1

	buildSong(beat+((beat%10)*(1./4.)),volSlop(makeTone(note['0']*8,v1Dur),v1Dec),thisSongL,v1Vol)
	beat+=1
	buildSong(beat+((beat%10)*(1./4.)),volSlop(makeTone(note['5']*8,v1Dur),v1Dec),thisSongL,v1Vol)
	beat+=1
	buildSong(beat+((beat%10)*(1./4.)),volSlop(makeTone(note['5']*8,v1Dur),v1Dec),thisSongL,v1Vol)
	beat+=3

	buildSong(beat+((beat%10)*(1./4.)),volSlop(makeTone(note['5']*8,v1Dur),v1Dec),thisSongL,v1Vol)
	beat+=3
	buildSong(beat+((beat%10)*(1./4.)),volSlop(makeTone(note['0']*8,v1Dur),v1Dec),thisSongL,v1Vol)
	beat+=1
	buildSong(beat+((beat%10)*(1./4.)),volSlop(makeTone(note['5']*8,v1Dur),v1Dec),thisSongL,v1Vol)
	beat+=1

	buildSong(beat+((beat%10)*(1./4.)),volSlop(makeTone(note['5']*8,v1Dur),v1Dec),thisSongL,v1Vol)
	beat+=2
	buildSong(beat+((beat%10)*(1./4.)),volSlop(makeTone(note['0']*8,v1Dur),v1Dec),thisSongL,v1Vol)
	beat+=2
	buildSong(beat+((beat%10)*(1./4.)),volSlop(makeTone(note['0']*8,v1Dur),v1Dec),thisSongL,v1Vol)
	beat+=1

while beat<360:

	buildSong(beat+((beat%10)*(1./4.)),volSlop(makeTone(note['0']*8,v1Dur),v1Dec),thisSongL,v1Vol)
	beat+=3
	buildSong(beat+((beat%10)*(1./4.)),volSlop(makeTone(note['0']*8,v1Dur),v1Dec),thisSongL,v1Vol)
	beat+=1
	buildSong(beat+((beat%10)*(1./4.)),volSlop(makeTone(note['0']*8,v1Dur),v1Dec),thisSongL,v1Vol)
	beat+=1

	buildSong(beat+((beat%10)*(1./4.)),volSlop(makeTone(note['0']*8,v1Dur),v1Dec),thisSongL,v1Vol)
	beat+=1
	buildSong(beat+((beat%10)*(1./4.)),volSlop(makeTone(note['0']*8,v1Dur),v1Dec),thisSongL,v1Vol)
	beat+=1
	buildSong(beat+((beat%10)*(1./4.)),volSlop(makeTone(note['0']*8,v1Dur),v1Dec),thisSongL,v1Vol)
	beat+=3

	buildSong(beat+((beat%10)*(1./4.)),volSlop(makeTone(note['0']*8,v1Dur),v1Dec),thisSongL,v1Vol)
	beat+=3
	buildSong(beat+((beat%10)*(1./4.)),volSlop(makeTone(note['0']*8,v1Dur),v1Dec),thisSongL,v1Vol)
	beat+=1
	buildSong(beat+((beat%10)*(1./4.)),volSlop(makeTone(note['0']*8,v1Dur),v1Dec),thisSongL,v1Vol)
	beat+=1

	buildSong(beat+((beat%10)*(1./4.)),volSlop(makeTone(note['0']*8,v1Dur),v1Dec),thisSongL,v1Vol)
	beat+=2
	buildSong(beat+((beat%10)*(1./4.)),volSlop(makeTone(note['0']*8,v1Dur),v1Dec),thisSongL,v1Vol)
	beat+=2
	buildSong(beat+((beat%10)*(1./4.)),volSlop(makeTone(note['0']*8,v1Dur),v1Dec),thisSongL,v1Vol)
	beat+=1

########################################################################
########################################################################
########## DRUM 0

snare = openFile('NP_snare.wav')
kick = openFile('NP_kick.wav')

d0Vol = 1000.

beat = 0

while beat<40:

	buildSong(beat,kick,thisSong,d0Vol)
	beat+=0.66
	buildSong(beat,kick,thisSong,d0Vol)
	beat+=0.34
	buildSong(beat,snare,thisSong,d0Vol)
	beat+=3

	buildSong(beat,kick,thisSong,d0Vol)
	beat+=0.66
	buildSong(beat,kick,thisSong,d0Vol)
	beat+=0.34
	buildSong(beat,snare,thisSong,d0Vol)
	beat+=3

	buildSong(beat,kick,thisSong,d0Vol)
	beat+=2
	buildSong(beat,snare,thisSong,d0Vol)
	beat+=2

	buildSong(beat,kick,thisSong,d0Vol)
	beat+=0.66
	buildSong(beat,kick,thisSong,d0Vol)
	beat+=0.34
	buildSong(beat,snare,thisSong,d0Vol)
	beat+=3

	buildSong(beat,kick,thisSong,d0Vol)
	beat+=2
	buildSong(beat,snare,thisSong,d0Vol)
	beat+=2

while beat<80:

	buildSong(beat,kick,thisSong,d0Vol)
	beat+=0.66
	buildSong(beat,kick,thisSong,d0Vol)
	beat+=0.34
	buildSong(beat,snare,thisSong,d0Vol)
	beat+=3

	buildSong(beat,kick,thisSong,d0Vol)
	beat+=0.66
	buildSong(beat,kick,thisSong,d0Vol)
	beat+=0.34
	buildSong(beat,snare,thisSong,d0Vol)
	beat+=3

	buildSong(beat,kick,thisSong,d0Vol)
	beat+=2
	buildSong(beat,snare,thisSong,d0Vol)
	beat+=2

	buildSong(beat,kick,thisSong,d0Vol)
	beat+=0.66
	buildSong(beat,kick,thisSong,d0Vol)
	beat+=0.34
	buildSong(beat,snare,thisSong,d0Vol)
	beat+=3

	buildSong(beat,kick,thisSong,d0Vol)
	beat+=2
	buildSong(beat,snare,thisSong,d0Vol)
	beat+=2

while beat<120:

	buildSong(beat,kick,thisSong,d0Vol)
	beat+=2
	buildSong(beat,snare,thisSong,d0Vol)
	beat+=2

	buildSong(beat,kick,thisSong,d0Vol)
	beat+=2
	buildSong(beat,snare,thisSong,d0Vol)
	beat+=2

while beat<160:

	buildSong(beat,kick,thisSong,d0Vol)
	beat+=1
	buildSong(beat,kick,thisSong,d0Vol)
	beat+=1
	buildSong(beat,snare,thisSong,d0Vol)
	beat+=2

while beat<200:

	buildSong(beat,kick,thisSong,d0Vol)
	beat+=2
	buildSong(beat,snare,thisSong,d0Vol)
	beat+=2

beat = 240

while beat<320:

	buildSong(beat,kick,thisSong,d0Vol)
	beat+=2
	buildSong(beat,snare,thisSong,d0Vol)
	beat+=2

while beat<360:

	buildSong(beat,kick,thisSong,d0Vol)
	beat+=0.66
	buildSong(beat,kick,thisSong,d0Vol)
	beat+=0.34
	buildSong(beat,snare,thisSong,d0Vol)
	beat+=3

	buildSong(beat,kick,thisSong,d0Vol)
	beat+=0.66
	buildSong(beat,kick,thisSong,d0Vol)
	beat+=0.34
	buildSong(beat,snare,thisSong,d0Vol)
	beat+=3

	buildSong(beat,kick,thisSong,d0Vol)
	beat+=2
	buildSong(beat,snare,thisSong,d0Vol)
	beat+=2

	buildSong(beat,kick,thisSong,d0Vol)
	beat+=0.66
	buildSong(beat,kick,thisSong,d0Vol)
	beat+=0.34
	buildSong(beat,snare,thisSong,d0Vol)
	beat+=3

	buildSong(beat,kick,thisSong,d0Vol)
	beat+=2
	buildSong(beat,snare,thisSong,d0Vol)
	beat+=2

##########################################################
##########################################################
## VOICE 2

beat = 80
phaseOff = 0.17

v2Dur=4
v2Dec=950.
v2Vol=400.

octaveV2 = 0.24

while beat<120:

	buildSong(beat,volSlop(makeTone(octaveV2*note['2'],v2Dur),v2Dec),thisSong,v2Vol)
	beat+=2

	buildSong(beat,volSlop(makeTone((1./octaveV2)*note['2'],v2Dur),v2Dec),thisSong,v2Vol)
	beat+=3

octaveV2 = 0.12

while beat<160:

	buildSong(beat,volSlop(makeTone(octaveV2*note['C'],v2Dur*2),v2Dec+25),thisSong,v2Vol)
	beat+=3

	buildSong(beat,volSlop(makeTone((0.24/octaveV2)*note['C'],v2Dur),v2Dec),thisSong,v2Vol)
	beat+=2

while beat<200:

	buildSong(beat,volSlop(makeTone((0.24/octaveV2)*note['C'],v2Dur),v2Dec),thisSong,v2Vol)
	beat+=3

	buildSong(beat,volSlop(makeTone((0.24/octaveV2)*note['C'],v2Dur),v2Dec),thisSong,v2Vol)
	beat+=2

while beat<240:

	buildSong(beat,volSlop(makeTone(octaveV2*note['C'],v2Dur*2),v2Dec+25),thisSong,v2Vol)
	beat+=2

	buildSong(beat,volSlop(makeTone((0.24/octaveV2)*note['5'],v2Dur),v2Dec),thisSong,v2Vol/2)
	beat+=3

while beat<280:

	buildSong(beat,volSlop(makeTone(octaveV2*note['8'],v2Dur*2),v2Dec+25),thisSong,v2Vol)
	beat+=2

	buildSong(beat,volSlop(makeTone((0.24/octaveV2)*note['F'],v2Dur),v2Dec),thisSong,v2Vol/2)
	beat+=3

while beat<320:

	buildSong(beat,volSlop(makeTone(octaveV2*note['C'],v2Dur*2),v2Dec+25),thisSong,v2Vol)
	beat+=2

	buildSong(beat,volSlop(makeTone((0.12/octaveV2)*note['0'],v2Dur),v2Dec),thisSong,v2Vol/2)
	beat+=3

while beat<360:

	buildSong(beat,volSlop(makeTone(octaveV2*note['0'],v2Dur*2),v2Dec+25),thisSong,v2Vol)
	beat+=2

	buildSong(beat,volSlop(makeTone((0.12/octaveV2)*note['0'],v2Dur),v2Dec),thisSong,v2Vol/2)
	beat+=3

##########################################################
##########################################################
## VOICE 3

beat = 160
phaseOff = 0.17

v3Dur=0.75
v3Dec=750.
v3Vol=900.

while beat<200:

	buildSong(beat,volSlop(makeTone(1.013*note['C'],v3Dur),v3Dec),thisSongR,v3Vol)
	beat+=2.5
	buildSong(beat,volSlop(makeTone(0.513*note['8'],v3Dur),v3Dec),thisSongR,v3Vol)
	beat+=0.5
	buildSong(beat,volSlop(makeTone(0.513*note['5'],v3Dur),v3Dec),thisSongR,v3Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(1.013*note['C'],v3Dur),v3Dec),thisSongR,v3Vol)
	beat+=1

	buildSong(beat,volSlop(makeTone(1.013*note['C'],v3Dur),v3Dec),thisSongR,v3Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(1.013*note['C'],v3Dur),v3Dec),thisSongR,v3Vol)
	beat+=0.5
	buildSong(beat,volSlop(makeTone(0.513*note['8'],v3Dur),v3Dec),thisSongR,v3Vol)
	beat+=1.5
	buildSong(beat,volSlop(makeTone(1.013*note['C'],v3Dur),v3Dec),thisSongR,v3Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(0.513*note['5'],v3Dur),v3Dec),thisSongR,v3Vol)
	beat+=1

	buildSong(beat,volSlop(makeTone(1.013*note['C'],v3Dur),v3Dec),thisSongR,v3Vol)
	beat+=2.5
	buildSong(beat,volSlop(makeTone(0.513*note['8'],v3Dur),v3Dec),thisSongR,v3Vol)
	beat+=0.5
	buildSong(beat,volSlop(makeTone(0.513*note['5'],v3Dur),v3Dec),thisSongR,v3Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(1.013*note['C'],v3Dur),v3Dec),thisSongR,v3Vol)
	beat+=1

	buildSong(beat,volSlop(makeTone(1.013*note['C'],v3Dur),v3Dec),thisSongR,v3Vol)
	beat+=0.5
	buildSong(beat,volSlop(makeTone(0.513*note['8'],v3Dur),v3Dec),thisSongR,v3Vol)
	beat+=2.5
	buildSong(beat,volSlop(makeTone(0.513*note['5'],v3Dur),v3Dec),thisSongR,v3Vol)
	beat+=2

while beat<240:

	buildSong(beat,volSlop(makeTone(1.013*note['C'],v3Dur),v3Dec),thisSongR,v3Vol)
	beat+=2.5
	buildSong(beat,volSlop(makeTone(0.513*note['8'],v3Dur),v3Dec),thisSongR,v3Vol)
	beat+=0.5
	buildSong(beat,volSlop(makeTone(0.513*note['5'],v3Dur),v3Dec),thisSongR,v3Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(1.013*note['C'],v3Dur),v3Dec),thisSongR,v3Vol)
	beat+=1

	buildSong(beat,volSlop(makeTone(1.013*note['C'],v3Dur),v3Dec),thisSongR,v3Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(1.013*note['C'],v3Dur),v3Dec),thisSongR,v3Vol)
	beat+=0.5
	buildSong(beat,volSlop(makeTone(0.513*note['8'],v3Dur),v3Dec),thisSongR,v3Vol)
	beat+=1.5
	buildSong(beat,volSlop(makeTone(1.013*note['C'],v3Dur),v3Dec),thisSongR,v3Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(0.513*note['5'],v3Dur),v3Dec),thisSongR,v3Vol)
	beat+=1

	buildSong(beat,volSlop(makeTone(1.013*note['C'],v3Dur),v3Dec),thisSongR,v3Vol)
	beat+=2.5
	buildSong(beat,volSlop(makeTone(0.513*note['8'],v3Dur),v3Dec),thisSongR,v3Vol)
	beat+=0.5
	buildSong(beat,volSlop(makeTone(0.513*note['5'],v3Dur),v3Dec),thisSongR,v3Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(1.013*note['C'],v3Dur),v3Dec),thisSongR,v3Vol)
	beat+=1

	buildSong(beat,volSlop(makeTone(1.013*note['C'],v3Dur),v3Dec),thisSongR,v3Vol)
	beat+=0.5
	buildSong(beat,volSlop(makeTone(0.513*note['8'],v3Dur),v3Dec),thisSongR,v3Vol)
	beat+=2.5
	buildSong(beat,volSlop(makeTone(0.513*note['5'],v3Dur),v3Dec),thisSongR,v3Vol)
	beat+=2

while beat<280:

	buildSong(beat,volSlop(makeTone(1.013*note['C'],v3Dur),v3Dec),thisSongR,v3Vol)
	beat+=2.5
	buildSong(beat,volSlop(makeTone(0.513*note['8'],v3Dur),v3Dec),thisSongR,v3Vol)
	beat+=0.5
	buildSong(beat,volSlop(makeTone(0.513*note['5'],v3Dur),v3Dec),thisSongR,v3Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(1.013*note['C'],v3Dur),v3Dec),thisSongR,v3Vol)
	beat+=1

	buildSong(beat,volSlop(makeTone(1.013*note['C'],v3Dur),v3Dec),thisSongR,v3Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(1.013*note['C'],v3Dur),v3Dec),thisSongR,v3Vol)
	beat+=0.5
	buildSong(beat,volSlop(makeTone(0.513*note['8'],v3Dur),v3Dec),thisSongR,v3Vol)
	beat+=1.5
	buildSong(beat,volSlop(makeTone(1.013*note['C'],v3Dur),v3Dec),thisSongR,v3Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(0.513*note['5'],v3Dur),v3Dec),thisSongR,v3Vol)
	beat+=1

	buildSong(beat,volSlop(makeTone(1.013*note['C'],v3Dur),v3Dec),thisSongR,v3Vol)
	beat+=2.5
	buildSong(beat,volSlop(makeTone(0.513*note['8'],v3Dur),v3Dec),thisSongR,v3Vol)
	beat+=0.5
	buildSong(beat,volSlop(makeTone(0.513*note['5'],v3Dur),v3Dec),thisSongR,v3Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(1.013*note['C'],v3Dur),v3Dec),thisSongR,v3Vol)
	beat+=1

	buildSong(beat,volSlop(makeTone(1.013*note['C'],v3Dur),v3Dec),thisSongR,v3Vol)
	beat+=0.5
	buildSong(beat,volSlop(makeTone(0.513*note['8'],v3Dur),v3Dec),thisSongR,v3Vol)
	beat+=2.5
	buildSong(beat,volSlop(makeTone(0.513*note['5'],v3Dur),v3Dec),thisSongR,v3Vol)
	beat+=2

while beat<320:

	buildSong(beat,volSlop(makeTone(1.013*note['F'],v3Dur),v3Dec),thisSongR,v3Vol)
	beat+=2.5
	buildSong(beat,volSlop(makeTone(0.513*note['5'],v3Dur),v3Dec),thisSongR,v3Vol)
	beat+=0.5
	buildSong(beat,volSlop(makeTone(0.513*note['2'],v3Dur),v3Dec),thisSongR,v3Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(1.013*note['F'],v3Dur),v3Dec),thisSongR,v3Vol)
	beat+=1

	buildSong(beat,volSlop(makeTone(1.013*note['F'],v3Dur),v3Dec),thisSongR,v3Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(1.013*note['F'],v3Dur),v3Dec),thisSongR,v3Vol)
	beat+=0.5
	buildSong(beat,volSlop(makeTone(0.513*note['5'],v3Dur),v3Dec),thisSongR,v3Vol)
	beat+=1.5
	buildSong(beat,volSlop(makeTone(1.013*note['F'],v3Dur),v3Dec),thisSongR,v3Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(0.513*note['2'],v3Dur),v3Dec),thisSongR,v3Vol)
	beat+=1

	buildSong(beat,volSlop(makeTone(1.013*note['F'],v3Dur),v3Dec),thisSongR,v3Vol)
	beat+=2.5
	buildSong(beat,volSlop(makeTone(0.513*note['5'],v3Dur),v3Dec),thisSongR,v3Vol)
	beat+=0.5
	buildSong(beat,volSlop(makeTone(0.513*note['2'],v3Dur),v3Dec),thisSongR,v3Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(1.013*note['F'],v3Dur),v3Dec),thisSongR,v3Vol)
	beat+=1

	buildSong(beat,volSlop(makeTone(1.013*note['F'],v3Dur),v3Dec),thisSongR,v3Vol)
	beat+=0.5
	buildSong(beat,volSlop(makeTone(0.513*note['5'],v3Dur),v3Dec),thisSongR,v3Vol)
	beat+=2.5
	buildSong(beat,volSlop(makeTone(0.513*note['2'],v3Dur),v3Dec),thisSongR,v3Vol)
	beat+=2

while beat<360:

	buildSong(beat,volSlop(makeTone(1.013*note['0'],v3Dur),v3Dec),thisSongR,v3Vol)
	beat+=2.5
	buildSong(beat,volSlop(makeTone(0.513*note['0'],v3Dur),v3Dec),thisSongR,v3Vol)
	beat+=0.5
	buildSong(beat,volSlop(makeTone(0.513*note['0'],v3Dur),v3Dec),thisSongR,v3Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(1.013*note['0'],v3Dur),v3Dec),thisSongR,v3Vol)
	beat+=1

	buildSong(beat,volSlop(makeTone(1.013*note['0'],v3Dur),v3Dec),thisSongR,v3Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(1.013*note['0'],v3Dur),v3Dec),thisSongR,v3Vol)
	beat+=0.5
	buildSong(beat,volSlop(makeTone(0.513*note['0'],v3Dur),v3Dec),thisSongR,v3Vol)
	beat+=1.5
	buildSong(beat,volSlop(makeTone(1.013*note['0'],v3Dur),v3Dec),thisSongR,v3Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(0.513*note['0'],v3Dur),v3Dec),thisSongR,v3Vol)
	beat+=1

	buildSong(beat,volSlop(makeTone(1.013*note['0'],v3Dur),v3Dec),thisSongR,v3Vol)
	beat+=2.5
	buildSong(beat,volSlop(makeTone(0.513*note['0'],v3Dur),v3Dec),thisSongR,v3Vol)
	beat+=0.5
	buildSong(beat,volSlop(makeTone(0.513*note['0'],v3Dur),v3Dec),thisSongR,v3Vol)
	beat+=1
	buildSong(beat,volSlop(makeTone(1.013*note['0'],v3Dur),v3Dec),thisSongR,v3Vol)
	beat+=1

	buildSong(beat,volSlop(makeTone(1.013*note['0'],v3Dur),v3Dec),thisSongR,v3Vol)
	beat+=0.5
	buildSong(beat,volSlop(makeTone(0.513*note['0'],v3Dur),v3Dec),thisSongR,v3Vol)
	beat+=2.5
	buildSong(beat,volSlop(makeTone(0.513*note['0'],v3Dur),v3Dec),thisSongR,v3Vol)
	beat+=2

print 'finished composing, make wav files NOW'

buildFile(thisSongL,'llL.wav')
buildFile(thisSongR,'llR.wav')
buildFile(thisSong,'llC.wav')