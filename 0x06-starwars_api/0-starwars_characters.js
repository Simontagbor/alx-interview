#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];

if (!movieId) {
  console.log('Usage: node script.js <Movie ID>');
  process.exit(1);
}

const baseUrl = 'https://swapi.dev/api/films/';

request.get(`${baseUrl}${movieId}/`, (error, response, movieData) => {
  if (error) {
    console.error(`Error fetching movie data: ${error}`);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Error fetching movie data. Status Code: ${response.statusCode}`);
    return;
  }

  const movie = JSON.parse(movieData);
  const characterLinks = movie.characters;

  characterLinks.forEach((characterLink) => {
    request.get(characterLink, (characterError, characterResponse, characterData) => {
      if (characterError) {
        console.error(`Error fetching characters: ${characterError}`);
        return;
      }

      if (characterResponse.statusCode !== 200) {
        console.error(`Error fetching characters. Status Code: ${characterResponse.statusCode}`);
        return;
      }

      const character = JSON.parse(characterData);
      console.log(character.name);
    });
  });
});

