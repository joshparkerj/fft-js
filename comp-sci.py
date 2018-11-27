'''
Another attempt to compress wavefile data using fft.

First argument: name of wave file.
Second argument: window size (power of 2, please).
Third argument: number of sin functions to save for each window.

Usage example:
python comp-sci.py sound.wav 1024 16
'''
import numpy as np
from scipy.io import wavfile
import sys
import pickle

rate, data = wavfile.read(sys.argv[1])
window = int(sys.argv[2])
sincount = int(sys.argv[3])
i = 0
dfts = []
while i + window < len(data)//2:
 dfts.append(np.fft.fft(data[i:i+window]))
 i += window
dfts_with_indices = []
for i in range(len(dfts)):
 dfts_with_indices.append([])
 for j in range(len(dfts[i])):
  dfts_with_indices[i].append([j,dfts[i][j]])
 dfts_with_indices[i].sort(key=lambda e: abs(e[1]),reverse=True)
 dfts_with_indices[i] = dfts_with_indices[i][0:sincount]
output = {'rate': rate, 'data': dfts_with_indices, 'window': window}
with open(sys.argv[1] + '.fft','wb') as file:
 pickle.dump(output,file)
