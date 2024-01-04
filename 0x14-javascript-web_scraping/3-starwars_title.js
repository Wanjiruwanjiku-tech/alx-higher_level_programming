#!/usr/bin/node

// The script prints the title of a star wars movie
// You must use the star wars API

const request = require('request');

const episodeId = 18;

if (parseInt(episodeId) < 8) {
  const url = 'https://swapi-api.hbtn.io/api/films/' + episodeId;

  request(url, (err, res, body) => {
    if (err) {
      return console.log(err);
    }
    console.log(JSON.parse(body).title);
  });
}