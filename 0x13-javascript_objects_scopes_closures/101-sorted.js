#!/usr/bin/node
// the script compute a new dict imported from 101-data.js

const{ dict } = require('./101-data');

// Create a function to compute the dictionary

function computeMyDictionary(inputDict) {
	const newDict = {};

	// Iterate over each user id in the original dictionary
	
	for (const userId in inputDict) {
		const occurrences = inputDict[userId];
		if (!newDict[occurrences]) {
			newDict[occurrences] = [];
		}
		newDict[occurrences].push(userId);
	}
	return newDict;
}
// Compute the new dictionary and log it

const newDict = computeNewDictionary(dict);
console.log(newDict);
