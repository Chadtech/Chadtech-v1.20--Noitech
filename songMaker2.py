execfile('Noitechbase.py')

sampleRate = 44100.
amp = 32767
oneSec = 1000.
noteDiv = 12
barNum = 4
noteDur = 550 # time length of note in thousandths of a second
noteCou = 4 #Number of notes per bar
percent = 0
speedOfSound = 340.49/sampleRate
songDur = (barNum*(noteDur/oneSec))*sampleRate
fileName = ''

theSong=makeSong(48)
THtwT=makeTone(THtw*4,4)
THtwT=volProf(THtwT,[(10.,1000.,1,0),(1000.,0.,0.2,3.8)])

THtwTL=makeTone(THtw*4,8)
THtwTL=volProf(THtwTL,[(10.,1000.,4,0),(1000.,0.,0.2,7.8)])
THtwTL=creatMany(THtwTL,10,10)
THtwTL=cutOff(THtwTL,332)
THtwTL=volDrop(THtwTL,33.)

FIfoT=makeTone(FIfo*8,4)
FIfoT=volProf(FIfoT,[(10.,1000.,1,0),(1000.,0.,0.2,3.8)])
FIfoT=creatMany(FIfoT,10,10)
FIfoT=cutOff(FIfoT,773)
FIfoT=volDrop(FIfoT,33.)

ONonT=makeTone(ONon*2,8)
ONonT=cutOff(ONonT,773)
ONonT=volProf(ONonT,[(10.,1000.,4,0),(1000.,0.,0.2,7.8)])
ONonT=creatMany(ONonT,10,100)
ONonT=volDrop(ONonT,400.)

FIfoT=cutOff(FIfoT,773)

buildSong(0,THtwT,theSong)
buildSong(6,THtwTL,theSong)
buildSong(8,FIfoT,theSong)
buildSong(16,ONonT,theSong)
buildSong(20,THtwT,theSong)
buildSong(20,FIfoT,theSong)

volDrop(theSong,250.)

lChan = theSong
rChan = theSong

lChanZe = zethre(lChan,(4,4,2),(20,17,20))
rChanZe = zethre(rChan,(5,4,2),(20,17,20))

lChanon = onthre(lChan,(4,4,2),(20,17,20),(30,40,50),750,0,0,4)
rChanon = onthre(rChan,(5,4,2),(20,17,20),(30,40,50),750,0,0,4)

lChanon = volDrop(lChanon,250.)
rChanon = volDrop(rChanon,250.)

buildSong(0,lChanZe,lChanon)
buildSong(0,rChanZe,rChanon)


buildFile(lChanon)
buildFile(rChanon)