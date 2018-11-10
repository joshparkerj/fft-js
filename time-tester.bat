ECHO OFF
REM This tests the fft function's run time vs. the numpy version
REM The first argument is the highest power of 2 to be tested.
REM The second argument is the number of times to iterate each test.
REM Usage example: time-tester.bat 18 10000
SET /A a=1
SETLOCAL ENABLEDELAYEDEXPANSION
FOR /L %%A IN (0,1,%1) DO (
 python sin-json.py data!a!.json !a!
 python time-dft.py data!a!.json %2
 node fft-time.js data!a!.json %2
 SET /A a=a*2
)
