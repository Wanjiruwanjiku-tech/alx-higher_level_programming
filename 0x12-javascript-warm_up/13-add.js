#!/usr/bin/node
// define the add function
function add (a, b) {
  return a + b;
}

// Export the function to make it accessible from the outside
module.exports = {
  add
};
