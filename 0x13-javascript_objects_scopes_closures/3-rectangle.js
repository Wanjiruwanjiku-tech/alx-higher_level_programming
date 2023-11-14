#!/usr/bin/node
/*
 * The script creates a class Rectangle
 * for this script we are going to create an instance method
 */
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      return {};
    }
  }

  print () {
    // Check if the width and height are present
    if (this.width !== undefined && this.width !== undefined) {
      for (let i = 0; i < this.height; i++) {
        console.log('X'.repeat(this.width));
      }
    }
  }
}
module.exports = Rectangle;
