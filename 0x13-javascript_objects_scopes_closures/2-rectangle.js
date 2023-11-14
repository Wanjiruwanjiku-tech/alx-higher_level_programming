#!/usr/bin/node
/*
 * the script create the class Rectangle
 * the constructor carries two parameters
 * if either parameter is <= 0 return an empty object
 */
class Rectangle {
  constructor (w, h) {
    // Check value status
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      return {};
    }
  }
}
module.exports = Rectangle;
