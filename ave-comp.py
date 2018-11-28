'''
Tuesday's attempt to compress wavefile data using fft.

First argument: name of wave file.
Second argument: percentage of data you want thrown out.

Usage example:
python ave-comp.py sound.wav 99
'''
import numpy as np
from scipy.io import wavfile
import sys
import pickle

rate, data = wavfile.read(sys.argv[1])
datalength = len(data)

dft = np.fft.fft(data).astype(np.complex64)
dft_cutoff = np.percentile(np.abs(dft), float(sys.argv[2]))
dft_highlights = []

for i,x in np.ndenumerate(dft):
 if abs(x) >= dft_cutoff:
  dft_highlights.append((i[0],x))

output = {'rate': rate, 'data': dft_highlights, 'length': datalength}
with open(sys.argv[1] + '.' + sys.argv[2] + '.fft','wb') as file:
 pickle.dump(output,file)
