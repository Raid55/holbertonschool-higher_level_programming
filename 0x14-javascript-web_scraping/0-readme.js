#!/usr/bin/node
const fs = require('fs');

fs.readFile(process.argv[2], 'utf8', (err, contents) => {
  if (contents) { console.log(contents); } else { console.log(err); }
});
