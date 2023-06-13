#!/usr/bin/node

function add(a, b)
{
	return (Number(a) + Number(b));
}

const argument = process.argv;
a = argument[2];
b = argument[3];
console.log(add(a, b));
