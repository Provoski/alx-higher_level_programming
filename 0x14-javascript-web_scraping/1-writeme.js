#!/usr/bin/node
const fs = require('fs');

function writeToFile (filePath, content) {
  fs.writeFile(filePath, content, 'utf-8', (err) => {
    if (err) {
      console.error(err);
    }
  });
}

// Check if both file path and content arguments are provided
if (process.argv.length !== 4) {
  console.log('Usage: node script.js FILE_PATH "CONTENT_TO_WRITE"');
} else {
  const filePath = process.argv[2];
  const content = process.argv[3];
  writeToFile(filePath, content);
}
