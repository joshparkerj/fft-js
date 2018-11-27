'''
Yet another attempt to decompress wavefile data using ifft.

First argument: name of binary pickle file.

Usage example:
python meandecomp.py sound.wav.fft
'''
import numpy as np
from scipy.io import wavfile
import sys
import pickle

with open(sys.argv[1],'rb') as file:
 x = pickle.load(file)
rate = x['rate']
data = x['data']
window = x['window']
cfactor = x['cfactor']
dfts = []
dft = []
for i in range(len(data)):
 dfts.append([])
 for j in range(window/cfactor):
  for k in range(cfactor):
   dfts[i].append(data[i][j])
 dft += np.fft.ifft(dfts[i]).tolist()
newdata = np.asarray(dft).astype(np.int16)
wavfile.write(sys.argv[1] + '.wav', rate, newdata)
