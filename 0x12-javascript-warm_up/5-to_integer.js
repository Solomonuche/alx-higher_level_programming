#!/usr/bin/node

/* a script that prints My number: <first argument converted in integer>
 * if the first argument can be converted to an integer
 * If the argument can’t be converted to an integer, print “Not a number”
 */

const arg = process.argv[2];

if (!isNaN(arg)) {
  console.log(`My number: ${arg}`);
} else {
  console.log('Not a number');
}
