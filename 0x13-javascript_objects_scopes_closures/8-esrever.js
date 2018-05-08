#!/usr/bin/node
exports.esrever = function (list) {
  return list.map((el, idx) => list[list.length - idx - 1]);
};
