#!/usr/bin/node

// The script prints the number of episodes where
// the character 'Wedge Antilles' is present.

// Import the required modules
const request = require('request');
const myurl = process.argv[2];

request(myurl, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const episodes = JSON.parse(body).results;

    let count = 0;
    for (const filmIndex in episodes) {
      const filmChars = episodes[filmIndex].characters;

      for (const charIndex in filmChars) {
        if (filmChars[charIndex].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  } else {
    console.log('An error occured. Status code: ' + response.statusCode);
  }
});
