'''
this file will just generate some periodic data for the fft codes.

The first command line argument is the filename to write to.
The second is the length of the list to write.
The third is the wavelength of the sawtooth wave

Usage example:
python saw-json.py data.json 2048 32
'''
from math import sin
import json
import sys

def sawtooth(index,wavelength=int(sys.argv[3]),amplitude=1,offset=0):
 return (index + offset)%wavelength - wavelength/2

with open(sys.argv[1],'w') as file:
 json.dump([sawtooth(i) for i in range(int(sys.argv[2]))],file)
