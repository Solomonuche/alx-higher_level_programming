#!/usr/bin/node

/* a script that prints the addition of 2 integers
 * The first argument is the first integer
 * The second argument is the second integer
 */

const arg1 = process.argv[2];
const arg2 = process.argv[3];

function add (a, b) {
  console.log(a + b);
}

add(+arg1, +arg2);
