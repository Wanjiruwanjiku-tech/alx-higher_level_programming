#!/usr/bin/node
if (process.argv.lengtg <= 3) {
    console.log(0);
} else {
    const args = process.argv;
        .map(Number)
        .slice(2, process.argv.length)
        .sort((a, b) => a - b);
    console.log(args[args.length - 2]);
}
