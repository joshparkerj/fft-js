/* 
usage example: 
node get-dft.js ./data.json ./freq.json
*/

const fs = require('fs');
const fft = require('./fft');
const input = require(process.argv[2]);

fs.writeFile(process.argv[3],JSON.stringify(fft.fft(input).map(e => e.view())),err => console.error(err));
