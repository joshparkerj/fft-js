'''
this file will just generate some random test cases for the fft codes.

The first command line argument is the filename to write to.
The second is the length of the list to write.
The third is the number of sin functions.

Usage example:
python gen-json.py data.json 16 16
'''
from math import sin
import json
import sys

output = []

for i in range(int(sys.argv[2])):
 output.append(0)
 for j in range(int(sys.argv[3])):
  output[i] += sin((1+i)*(1+j))
  

with open(sys.argv[1],'w') as file:
 json.dump(output,file)
