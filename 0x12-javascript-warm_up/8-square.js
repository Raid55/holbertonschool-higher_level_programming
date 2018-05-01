#!/usr/bin/node

if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  let c = parseInt(process.argv[2], 10);
  let i = 0;
  let l;
  while (i++ < c) {
    l = 0;
    let st = '';
    while (l++ < c) {
      st += '#';
    }
    console.log(st);
  }
}
