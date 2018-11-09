'''
this file will just generate some random test cases for the fft codes.

The first command line argument is the filename to write to.
The second is the length of the list to write.

Usage example:
python gen-json.py data.json 16
'''
import random
import json
import sys

with open(sys.argv[1],'w') as file:
 json.dump([random.random() for i in range(int(sys.argv[2]))],file)
