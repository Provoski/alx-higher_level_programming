#!/usr/bin/node
const fs = require('fs');

function readAndPrintFileContent (filePath) {
  fs.readFile(filePath, 'utf-8', (err, data) => {
    if (err) {
      console.error(err);
    } else {
      console.log(data);
    }
  });
}

// Check if the file path argument is provided
if (process.argv.length !== 3) {
  console.log('Usage: node script.js FILE_PATH');
} else {
  const filePath = process.argv[2];
  readAndPrintFileContent(filePath);
}
