/* Josh Parker 11/7/2018 UVU CS 3310 */

/* Let's attempt to implement the Cooley-Tukey FFT algorithm using javascript */
/* (a divide and conquer algorithm for the discrete Fourier transform) */

/* Also, let's count the basic operations */

/* 
usage example: 
node fft-bo.js data.json freq.json
*/


const fs = require('fs');
const IN = require(`./${process.argv[2]}`);
const Complex = require('./complex').Complex;

let BO = 0;

function fft(signal){
	const N = signal.length;
	const N2 = Math.floor(N/2);
	if (N === 1) {
		return [new Complex(signal[0],0)];
	}
	const freqs = fft(signal.filter((e,i) => i%2===0))
		.concat(fft(signal.filter((e,i) => i%2===1)));
	for (let i = 0; i < N2; i++){
		const t = freqs[i];
		const Ok = freqs[i+N2];
    /* This addition/subtraction looks like the basic operation to me */
    BO++;
		freqs[i] = t.add(Complex.eulers(-2 * Math.PI * i / N).multiply(Ok));
    /* Counting it twice since it does almost the same thing twice in a row */
    BO++;
		freqs[i+N2] = t.subtract(Complex.eulers(-2 * Math.PI * i / N).multiply(Ok));
	}
	return freqs;
}

const output = fft(IN);

console.log(`The length of the input was ${IN.length}`);
console.log(`${BO} basic operations were performed`);
console.log(`${IN.length * Math.log2(IN.length) / BO} is the constant factor`);


fs.writeFile(
 `./${process.argv[3]}`,
 JSON.stringify(output.map(e => e.magnitude())),
 err => console.error(err));
