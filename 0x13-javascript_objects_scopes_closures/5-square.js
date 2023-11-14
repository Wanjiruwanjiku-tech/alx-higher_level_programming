#!/usr/bin/node
// The script runs a class that extends from another class

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
	constructor (size) {
		super(size, size);
	}
}
module.exports = Square;
