#!/usr/bin/node
// a script that reads and prints the content of a file.

const filename = process.argv[2];
const fs = require('fs');

fs.writeFile(filename, process.argv[3], 'utf-8', (err) => {
  if (err) console.log(err);
});
