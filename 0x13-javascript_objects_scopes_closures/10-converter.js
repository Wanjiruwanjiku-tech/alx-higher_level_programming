#!/usr/bin/node
// the script creates a function that converts a num from base 10 to another base

exports.converter = function (base) {
	exports.converterAux = function (number) {
		if (number > 0) {
			exports.converterAux((number / base) | 0);
			process.stdout.write((number % base).toString());
		}
	};
};
