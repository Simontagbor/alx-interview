# 0x06. Star Wars API
`API` `JavaScript` `Algorithms`

## Overview
This project is about using the [Star Wars API](https://swapi-api.hbtn.io/) to get information about Star Wars characters.

## Learning Outcomes
* How to use `request` to access the Star Wars API
* How to use Parse to read from `JSON` format.

## Tasks

### [0. Star Wars Characters](./0-starwars_characters.js)
In this Task I wrote a script that prints all characters of a Star Wars movie:
* The first positional argument passed to the script is the Movie ID - example: `3` = "Return of the Jedi"
* The script Displays one character name per line in the same order as the "characters" list in the `/films/` endpoint

#### Output
```
simontagbor@ubuntu:~/alx-interview/0x06-starwars_api$ ./0-starwars_characters.js 3
Darth Vader
R2-D2
Luke Skywalker
Han Solo
Leia Organa
Chewbacca
Palpatine
Obi-Wan Kenobi
Jabba Desilijic Tiure
Wedge Antilles
Yoda
Boba Fett
Lando Calrissian
Ackbar
Arvel Crynyd
Mon Mothma
Nien Nunb
Wicket Systri Warrick
Bib Fortuna
simontagbor@ubuntu:~/alx-interview/0x06-starwars_api$
```

