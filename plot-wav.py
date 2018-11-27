'''
This file takes a wave file and plots the original samples and the dft.

Usage example:
python plot-wav.py sound.wav

'''
from numpy import fft
import matplotlib.pyplot as plt
import wave
import sys

wave_file = wave.open(sys.argv[1],'rb')
wf = list(wave_file.readframes(wave_file.getnframes()))
wave_file.close()

plt.plot(wf)
plt.savefig(sys.argv[1] + '-original.png')

plt.plot([abs(x) for x in fft.fft(wf).tolist()])
plt.savefig(sys.argv[1] + '-dft.png')
