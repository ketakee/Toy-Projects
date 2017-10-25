# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 18:19:48 2016

@author: Ketakee Nimavat
"""
import scipy.io.wavfile
import scipy
import contextlib
import wave

from matplotlib import pyplot as plt
rate1m, data1m = scipy.io.wavfile.read('D:\\Speech-Text-Speech\\male\\_male_voice_goodbye_sound_effect.wav')
rate2m,data2m=scipy.io.wavfile.read('D:\\Speech-Text-Speech\\female\\_female_voice_goodbye_sound_effect.wav')
print rate1m, rate2m
print data1m,data2m
plt.plot(data1m,color='r')
plt.plot(data2m)
plt.show()


fname = 'D:\\Speech-Text-Speech\\male\\_male_voice_hi_sound_effect.wav'
with contextlib.closing(wave.open(fname,'r')) as f:
    frames = f.getnframes()
    rate = f.getframerate()
    duration = frames / float(rate)
    print(duration)

#male
lst=[]
for l in data1m:
     lst=lst + [l[1],]
zcr=0
for i in range(len(lst)-1):
    if lst[i+1]==0:
        continue
    elif lst[i]==0 :
        zcr+=1
    elif (lst[i]<0 and lst[i+1]>0) or (lst[i]>0 and lst[i+1]<0):
        zcr+=1
    else:
        continue

print zcr/duration


#female
fname = 'D:\\Speech-Text-Speech\\female\\_female_voice_good_evening_sound_effect.wav'
with contextlib.closing(wave.open(fname,'r')) as f:
    frames = f.getnframes()
    rate = f.getframerate()
    duration = frames / float(rate)
    print(duration)


#Zero Crossing Rate
lstf=[]
for l in data2m:
     lstf=lstf + [l[1],]
zcrf=0
for i in range(len(lstf)-1):
    if lstf[i+1]==0:
        continue
    elif lstf[i]==0 :
        zcrf+=1
    elif (lstf[i]<0 and lstf[i+1]>0) or (lstf[i]>0 and lstf[i+1]<0):
        zcrf+=1
    else:
        continue
        
print zcrf/duration


print "/*****************************************************************/"
#
#rate1m, data1m = scipy.io.wavfile.read('D:\\Speech-Text-Speech\\female\\_female_voice_good_evening_sound_effect.wav')
#rate2m,data2m=scipy.io.wavfile.read('D:\\Speech-Text-Speech\\female\\_female_voice_goodbye_sound_effect.wav')
#print rate1m, rate2m
#print data1m,data2m
#z=plt.plot(data1m)
#plt.show()
#y=plt.plot(data2m)
#plt.show()
