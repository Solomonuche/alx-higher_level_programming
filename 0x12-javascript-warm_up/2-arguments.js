#!/usr/bin/node

/* a script that prints a message depending of the number of arguments passed
 * If no arguments are passed to the script, print “No argument”
 * If only one argument is passed to the script, print “Argument found”
 * Otherwise, print “Arguments found”
 */

const argsCount = process.argv.length;

if (argsCount > 3) {
  console.log('Arguments found');
} else if (argsCount === 3) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
