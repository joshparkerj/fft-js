'''
Another attempt to decompress wavefile data using ifft.

First argument: name of binary pickle file.

Usage example:
python decomp-sci.py sound.wav.fft
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
dfts = []
dft = []
for i in range(len(data)):
 dfts.append([])
 for j in range(window):
  dfts[i].append(0+0j)
 for k in range(len(data[i])):
  dfts[i][data[i][k][0]] = data[i][k][1]
 dfts[i] += dfts[i][::-1]
 dft += np.fft.ifft(dfts[i]).tolist()
newdata = np.asarray(dft).astype(np.int16)
wavfile.write(sys.argv[1] + '.wav', rate, newdata)
