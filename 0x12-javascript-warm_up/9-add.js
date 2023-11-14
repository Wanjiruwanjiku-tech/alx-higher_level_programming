#!/usr/bin/node
// the script prints the addition of two integers
// define a function
function add(a, b){
	return a + b;
}
const arg1 = process.argv[2];
const arg2 = process.argv[3];
if (arg1 !== undefined && arg2 !== undefined){
	const num1 = parseInt(arg1);
	const num2 = parseInt(arg2);
	if (!isNaN(num1) && !isNaN(num2)){
		const result = add(num1, num2);
		console.log(result);
	} else {
		return NaN;
	}
}
