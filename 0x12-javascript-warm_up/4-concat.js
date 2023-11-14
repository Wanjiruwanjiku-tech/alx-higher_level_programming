#!/usr/bin/node
// the script concatenates two command line args
const arg1 = process.argv[2];
const arg2 = process.argv[3];
// use placeholders to concatenate
console.log(`${arg1} is ${arg2}`);
