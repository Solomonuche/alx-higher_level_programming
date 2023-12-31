#!/usr/bin/node

/* a script that prints x times “C is fun”
 * Where x is the first argument of the script
 * If the first argument can’t be converted to an integer
 * print “Missing number of occurrences”
 */

const arg = process.argv[2];
const str = 'C is fun';

if (!isNaN(arg)) {
  for (let i = 0; i < arg; i++) {
    if (arg <= 0) break;
    console.log(str);
  }
} else {
  console.log('Missing number of occurrences');
}
