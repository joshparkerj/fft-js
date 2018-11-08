REM Usage example: comp-dfts.bat data freq
ECHO OFF
node get-dft.js %1.json %2-js.json
python get-dft.py %1.json %2-py.json
node compare-json.js %2-js.json %2-py.json
