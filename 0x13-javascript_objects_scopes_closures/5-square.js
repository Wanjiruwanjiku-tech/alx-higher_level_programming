#!/usr/bin/node
/*
 * The Class defines a Square that inherits from
 * 4-rectangle.js
 * The Constructor takes one argument and the
 * constructor of rectangle must be called using
 * super()
 */
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}
module.exports = Square;
