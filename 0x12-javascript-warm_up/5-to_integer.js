#!/usr/bin/node

const arg = process.argv[2];
// Check if the arg is a number
if (!isNaN(arg)) {
  // if true convert it into an int
  const num = parseInt(arg);

  // check if sucessful and output txt
  if (!isNaN(num)) {
    console.log(`My number: ${num}`);
  } else {
    console.log('Not a number');
  }
} else {
  console.log('Not a number');
}
