#!/usr/bin/node

function add (a, b) {
  return (Number(a) + Number(b));
}

const argument = process.argv;
const a = argument[2];
const b = argument[3];
console.log(add(a, b));
