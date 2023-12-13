#!/usr/bin/node
// a class Rectangle that defines a rectangle

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || typeof w !== 'number' || typeof h !== 'number') {
      return;
    }

    this.width = w;
    this.height = h;
  }

  // instance method print()
  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  // an instance method that exchanges the width and the height of the rectangle
  rotate () {
    this.tmp = this.width;
    this.width = this.height;
    this.height = this.tmp;
  }

  // an instance method that multiples the width and the height of the rectangle by 2
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
