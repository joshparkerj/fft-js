'''
Tuesday's attempt to decompress wavefile data using fft.

First argument: name of compressed file.

Usage example:
python ave-decomp.py sound.wav.fft
'''
import numpy as np
from scipy.io import wavfile
import sys
import pickle

with open(sys.argv[1],'rb') as file:
 x = pickle.load(file)

dft = [0+0j for i in range(x['length'])]
for datum in x['data']:
 dft[datum[0]] = datum[1]

newdata = np.fft.ifft(dft).astype(np.int16)
wavfile.write(sys.argv[1] + '.wav', x['rate'], newdata)
