#!/usr/bin/node
const request = require('request');
const fs = require('fs');

function fetchAndStore (url, filePath) {
  request.get(url, (error, response, body) => {
    if (error) {
      console.error(error);
    } else {
      fs.writeFile(filePath, body, 'utf-8', (err) => {
        if (err) {
          console.error(err);
        }
      });
    }
  });
}

// Check if both URL and file path arguments are provided
if (process.argv.length !== 4) {
  console.log('Usage: node fetchAndStore.js URL FILE_PATH');
} else {
  const url = process.argv[2];
  const filePath = process.argv[3];
  fetchAndStore(url, filePath);
}
