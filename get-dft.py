'''
This file is uses Numpy's fft function so I have something to compare my 
"homebrew" javascript fft function to.

Usage example:
python get-dft.py data.json freq.json
'''
from numpy import fft
import json
import sys

def map_helper(e):
 if e.imag >= 0:
  return f"{e.real:.3f}+{e.imag:.3f}j"
 return f"{e.real:.3f}{e.imag:.3f}j"

data = []
with open(sys.argv[1]) as input:
 for line in input:
  data.append(line)
decoded_data = json.loads(data[0])
with open(sys.argv[2],'w') as output:
 json.dump(list(map(map_helper,fft.fft(decoded_data).tolist())),output)
