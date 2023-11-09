#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];

if (!movieId) {
  console.log('Usage: ./script.js <Movie ID>');
  process.exit(1);
}

const baseUrl = 'https://swapi.dev/api/films/';

const fetchMovieData = (movieId, callback) => {
  const url = `${baseUrl}${movieId}/`;
  request(url, (error, response, body) => {
    if (error) {
      return callback(error);
    }
    if (response.statusCode !== 200) {
      return callback(new Error(`Error fetching movie data. Status Code: ${response.statusCode}`));
    }
    const movieData = JSON.parse(body);
    callback(null, movieData);
  });
};

const fetchCharacterData = (characterUrl, callback) => {
  request(characterUrl, (error, response, body) => {
    if (error) {
      return callback(error);
    }
    if (response.statusCode !== 200) {
      return callback(new Error(`Error fetching character data. Status Code: ${response.statusCode}`));
    }
    const characterData = JSON.parse(body);
    callback(null, characterData);
  });
};

const printCharacterNames = (movieId) => {
  fetchMovieData(movieId, (movieError, movieData) => {
    if (movieError) {
      return console.error(movieError.message);
    }
    const characterUrls = movieData.characters;
    let currentIndex = 0;

    const printNextCharacterName = () => {
      if (currentIndex >= characterUrls.length) {
        return; 
      }

      fetchCharacterData(characterUrls[currentIndex], (characterError, characterData) => {
        if (characterError) {
          return console.error(characterError.message);
        }
        console.log(characterData.name);
        currentIndex++;
        printNextCharacterName(); 
      });
    };

    printNextCharacterName(); 
  });
};

printCharacterNames(movieId);

