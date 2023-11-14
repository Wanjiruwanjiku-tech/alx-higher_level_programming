#!/usr/bin/node
// the script searches for the 2nd biggest integers in a string of args
const myArgs = process.argv.slice(2);

// convert args into integers
const numerals = myArgs.map(myArg => parseInt(myArg));

// filter out NaN values and store the remaining in desc order
const sortedNumbers = numerals.filter(num => !isNaN(num)).sort((a, b) => b - a);

// Print the second largest int or 0
console.log(sortedNumbers.length >= 2 ? sortedNumbers[1] : 0);
