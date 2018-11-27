'''
this file will generate a sin function.
The purpose is to test fft codes.

The first command line argument is the filename to write to.
The second is the length of the list to write.
The third is the wavelength of the sin function.

Usage example:
python sin-json.py data.json 2048 128
'''
from math import sin
from math import pi
import json
import sys

freq = 2*pi/float(sys.argv[3])

with open(sys.argv[1],'w') as file:
 json.dump([sin(freq*i) for i in range(int(sys.argv[2]))],file)
