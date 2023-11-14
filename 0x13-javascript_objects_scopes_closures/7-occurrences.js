#!/usr/bin/node
// The script gets the number of occurrence
//
exports.nbOccurences = function (list, searchElement) {
  return list.filter(element => element === searchElement).length;
};
