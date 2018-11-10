ECHO OFF
REM This tests the fft function's basic operations
REM The argument is the highest power of 2 to be tested.
REM Usage example: bo-tester.bat 18
SET /A a=1
SETLOCAL ENABLEDELAYEDEXPANSION
FOR /L %%A IN (0,1,%1) DO (
 python sin-json.py data!a!.json !a!
 node fft-bo.js data!a!.json freq!a!.json
 SET /A a=a*2
)
