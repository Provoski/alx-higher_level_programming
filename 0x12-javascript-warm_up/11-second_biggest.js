#!/usr/bin/node

const list = process.argv;
const listLength = list.length;
let index = 2;
let max = -Infinity;
let secondmax = Infinity;

if (isNaN(list[2])) {
  console.log(0);
} else {
  for (index = 2; index < listLength; index++) {
    if (list[index] > max) {
      secondmax = max;
      max = list[index];
    }
    if (list[index] > secondmax && list[index] < max) {
      secondmax = list[index];
    }
  }
  if (secondmax === -Infinity) {
    console.log(0);
  } else {
    console.log(secondmax);
  }
}
