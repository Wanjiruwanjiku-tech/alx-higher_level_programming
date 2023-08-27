#!/usr/bin/node

function factorial (n) {
    return n === 0 || isNan(n) ? 1 : n * factorial(n - 1);
}

console.log(factorial(Number(process.argv[2])));
