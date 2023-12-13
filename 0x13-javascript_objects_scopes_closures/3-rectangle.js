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
}

module.exports = Rectangle;
