#!/usr/bin/node

const request = require('request');

function getMovieCharacters (movieId) {
  const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

  request.get(apiUrl, (error, response, body) => {
    if (error) {
      console.error(error);
    } else if (response.statusCode === 200) {
      const movieData = JSON.parse(body);
      const charactersUrls = movieData.characters;

      charactersUrls.forEach(characterUrl => {
        request.get(characterUrl, (charError, charResponse, charBody) => {
          if (charError) {
            console.error(charError);
          } else if (charResponse.statusCode === 200) {
            const characterData = JSON.parse(charBody);
            console.log(characterData.name);
          }
        });
      });
    }
  });
}

// Check if the Movie ID argument is provided
if (process.argv.length !== 3) {
  console.log('Usage: node script.js MOVIE_ID');
} else {
  const movieId = process.argv[2];
  getMovieCharacters(movieId);
}
