#!/usr/bin/node

const request = require('request');

function printMovieCharacters (movieId) {
  const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

  request.get(apiUrl, (error, response, body) => {
    if (error) {
      console.error(error);
    } else if (response.statusCode === 200) {
      const movieData = JSON.parse(body);
      const charactersUrls = movieData.characters;
      fetchCharacters(charactersUrls, 0);
    }
  });
}

function fetchCharacters (charactersUrls, index) {
  if (index >= charactersUrls.length) {
    return;
  }

  request.get(charactersUrls[index], (charError, charResponse, charBody) => {
    if (charError) {
      console.error(charError);
    } else if (charResponse.statusCode === 200) {
      const characterData = JSON.parse(charBody);
      console.log(characterData.name);
      fetchCharacters(charactersUrls, index + 1);
    }
  });
}

// Check if the Movie ID argument is provided
if (process.argv.length !== 3) {
  console.log('Usage: node script.js MOVIE_ID');
} else {
  const movieId = process.argv[2];
  printMovieCharacters(movieId);
}
