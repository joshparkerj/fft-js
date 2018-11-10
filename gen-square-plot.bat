ECHO OFF
REM This generates a square wave, finds its dft, and plots it.
REM The first argument is the length of the input.
REM The second argument is the length of the square function.
REM Usage example: gen-square-plot.bat 2048 32
python square-json.py sq%1.%2.json %1 %2
node get-amp.js sq%1.%2.json fr%1.%2.json
python make-plot.py fr%1.%2.json dft%1.%2.png
