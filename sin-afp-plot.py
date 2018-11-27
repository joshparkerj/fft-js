'''
this file will generate a more sophisticated sin function.
The purpose is to test fft codes.
Tryna figure out how to retrieve the amplitude, frequency, and phase shift.

The first command line argument is the filename to write to.
The second is the length of the list to write.
The third is the amplitude of the sin function.
The fourth is the frequency of the sin function.
The fifth is the phase shift of the sin function.

Usage example:
python sin-afp-plot.py data.json 10000 2 50 0.01 
'''
from numpy import fft
import matplotlib.pyplot as plt
from math import sin
from math import pi
from cmath import phase
import sys
import json

amp = float(sys.argv[3])
freq = float(sys.argv[4])/2/pi
ps = float(sys.argv[5])

original = [amp * sin(freq*(i+ps)) for i in range(int(sys.argv[2]))]
dft = fft.fft(original).tolist()

dft_interpreted = [{'frequency': i, 
                    'amplitude': abs(dft[i]), 
                    'phase': phase(dft[i])}
                    for i in range(len(dft)//2)]

med_amp = max([x['amplitude'] for x in dft_interpreted])

di_filtered = filter(lambda x: x['amplitude'] >= med_amp, dft_interpreted)

with open(sys.argv[1],'w') as file:
 json.dump(original,file)

for i in di_filtered:
 print(i)
