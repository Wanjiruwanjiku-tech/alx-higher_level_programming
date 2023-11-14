#!/usr/bin/node
const arg = process.argv[2];
const parsedArg = parseInt(arg);
// use a conditional statement to determine data type of value
if (!isNaN(parsedArg)) {
  console.log(`My number: ${parsedArg}`);
} else {
  console.log('Not a number');
}
