#!/usr/bin/node

const argument = process.argv;
if (Number(argument[2]))
{
	console.log('My number: ' + argument[2]);
}
else
	console.log('Not a number');
