#!/usr/bin/node
const Square1 = require('./5-square');

class Square extends Square1 {
  // instance method that prints the rectangle using the character c
  charPrint (c) {
    if (c) {
      for (let i = 0; i < this.height; i++) {
        console.log(c.repeat(this.width));
      }
    } else {
      super.print();
    }
  }
}

module.exports = Square;
