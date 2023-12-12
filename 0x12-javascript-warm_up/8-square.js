#!/usr/bin/node

/* a script that prints a square
 * The first argument is the size of the square
 * If the first argument can’t be converted to an integer, print “Missing size”
 * You must use the character X to print the square
 */

const size = process.argv[2];
const str = 'X';

if (!isNaN(size)) {
  for (let i = 0; i < size; i++) {
    if (size <= 0) break;
    console.log(str.repeat(size));
  }
} else {
  console.log('Missing size');
}
