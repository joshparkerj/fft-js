ECHO OFF
REM This plots the provided data series, then finds its dft and plots it.
REM The first argument is the data.
REM Usage example: gen-data-plot.bat data.json
node get-amp.js %1 dft-%1
python make-plot.py %1 %1.png
python make-plot.py dft-%1 dft-%1.png
