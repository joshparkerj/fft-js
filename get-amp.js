/* 
Instead of getting the dft, this file uses the dft to get the amplitude by frequency.

usage example: 
node get-amp.js data.json amp.json
*/

const fs = require('fs');
const fft = require('./fft').fft;
const input = require(`./${process.argv[2]}`);

fs.writeFile(`./${process.argv[3]}`,JSON.stringify(fft(input).map(e => e.magnitude())),err => console.error(err));
