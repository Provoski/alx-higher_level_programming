#!/usr/bin/node

function factorial (number) {
  if (isNaN(number)) {
    return (1);
  }
  if (number === 0) {
    return (1);
  }
  return number * factorial(number - 1);
}

const argument = process.argv;
const number = parseInt(argument[2]);
console.log(factorial(number));
