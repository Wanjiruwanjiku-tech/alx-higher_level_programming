#!/usr/bin/node
/*
 * The Class defines a Rectane.
 * For this task, in addition to the print() method,
 * we are adding two instance methods
 * The first is rotate() that exchanges w and h
 * The second is double() that double w and h
 */

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // Print instance Method
  print (c = 'X') {
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }

  // Rotate instance Method.
  rotate () {
    const tempVar = this.width;
    this.width = this.height;
    this.height = tempVar;
  }

  // Double Instance Method.
  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
