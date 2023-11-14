#!/usr/bin/node
const Square = require('./5-square');

class SquareWithCharPrint extends Square {
	constructor (size) {
		super(size);
	}

	charPrint(c) {
		// Check if c is undefined
		const myChar = c || 'X';
		for (let i = 0; i < this.size; i++) {
			console.log(myChar.repeat(this.size));
		}
	}
}
module.exports = SquareWithCharPrint;
