'''
This file is uses Numpy's fft function so I have something to compare my 
"homebrew" javascript fft function to.

It measures the runtime.

The first argument is the data source file.
The second argument is the number of test iterations.

Usage example:
python time-dft.py data.json 10000
'''
from numpy import fft
from time import perf_counter
from math import log2
import sys
import json

data = []
with open(sys.argv[1]) as input:
 for line in input:
  data.append(line)
decoded_data = json.loads(data[0])

dft = []
start = perf_counter()
for i in range(int(sys.argv[2])):
 dft.append(fft.fft(decoded_data))
end = perf_counter()

print('****************Python Numpy FFT****************')
print(f"The length of the input was {len(decoded_data)}")
print(f"The runtime was {(1000*(end - start)):.2f}")
print(f"{(len(decoded_data)*log2(len(decoded_data))/(1000*(end-start))):.2f} is the constant factor")
print('************************************************')
