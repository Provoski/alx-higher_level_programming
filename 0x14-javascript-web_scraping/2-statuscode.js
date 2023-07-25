#!/usr/bin/node
const request = require('request');

function displayStatusCode (url) {
  request.get(url, (error, response) => {
    if (error) {
      console.error(error);
    } else {
      console.log(`code: ${response.statusCode}`);
    }
  });
}

// Check if the URL argument is provided
if (process.argv.length !== 3) {
  console.log('Usage: node getStatus.js URL');
} else {
  const url = process.argv[2];
  displayStatusCode(url);
}
