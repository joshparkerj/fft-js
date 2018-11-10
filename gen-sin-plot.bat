ECHO OFF
REM This runs the scripts for generating dfts and compares the outputs.
REM Usage example: comp-dfts.bat data freq
python sin-json.py data%1.json %1
node get-amp.js data%1.json freq%1-js.json
python make-plot.py freq%1-js.json plot%1.png
