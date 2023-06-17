#!/usr/bin/node

const Square2 = require('./5-square.js');

class Square extends Square2 {
  charPrint (c) {
    let i = 0;
    let x = 0;
    if (c !== undefined) {
      for (i = 0; i < this.height; i++) {
        console.log('X'.repeat(this.width));
      }
    } else {
      for (x = 0; x < this.height; x++) {
        console.log('C'.repeat(this.width));
      }
    }
  }
}
module.exports = Square;
