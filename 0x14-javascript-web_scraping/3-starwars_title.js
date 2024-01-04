#!/usr/bin/node

// The script prints the title of a star wars movie
// You must use the star wars API

const request = require('request');

const episode = process.argv[2];

if (parseInt(episode) < 8) {
    const url = 'https://swapi-api.alx-tools.com/api/films/:id';

    request(url, (err, res, body) => {
        if (err) {
            return console.log(err);
        }
        console.log(JSON.parse(body).title);
    });
}