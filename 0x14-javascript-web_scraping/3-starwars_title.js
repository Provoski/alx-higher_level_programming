#!/usr/bin/node
const request = require('request');

function getMovieTitle (movieId) {
  const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

  request.get(apiUrl, (error, response, body) => {
    if (error) {
      console.error(error);
    } else if (response.statusCode === 200) {
      const movieData = JSON.parse(body);
      console.log(movieData.title);
    } else {
      console.error(`Failed to fetch movie data. Status code: ${response.statusCode}`);
    }
  });
}

// Check if the movie ID argument is provided
if (process.argv.length !== 3) {
  console.log('Usage: node starWarsMovie.js MOVIE_ID');
} else {
  const movieId = process.argv[2];
  getMovieTitle(movieId);
}
