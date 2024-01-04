#!/usr/bin/node
// The script reads and prints the content of a file.

// Import the fs module from Node.js
import fs, { lstat } from 'fs';

const filePath = process.argv[2];
fs.readFile(filePath, 'utf-8', function(err, data) {
    if (err) {
        console.log(err);
    } else {
        console.log(data);
    }
});