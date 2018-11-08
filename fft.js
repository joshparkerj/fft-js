/* Josh Parker 11/7/2018 UVU CS 3310 */

/* Let's attempt to implement the algorithm using javascript */

/* I probably could have found one, but I opted to roll my own complex class */
class Complex {
	constructor(real_component,imaginary_component){
		this.r = real_component;
		this.i = imaginary_component;
		this.add = op => {
			return new Complex(this.r + op.r, this.i + op.i);
		}
		this.subtract = op => {
			return new Complex(this.r - op.r, this.i - op.i);
		}
		this.multiply = op => {
			const coefficientiSquared = this.i * op.i;
			const coefficienti = this.i * op.r + this.r * op.i;
			const constant = this.r * op.r;
			return new Complex(constant - coefficientiSquared, coefficienti);
		}
		this.divide = op => {
			const conjugate = new Complex(op.r, -op.i);
			const complexDividend = this.multiply(conjugate);
			const realDivisor = op.multiply(conjugate);
			return new Complex(complexDividend.r / realDivisor.r, complexDividend.i / realDivisor.r);
		}
		this.view = () => {
			return `(${this.r}+${this.i}j)`;
		}
	}
}

/* Now, for the real reason I needed complex numbers: Euler's formula */
const eulers = x => {
	return new Complex(Math.cos(x),Math.sin(x));
}

/* Here's a function to make it more convenient to view the output of fft */
/* The formatting should match Python's complex number formatting. */
const printComplexArray = c => {
	for (let i = 0; i < c.length; i++){
		console.log(c[i].view());
	}
}

/* Last, but not least, the Cooley-Tukey FFT algorithm */
/* (a divide and conquer algorithm for the discrete Fourier transform) */
function fft(signal){
	const N = signal.length;
	const N2 = Math.floor(signal.length/2);
	if (N < 1){
		return "some kind of error";
	}
	if (N === 1) {
		const z = [];
		z.push(new Complex(signal[0],0));
		return z;
	}
	const freqs = fft(signal.filter((e,i) => i%2===0))
		.concat(fft(signal.filter((e,i) => i%2===1)));
	for (let i = 0; i < N2; i++){
		let t = freqs[i];
		let Ok = freqs[i+N2];
		freqs[i] = t.add(eulers(-2 * Math.PI * i / N).multiply(Ok));
		freqs[i+N2] = t.subtract(eulers(-2 * Math.PI * i / N).multiply(Ok));
	}
	return freqs;
}

module.exports = {
	fft: fft
}
