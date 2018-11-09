'''
A file to create a very simple plot from json data

Usage Example:
python make-plot.py data.json plot.png
'''
import matplotlib.pyplot as plt
import json
import sys

data = []
with open(sys.argv[1]) as input:
 for line in input:
  data.append(line)
decoded_data = json.loads(data[0])

plt.plot(decoded_data)
plt.savefig(sys.argv[2])
