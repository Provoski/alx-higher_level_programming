#!/usr/bin/node

const list = process.argv;
const list_length = list.length;
let index = 2;
let i = 0;
let x = 0;
let max = -Infinity;
let secondmax = Infinity;

if (isNaN(list[2]))
{
	 console.log(0);
}
else
{
	for (index = 2; index < list_length; index++)
	{
		if (list[index] > max)
		{
			secondmax = max;
			max = list[index];
		}
		else if (list[index] > secondmax && list[index] < max)
		{
			secondmax = list[index];
		}
	}
	if (secondmax === -Infinity)
	{
		console.log(0);
	}
	else
		console.log(secondmax);
}
