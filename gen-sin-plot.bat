ECHO OFF
REM This generates and plots a sin wave, then finds and plots its dft.
REM The first argument is the length of the input.
REM The second argument is the length of the sin function.
REM Usage example: gen-sin-plot.bat 2048 128
python sin-json.py sin%1.%2.json %1 %2
node get-amp.js sin%1.%2.json fr-sin%1.%2.json
python make-plot.py sin%1.%2.json sin%1.%2.png
python make-plot.py fr-sin%1.%2.json dft-sin%1.%2.png
