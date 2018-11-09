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
      if (this.i >= 0){
        return `${this.r.toFixed(3)}+${this.i.toFixed(3)}j`;
      }
      return `${this.r.toFixed(3)}${this.i.toFixed(3)}j`;
		}
    this.magnitude = () => {
      return Math.sqrt(Math.pow(this.r,2)+Math.pow(this.i,2));
    }
    this.angle = () => {
      if(this.r > 0){
        return Math.atan(this.i/this.r);
      }
      if(this.r < 0 && this.i >= 0){
        return Math.atan(this.i/this.r) + Math.PI;
      }
      if(this.r < 0 && this.i < 0){
        return Math.atan(this.i/this.r) + Math.PI;
      }
      if(this.r === 0 && this.i > 0){
        return Math.PI / 2;
      }
      if(this.r === 0 && this.i < 0){
        return -Math.PI / 2;
      }
      return "indeterminate";
    }
	}
}

Complex.eulers = x => {
  return new Complex(Math.cos(x),Math.sin(x));
}

module.exports = {
  Complex: Complex
}
