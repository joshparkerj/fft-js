/* Josh Parker 11/7/2018 UVU CS 3310 */

/* Let's attempt to implement the Cooley-Tukey FFT algorithm using javascript */
/* (a divide and conquer algorithm for the discrete Fourier transform) */

const Complex = require('./complex').Complex;

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

module.exports = {
	fft: fft
}
