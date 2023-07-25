#!/usr/bin/node
const request = require('request');

function countMoviesWithCharacter (apiUrl) {
  request.get(apiUrl, (error, response, body) => {
    if (error) {
      console.error(error);
    } else {
      const filmsData = JSON.parse(body).results;
      const wedgeMovies = filmsData.filter(movie => {
        return movie.characters.includes('https://swapi-api.alx-tools.com/api/people/18/');
      });
      console.log(`${wedgeMovies.length}`);
    }
  });
}

// Check if the API URL argument is provided
if (process.argv.length !== 3) {
  console.log('Usage: node countMoviesWithWedgeAntilles.js API_URL');
} else {
  const apiUrl = process.argv[2];
  countMoviesWithCharacter(apiUrl);
}
