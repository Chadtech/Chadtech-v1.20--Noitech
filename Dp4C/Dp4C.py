execfile('Noitech.py')

tones = [
1.0, #      1/1            0
1.05, #     21/20          1
1.11111, #  10/9           2
1.16667, #  7/6            3
1.2, #      6/5            4
1.25, #     5/4            5
1.28571, #  9/7            6
1.3125, #   21/16          7
1.42857, #  10/7           8
1.48148, #  40/27          9
1.55556, #  14/9           A
1.6, #      8/5            B
1.66667, #  5/3            C
1.71429, #  12/7           D
1.8, #      9/5            E
1.90476, #  15/8           F
]

note = {
	'0':tones[0],
	'1':tones[1],
	'2':tones[2],
	'3':tones[3],
	'4':tones[4],
	'5':tones[5],
	'6':tones[6],
	'7':tones[7],
	'8':tones[8],
	'9':tones[9],
	'A':tones[10],
	'B':tones[11],
	'C':tones[12],
	'D':tones[13],
	'E':tones[14],
	'F':tones[15]
}

basic = openFile('basic_sample.wav')

noteDur=300.

pieceDur = 200
v0 = makeEmptyArray(pieceDur)
v1 = makeEmptyArray(pieceDur)
v2 = makeEmptyArray(pieceDur)

#################################################################
#################################################################
### VOICE 0
#################################################################
#################################################################

beat = 0

v0Dur=0.6
v0Dec=400.
v0Vol=300.

v1Dur=0.6
v1Dec=400.
v1Vol=300.

v2Dur=0.6
v2Dec=400.
v2Vol=65.

#################### Part 0.0
####################
####################


AddTo(beat,grainSynth(basic,5/4.,400),v0,v0Vol)
AddTo(beat,changeSpeed(grainSynth(basic,5/1.,750),0.0675),v2,60.)
beat+=1

AddTo(beat,grainSynth(basic,5/4.,400),v0,v0Vol)
beat+=3
v0Vol+=100.

####################

AddTo(beat,grainSynth(basic,4/3.,400),v0,v0Vol)
beat+=1

AddTo(beat,grainSynth(basic,5/4.,400),v0,v0Vol)
beat+=3
v0Vol+=200.

AddTo(beat,grainSynth(basic,16/9.,400),v0,v0Vol)
beat+=1

AddTo(beat,grainSynth(basic,5/3.,400),v0,v0Vol)
beat+=1

AddTo(beat,grainSynth(basic,16/9.,400),v0,v0Vol)
beat+=1

AddTo(beat,grainSynth(basic,5/3.,400),v0,v0Vol)
beat+=3

####################

AddTo(beat,fadeOut(grainSynth(basic[0:len(basic)/3],4/3.,400)),v0,v0Vol)
AddTo(beat,changeSpeed(grainSynth(basic,4/1.,750),0.0675),v2,35.)
beat+=0.5

AddTo(beat,fadeOut(grainSynth(basic[0:len(basic)/3],5/4.,400)),v0,v0Vol)
beat+=0.5

AddTo(beat,fadeOut(grainSynth(basic[0:len(basic)/3],4/3.,400)),v0,v0Vol)
beat+=0.5

AddTo(beat,fadeOut(grainSynth(basic[0:len(basic)/3],5/4.,400)),v0,v0Vol)
beat+=0.5

####################

AddTo(beat,grainSynth(changeSpeed(basic[0:len(basic)],0.5),20/9.,400),v0,v0Vol)
beat+=2

AddTo(beat,grainSynth(changeSpeed(basic[0:len(basic)],0.5),4/1.,400),v1,v1Vol)
beat+=2
v1Vol+=100.

####################

AddTo(beat,grainSynth(changeSpeed(basic[0:len(basic)/3],0.5),3/1.,400),v0,v0Vol)
AddTo(beat,grainSynth(changeSpeed(basic[0:len(basic)],0.5),40/9.,400),v1,v1Vol)
AddTo(beat,changeSpeed(grainSynth(basic,4/1.,750),0.0675),v2,35.)
beat+=1

AddTo(beat,grainSynth(changeSpeed(basic[0:len(basic)/3],0.5),45/16.,400),v0,v0Vol)
beat+=1

AddTo(beat,grainSynth(changeSpeed(basic[0:len(basic)/3],0.5),3/1.,400),v0,v0Vol)
AddTo(beat,grainSynth(changeSpeed(basic[0:len(basic)],0.5),4/1.,400),v1,v1Vol)
beat+=1
v1Vol+=200.

AddTo(beat,grainSynth(changeSpeed(basic[0:len(basic)/3],0.5),45/16.,400),v0,v0Vol)
beat+=1

####################

AddTo(beat,fadeOut(grainSynth(basic[0:len(basic)/3],5/4.,400)),v0,v0Vol)

AddTo(beat,grainSynth(basic[0:len(basic)/3],45/32.,400),v0,v0Vol)
AddTo(beat,grainSynth(basic[0:len(basic)/3],20/9.,400),v1,v1Vol)
beat+=0.5

AddTo(beat,grainSynth(basic[0:len(basic)/3],4/3.,400),v0,v0Vol)
beat+=0.5

AddTo(beat,grainSynth(basic[0:len(basic)/3],45/32.,400),v0,v0Vol)
AddTo(beat,grainSynth(basic[0:len(basic)/3],2/1.,400),v1,v1Vol)
beat+=0.5

AddTo(beat,grainSynth(basic[0:len(basic)/3],4/3.,400),v0,v0Vol)
AddTo(beat,grainSynth(basic[0:len(basic)/3],20/9.,400),v1,v1Vol)
beat+=0.5
v0Vol-=100

####################

AddTo(beat,grainSynth(changeSpeed(basic[0:len(basic)],0.25),5/2.,400),v0,v0Vol)
AddTo(beat,grainSynth(basic[0:len(basic)/3],15/8.,400),v1,v1Vol)
beat+=0.5
v0Vol-=200

#AddTo(beat,grainSynth(changeSpeed(basic[0:len(basic)],0.5),10/9.,400),v0,v0Vol)
AddTo(beat,grainSynth(basic[0:len(basic)/3],2/1.,400),v1,v1Vol)
beat+=0.5

#AddTo(beat,grainSynth(changeSpeed(basic[0:len(basic)],0.5),5/4.,400),v0,v0Vol)
AddTo(beat,grainSynth(basic[0:len(basic)/3],20/9.,400),v1,v1Vol)
beat+=0.5

AddTo(beat,grainSynth(basic[0:len(basic)/3],2/1.,400),v1,v1Vol)
beat+=0.5

####################


AddTo(beat,grainSynth(changeSpeed(basic[0:len(basic)],0.25),15/2.,400),v1,v1Vol)
beat+=4

####################

v0Dur=0.6
v0Dec=400.
v0Vol=300.

v1Dur=0.6
v1Dec=400.
v1Vol=300.

v2Dur=0.6
v2Dec=400.
v2Vol=65.

#################### Part 0.0
####################
####################


AddTo(beat,grainSynth(basic,5/4.,400),v0,v0Vol)
beat+=1

AddTo(beat,grainSynth(basic,5/4.,400),v0,v0Vol)
beat+=3
v0Vol+=100.

####################

AddTo(beat,grainSynth(basic,4/3.,400),v0,v0Vol)
beat+=1

AddTo(beat,grainSynth(basic,5/4.,400),v0,v0Vol)
beat+=2
v0Vol+=200.

AddTo(beat,grainSynth(basic,5/3.,400),v0,v0Vol/2)
beat+=1

####################

AddTo(beat,grainSynth(basic,16/9.,400),v0,v0Vol)
beat+=1

AddTo(beat,grainSynth(basic,5/3.,400),v0,v0Vol)
beat+=1

AddTo(beat,grainSynth(basic,16/9.,400),v0,v0Vol)
beat+=1

AddTo(beat,grainSynth(basic,5/3.,400),v0,v0Vol/2)
beat+=1

####################

AddTo(beat,grainSynth(basic,16/9.,400),v0,v0Vol/3)
beat+=1

AddTo(beat,grainSynth(basic,5/3.,400),v0,v0Vol/3)
beat+=1

AddTo(beat,fadeOut(grainSynth(basic[0:int(len(basic)/1.5)],4/3.,400)),v0,v0Vol)
beat+=1

AddTo(beat,fadeOut(grainSynth(basic[0:int(len(basic)/1.5)],5/4.,400)),v0,v0Vol)
beat+=1

####################

AddTo(beat,grainSynth(changeSpeed(basic[0:len(basic)],0.5),20/9.,400),v0,v0Vol)
beat+=2

AddTo(beat,grainSynth(changeSpeed(basic[0:len(basic)],0.5),4/1.,400),v1,v1Vol)
beat+=2
v1Vol+=100.

####################

AddTo(beat,grainSynth(changeSpeed(basic[0:len(basic)/3],0.5),3/1.,400),v0,v0Vol)
AddTo(beat,grainSynth(changeSpeed(basic[0:len(basic)],0.5),40/9.,400),v1,v1Vol)
AddTo(beat,changeSpeed(grainSynth(basic,4/1.,750),0.0675),v2,35.)
beat+=1

AddTo(beat,grainSynth(changeSpeed(basic[0:len(basic)/3],0.5),45/16.,400),v0,v0Vol)
beat+=1

AddTo(beat,grainSynth(changeSpeed(basic[0:len(basic)/3],0.5),3/1.,400),v0,v0Vol)
AddTo(beat,grainSynth(changeSpeed(basic[0:len(basic)],0.5),4/1.,400),v1,v1Vol)
beat+=1
v1Vol+=200.

AddTo(beat,grainSynth(changeSpeed(basic[0:len(basic)/3],0.5),45/16.,400),v0,v0Vol)
beat+=1

####################

AddTo(beat,fadeOut(grainSynth(basic[0:len(basic)/3],5/4.,400)),v0,v0Vol)

AddTo(beat,grainSynth(basic[0:int(len(basic)/1.5)],45/32.,400),v0,v0Vol)
AddTo(beat,grainSynth(basic[0:int(len(basic)/1.5)],20/9.,400),v1,v1Vol)
beat+=1

AddTo(beat,grainSynth(basic[0:int(len(basic)/1.5)],45/32.,400),v0,v0Vol)
AddTo(beat,grainSynth(basic[0:int(len(basic)/1.5)],2/1.,400),v1,v1Vol)
beat+=1

v0Vol-=100

####################

AddTo(beat,grainSynth(changeSpeed(basic[0:len(basic)],0.25),5/2.,400),v0,v0Vol)
AddTo(beat,grainSynth(basic[0:int(len(basic)/1.5)],15/8.,400),v1,v1Vol)
beat+=1
v0Vol-=200

#AddTo(beat,grainSynth(changeSpeed(basic[0:len(basic)],0.5),5/4.,400),v0,v0Vol)
AddTo(beat,grainSynth(basic[0:len(basic)/3],20/9.,400),v1,v1Vol)
beat+=0.5

AddTo(beat,grainSynth(basic[0:len(basic)/3],2/1.,400),v1,v1Vol)
beat+=0.5

####################


AddTo(beat,grainSynth(changeSpeed(basic[0:len(basic)],0.25),20/3.,400),v1,v1Vol)
beat+=4

####################
beat+4
####################

AddTo(beat,grainSynth(basic,5/3.,400),v0,v0Vol)
beat+=1
AddTo(beat,grainSynth(basic,8/5.,400),v0,v0Vol)
beat+=1
AddTo(beat,grainSynth(basic,5/3.,400),v0,v0Vol)
beat+=1
AddTo(beat,grainSynth(basic,8/5.,400),v0,v0Vol)
beat+=1
AddTo(beat,grainSynth(basic,45/32.,400),v0,v0Vol)
beat+=1

####################

AddTo(beat,grainSynth(basic,5/3.,400),v0,v0Vol)
beat+=1
AddTo(beat,grainSynth(basic,8/5.,400),v0,v0Vol)
beat+=1
AddTo(beat,grainSynth(basic,5/3.,400),v0,v0Vol)
beat+=1
AddTo(beat,grainSynth(basic,8/5.,400),v0,v0Vol)
beat+=1
AddTo(beat,grainSynth(basic,45/32.,400),v0,v0Vol)
beat+=1

####################

AddTo(beat,grainSynth(basic,5/3.,400),v0,v0Vol)
AddTo(beat,grainSynth(basic,45/16.,400),v1,v1Vol)
beat+=1
AddTo(beat,grainSynth(basic,8/5.,400),v0,v0Vol)
AddTo(beat,grainSynth(basic,5/2.,400),v1,v1Vol)
beat+=1
AddTo(beat,grainSynth(basic,5/3.,400),v0,v0Vol)
AddTo(beat,grainSynth(basic,45/16.,400),v1,v1Vol)
beat+=1
AddTo(beat,grainSynth(basic,8/5.,400),v0,v0Vol)
AddTo(beat,grainSynth(basic,5/2.,400),v1,v1Vol)
beat+=1
AddTo(beat,grainSynth(basic,45/32.,400),v0,v0Vol)
AddTo(beat,grainSynth(changeSpeed(basic,0.5),5/1.,400),v1,v1Vol)
beat+=1

####################

AddTo(beat,grainSynth(basic,5/3.,400),v0,v0Vol)
beat+=1
AddTo(beat,grainSynth(basic,8/5.,400),v0,v0Vol)
beat+=1
AddTo(beat,grainSynth(basic,5/3.,400),v0,v0Vol)
beat+=1
AddTo(beat,grainSynth(basic,8/5.,400),v0,v0Vol)
beat+=1
AddTo(beat,grainSynth(basic,45/32.,400),v0,v0Vol)
beat+=1

####################

AddTo(beat,grainSynth(basic,5/3.,400),v0,v0Vol)
AddTo(beat,grainSynth(basic,45/16.,400),v1,v1Vol)
beat+=1
AddTo(beat,grainSynth(basic,8/5.,400),v0,v0Vol)
AddTo(beat,grainSynth(basic,5/2.,400),v1,v1Vol)
beat+=1
AddTo(beat,grainSynth(basic,5/3.,400),v0,v0Vol)
AddTo(beat,grainSynth(basic,45/16.,400),v1,v1Vol)
beat+=1
AddTo(beat,grainSynth(basic,8/5.,400),v0,v0Vol)
AddTo(beat,grainSynth(basic,5/2.,400),v1,v1Vol)
beat+=1
AddTo(beat,grainSynth(basic,45/32.,400),v0,v0Vol)
AddTo(beat,grainSynth(changeSpeed(basic,0.5),5/1.,400),v1,v1Vol)
beat+=1

####################

AddTo(beat,grainSynth(basic,5/3.,400),v0,v0Vol)
beat+=1
AddTo(beat,grainSynth(basic,8/5.,400),v0,v0Vol)
AddTo(beat,grainSynth(basic,45/16.,400),v1,v1Vol)
beat+=1
AddTo(beat,grainSynth(basic,5/3.,400),v0,v0Vol)
AddTo(beat,grainSynth(basic,5/2.,400),v1,v1Vol)
beat+=1
AddTo(beat,grainSynth(basic,8/5.,400),v0,v0Vol)
AddTo(beat,grainSynth(basic,45/16.,400),v1,v1Vol)
beat+=1
AddTo(beat,grainSynth(basic,45/32.,400),v0,v0Vol)
AddTo(beat,grainSynth(basic,5/2.,400),v1,v1Vol)
beat+=1

####################

AddTo(beat,grainSynth(basic,5/3.,400),v0,v0Vol)
AddTo(beat,grainSynth(basic,12/5.,400),v1,v1Vol)
beat+=1
AddTo(beat,grainSynth(basic,8/5.,400),v0,v0Vol)
AddTo(beat,grainSynth(basic,5/2.,400),v1,v1Vol)
beat+=1
AddTo(beat,grainSynth(basic,5/3.,400),v0,v0Vol)
AddTo(beat,grainSynth(basic,12/5.,400),v1,v1Vol)
beat+=1
AddTo(beat,grainSynth(basic,8/5.,400),v0,v0Vol)
AddTo(beat,grainSynth(basic,5/2.,400),v1,v1Vol)
beat+=1
AddTo(beat,grainSynth(basic,45/32.,400),v0,v0Vol)
AddTo(beat,grainSynth(basic,20/9.,400),v1,v1Vol)
beat+=1

####################

AddTo(beat,grainSynth(basic,5/3.,400),v0,v0Vol)
AddTo(beat,grainSynth(basic,5/2.,400),v1,v1Vol)
beat+=1
AddTo(beat,grainSynth(basic,8/5.,400),v0,v0Vol)
AddTo(beat,grainSynth(basic,12/5.,400),v1,v1Vol)
beat+=1
AddTo(beat,grainSynth(basic,5/3.,400),v0,v0Vol)
AddTo(beat,grainSynth(basic,5/4.,400),v1,v1Vol)
beat+=1
AddTo(beat,grainSynth(basic,8/5.,400),v0,v0Vol)
AddTo(beat,grainSynth(basic,12/5.,400),v1,v1Vol)
beat+=1
AddTo(beat,grainSynth(basic,45/32.,400),v0,v0Vol)
AddTo(beat,grainSynth(basic,20/9.,400),v1,v1Vol)
beat+=1




buildFile(v0,'v0.wav')
buildFile(v1,'v1.wav')
#buildFile(v2,'v2.wav')
