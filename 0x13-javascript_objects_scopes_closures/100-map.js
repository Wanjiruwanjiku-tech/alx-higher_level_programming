#!/usr/bin/node
/*
 * the script imports a list from 100-data.js
 * use destructing to extract the list
 */

const { list } = require('./100-data');
/*
 * The map method is called on the list array. It iterates over each element of the array and applies a callback function to each element.
 * The callback function takes two parameters: value (the current element in the array) and index (the index of the current element).
 * It returns a new value for each element based on the specified computation (in this case, multiplying the value by its index).
 * The result is a new array (newList) where each element is the result of the computation.
 */

const newList = list.map((value, index) => value * index);

// logging the original and new list

console.log(list);
console.log(newList);
