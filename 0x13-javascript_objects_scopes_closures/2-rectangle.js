#!/usr/bin/node
/*
 * The class defines a rectangle.
 * if the values w and h are <= 0, An Empty
 * Object should be created
 */

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      Object.assign(this, {});
    }
  }
}
module.exports = Rectangle;
