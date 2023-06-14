#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
      return (this.className);
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i = 0;
    for (i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const tempWidth = this.width;
    const tempHeight = this.height;
    this.width = tempHeight;
    this.height = tempWidth;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}
module.exports = Rectangle;
