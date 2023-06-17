#!/usr/bin/node

let i = 0;
const argument = process.argv;
const counter = argument[2];

if (!Number(argument[2])) {
  console.log('Missing size');
} else {
  while (i < counter) {
    console.log('X'.repeat(counter));
    i++;
  }
}
