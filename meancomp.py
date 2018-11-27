'''
Yet another attempt to compress wavefile data using fft.

First argument: name of wave file.
Second argument: window size (power of 2, please).
Third argument: compression factor (another power of 2, probably).

Usage example:
python meancomp.py sound.wav 1024 16
'''
import numpy as np
from scipy.io import wavfile
from statistics import mean
import sys
import pickle

rate, data = wavfile.read(sys.argv[1])
window = int(sys.argv[2])
cfactor = int(sys.argv[3])
i = 0
dfts = []
while i + window < len(data)//2:
 dfts.append(np.fft.fft(data[i:i+window]))
 i += window
mean_dfts = []
for i in range(len(dfts)):
 for j in range(0,len(dfts[i]),cfactor):
  mean_dfts.append(mean([x.real for x in dfts[i][j:j+cfactor]]))
output = {'rate': rate, 'data': mean_dfts, 'window': window,'cfactor': cfactor}
with open(sys.argv[1] + '.fft','wb') as file:
 pickle.dump(output,file)
