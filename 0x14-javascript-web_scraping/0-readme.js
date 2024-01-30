#!/usr/bin/node
// a script that reads and prints the content of a file.

const filename = process.argv[2];
const fs = require('fs');

fs.readFile(filename, 'utf-8', (err, data) => {
  if (err) console.log(err);
  else if (data) console.log(data);
});
