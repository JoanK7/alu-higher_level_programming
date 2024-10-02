#!/usr/bin/node

const fs = require('fs');
const filePath = process.argv[2];
const toWrite = process.argv[3];

if (filePath || toWrite) {
  fs.writeFile(filePath, toWrite, 'utf8', (err) => {
    if (err) {
      console.log(err);
    }
  });
}
