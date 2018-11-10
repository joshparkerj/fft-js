/* 
Josh Parker 11/10/2018 UVU CS 3310

Let's attempt to implement the Cooley-Tukey FFT algorithm using javascript
(a divide and conquer algorithm for the discrete Fourier transform)

Also, let's time it

The first argument is the source data file.
The second argument is the number of times to iterate the test.

usage example: 
node fft-time.js data.json 10000
*/

const fs = require('fs');
const IN = require(`./${process.argv[2]}`);
const Complex = require('./complex').Complex;
const { performance } = require('perf_hooks');

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
		freqs[i] = t.add(Complex.eulers(-2 * Math.PI * i / N).multiply(Ok));
		freqs[i+N2] = t.subtract(Complex.eulers(-2 * Math.PI * i / N).multiply(Ok));
	}
	return freqs;
}
const output = [];
performance.mark('start');
for (let i = 0; i<process.argv[3]; i++){
  output.push(fft(IN));
}
performance.mark('end');
performance.measure('time', 'start', 'end');
const measure = performance.getEntriesByName('time')[0];
console.log('****************JavaScript FFT****************');
console.log(`The length of the input was ${IN.length}`);
console.log(`The run-time was ${measure.duration.toFixed(2)}`);
console.log(`${(IN.length * Math.log2(IN.length) / (measure.duration)).toFixed(2)} is the constant factor`);
console.log('**********************************************');
