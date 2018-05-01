#!/usr/bin/node

function fac(x) {
  if (x < 0) 
        return -1;
  else if (x == 0) 
      return 1;
  else {
      return (x * fac(x - 1));
  }
}

console.log(fac(parseInt(isNaN(process.argv[2]) ? 1 : process.argv[2], 10)))
