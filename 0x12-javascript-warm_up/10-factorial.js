#!/usr/bin/node

// a script that computes and prints a factorial

const arg1 = process.argv[2];

function fact (a) {
  if (isNaN(a)) {
    return 1;
  } else if (a <= 0) {
    return 1;
  }

  let result = a;
  result *= fact(a - 1);
  return result;
}

console.log(fact(+arg1));
