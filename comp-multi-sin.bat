ECHO OFF
REM This runs the scripts for generating periodic data then comparing dfts.
REM The argument sets the length of the data to be generated.
REM The results seem to be good when the length is a power of 2.
REM The first number argument is the length of the input.
REM The second number argument is the number of sin functions to sum.
REM Usage example: comp-rand.bat 16 16
python multi-sin-json.py data%1.json %1 %2
comp-dfts.bat data%1 freq%1
