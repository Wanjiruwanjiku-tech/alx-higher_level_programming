#!/usr/bin/node
const size = process.argv[2];
if (!isNaN(size) && size !== null) {
  const squareSize = parseInt(size);
  for (let i = 0; i < squareSize; i++) {
    let row = '';
    for (let j = 0; j < squareSize; j++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
