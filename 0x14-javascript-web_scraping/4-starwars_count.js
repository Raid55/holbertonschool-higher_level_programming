#!/usr/bin/node
const request = require('request');
let check = 'https://swapi.co/api/people/18/';
let count = 0;
request.get(process.argv[2], (err, res, body) => {
  if (err) {
    console.log(err);
    return;
  }
  let jRes = JSON.parse(body);
  for (let i in jRes.results) {
    if (jRes.results[i].characters.includes(check)) { count++; }
  }
  console.log(count);
});
