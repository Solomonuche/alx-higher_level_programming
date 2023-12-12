#!/usr/bin/node

/* a script that prints the first argument passed to it
 * If no arguments are passed to the script, print “No argument”
 * You are not allowed to use length
 */

const args = process.argv;

if (args[2]) {
  console.log(args[2]);
} else {
  console.log('No argument');
}
