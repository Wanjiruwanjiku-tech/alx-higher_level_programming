#!/usr/bin/node
/*
 * The classDefines a Square.
 * The class inherits from 5-square.js
 * In this task we are creating an insatnce method
 * charPrint() that prints a square using 'c'.
 * if undefined print using 'X'
 */
const mySquare = require('./5-square');

class Square extends mySquare {
  // Instance Method
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}
module.exports = Square;
