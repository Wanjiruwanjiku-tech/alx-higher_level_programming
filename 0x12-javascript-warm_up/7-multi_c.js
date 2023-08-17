#!/usr/bin/node

const arg = process.argv[2];

if (!isNaN(arg)) {
  const numOccurrences = parseInt(arg);

  if (!isNaN(numOccurrences)) {
    let i;
    for (i = 0; i < numOccurrences; i++) {
      console.log('C is fun');
    }
  } else {
    console.log('Missing number of occurrences');
  }
} else {
  console.log('Missing number of occurrences');
}
