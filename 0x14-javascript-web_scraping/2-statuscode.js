#!/usr/bin/node

// The script displays the status code of a GET Request
// Import the required modules

const request = require('request');

// Store the url in question
const url = process.argv[2];

request(url, function (err, response) {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
