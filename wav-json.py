'''

This file generates a json file from a wave file.

Usage example:
python wav-json.py sound.wav sound-data.json

'''

import wave
import sys
import json

wave_file = wave.open(sys.argv[1],'rb')
with open(sys.argv[2],'w') as file:
 json.dump(list(wave_file.readframes(wave_file.getnframes())),file)

wave_file.close()
