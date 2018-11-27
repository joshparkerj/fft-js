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
python sin-afp-json.py data.json 10000 2 50 0.01 
'''
from math import sin
from math import pi
import json
import sys

amp = float(sys.argv[3])
freq = float(sys.argv[4])/2/pi
ps = float(sys.argv[5])

with open(sys.argv[1],'w') as file:
 json.dump([amp * sin(freq*(i+ps)) for i in range(int(sys.argv[2]))],file)
