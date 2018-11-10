ECHO OFF
REM This runs the scripts for generating periodic data then comparing dfts.
REM The argument sets the length of the data to be generated.
REM The results seem to be good when the length is a power of 2.
REM Usage example: comp-rand.bat 16
python sin-json.py data%1.json %1
comp-dfts.bat data%1 freq%1
