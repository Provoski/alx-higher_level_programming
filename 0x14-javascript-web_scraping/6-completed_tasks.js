#!/usr/bin/node
const request = require('request');

function countCompletedTasks (apiUrl) {
  request.get(apiUrl, (error, response, body) => {
    if (error) {
      console.error('Error fetching data:', error);
    } else if (response.statusCode === 200) {
      const todos = JSON.parse(body);
      const usersCompletedTasks = {};

      todos.forEach(todo => {
        if (todo.completed) {
          // Check if the user ID exists in the dictionary
          if (Object.prototype.hasOwnProperty.call(usersCompletedTasks, todo.userId)) {
            // If it exists, increment the completed tasks count
            usersCompletedTasks[todo.userId]++;
          } else {
            // If it doesn't exist, set completed tasks count to 1
            usersCompletedTasks[todo.userId] = 1;
          }
        }
      });

      console.log(usersCompletedTasks);
    }
  });
}

// Check if the API URL argument is provided
if (process.argv.length !== 3) {
  console.log('Usage: node countCompletedTasks.js API_URL');
} else {
  const apiUrl = process.argv[2];
  countCompletedTasks(apiUrl);
}
