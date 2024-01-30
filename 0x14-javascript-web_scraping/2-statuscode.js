#!/usr/bin/node
// a script that display the status code of a GET request

const url = process.argv[2];
const request = require('request');

request.get(url, (err, res, body) => {
  if (err) console.log(err);
  console.log(`code: ${res.statusCode}`);
});
