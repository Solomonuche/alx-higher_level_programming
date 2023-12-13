#!/usr/bin/node
//  a function that prints the number of arguments already printed and the new argument value

exports.logMe = (function (item) {
  let count = -1;

  return (item) => {
    count++;
    console.log(`${count}: ${item}`);
  };
}());
