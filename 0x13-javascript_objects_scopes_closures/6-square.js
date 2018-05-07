const Square = require("./5-square.js");

module.exports = class extends Square {
  constructor(size) {
    super(size);
  }

  charPrint(c) {
    for (let i = 0; i < this.height; i++) {
      let line = "";
      for (let j = 0; j < this.width; j++)
        line += c ? c : 'X';
      console.log(line);
    }
  }

}

