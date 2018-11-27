ECHO OFF
REM This generates and plots a sawtooth wave, then finds its dft and plots it.
REM The first argument is the length of the input.
REM The second argument is the wavelength of the saw function.
REM Usage example: gen-saw-plot.bat 2048 32
python saw-json.py saw%1.%2.json %1 %2
node get-amp.js saw%1.%2.json fr-saw%1.%2.json
python make-plot.py saw%1.%2.json saw%1.%2.png
python make-plot.py fr-saw%1.%2.json dft-saw%1.%2.png
