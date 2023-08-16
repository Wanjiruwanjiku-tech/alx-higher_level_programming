#!/usr/bin/node
/*
 * The class defines a rectangle.
 * In this task we are creating an instance method
 * called print() that prints the rectangle using the
 * character 'X'
 */

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print (c = 'X') {
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}
module.exports = Rectangle;
