#!/usr/bin/node

//  a script that searches the second biggest integer in the list of arguments.

const args = process.argv;

if (args.length > 3) {
  const maxNumber = Math.max(...args.slice(2));
  let secondLargest = -Infinity;

  for (let i = 2; i < args.length; i++) {
    if (args[i] === maxNumber) continue;
    if (args[i] > secondLargest && args[i] < maxNumber) {
      secondLargest = args[i];
    }
  }
  console.log(secondLargest);
} else {
  console.log(0);
}
