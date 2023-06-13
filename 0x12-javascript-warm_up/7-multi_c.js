#!/usr/bin/node

let i = 0;
const argument = process.argv;
const counter = argument[2];

if (!Number(argument[2]))
{
	console.log('Missing number of occurrences');
}
else
{
	while (i < counter)
	{
		console.log('C is fun');
		i++;
	}
}
