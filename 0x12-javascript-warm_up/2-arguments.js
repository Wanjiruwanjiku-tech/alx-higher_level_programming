#!/usr/bin/node
// Using conditional statements

const numArgs = process.argv.length - 2;

if (numArgs === 0) {
  console.log('No Arguments');
} else if (numArgs === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
