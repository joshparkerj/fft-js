'''
This file uses fft to compress a wav file.

The first command line argument is the name of the file to compress.
The second is the window size for the fft (should be a power of 2).
The third is the desired signal to noise ratio in decibels.

Usage example:
python compress.py sound.wav 1024 30

'''
from numpy import fft
import wave
import sys
import pickle
import struct

wave_file = wave.open(sys.argv[1],'rb')
wf = struct.unpack('{n}h'.format(n=wave_file.getnframes()),
                   wave_file.readframes(wave_file.getnframes()))
wfparams = wave_file.getparams()
wave_file.close()

i = 0
dft = []
window = int(sys.argv[2])
sn = float(sys.argv[3])
while i < len(wf) - window:
 dft.append(fft.fft(wf[i:i+window]).tolist())
 i += window

compdft = []
for i in range(len(dft)):
 compdft.append([])
 for j in range(len(dft[i])):
  if abs(dft[i][j]) > max([abs(x) for x in dft[i]]) / 10**(sn/10):
   compdft[i].append([j,dft[i][j]])

output = {'params': wfparams, 'window': window, 'data': compdft}
   
with open(sys.argv[1] + '.fft','wb') as file:
 pickle.dump(output,file)
