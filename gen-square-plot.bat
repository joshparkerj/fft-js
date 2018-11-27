ECHO OFF
REM This generates and plots a square wave, then finds and plots its dft.
REM The first argument is the length of the input.
REM The second argument is the length of the square function.
REM Usage example: gen-square-plot.bat 2048 32
python square-json.py sq%1.%2.json %1 %2
node get-amp.js sq%1.%2.json fr%1.%2.json
python make-plot.py sq%1.%2.json sq%1.%2.png
python make-plot.py fr%1.%2.json dft%1.%2.png
