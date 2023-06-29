#!/usr/bin/node

exports.logMe = function (...item) {
  this.counter = this.counter || 0;
  for (const i of item) {
    console.log(this.counter + ':'  + item);
    this.counter++;
  }
}
