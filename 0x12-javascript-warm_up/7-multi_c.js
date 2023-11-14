#!/usr/bin/node
const arg = process.argv[2];
const myStr = 'C is fun';
const count = parseInt(arg);
if (!isNaN(count) && count !== null) {
  for (let i = 0; i < count; i++) {
    console.log(myStr);
  }
} else {
  console.log('Missing number of occurrences');
}
