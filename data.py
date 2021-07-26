import requests
data =[
  {
    "popularity99": 83.0,
    "director": "Victor Fleming",
    "genre": [
      "Adventure",
      " Family",
      " Fantasy",
      " Musical"
    ],
    "imdb_score": 8.3,
    "name": "The Wizard of Oz"
  },
  {
    "popularity99": 88.0,
    "director": "George Lucas",
    "genre": [
      "Action",
      " Adventure",
      " Fantasy",
      " Sci-Fi"
    ],
    "imdb_score": 8.8,
    "name": "Star Wars"
  },
  {
    "popularity99": 66.0,
    "director": "Giovanni Pastrone",
    "genre": [
      "Adventure",
      " Drama",
      " War"
    ],
    "imdb_score": 6.6,
    "name": "Cabiria"
  },
  {
    "popularity99": 87.0,
    "director": "Alfred Hitchcock",
    "genre": [
      "Horror",
      " Mystery",
      " Thriller"
    ],
    "imdb_score": 8.7,
    "name": "Psycho"
  },
  {
    "popularity99": 80.0,
    "director": "Merian C. Cooper",
    "genre": [
      "Adventure",
      " Fantasy",
      " Horror"
    ],
    "imdb_score": 8.0,
    "name": "King Kong"
  },
  {
    "popularity99": 84.0,
    "director": "Fritz Lang",
    "genre": [
      "Adventure",
      " Drama",
      " Sci-Fi"
    ],
    "imdb_score": 8.4,
    "name": "Metropolis"
  },
  {
    "popularity99": 86.0,
    "director": "Marc Daniels",
    "genre": [
      "Adventure",
      " Sci-Fi"
    ],
    "imdb_score": 8.6,
    "name": "Star Trek"
  },
  {
    "popularity99": 88.0,
    "director": "Michael Curtiz",
    "genre": [
      "Drama",
      " Romance",
      " War"
    ],
    "imdb_score": 8.8,
    "name": "Casablanca"
  },
  {
    "popularity99": 79.0,
    "director": "William Cottrell",
    "genre": [
      "Animation",
      " Family",
      " Fantasy",
      " Musical",
      " Romance"
    ],
    "imdb_score": 7.9,
    "name": "Snow White and the Seven Dwarfs"
  },
  {
    "popularity99": 84.0,
    "director": "Stanley Kubrick",
    "genre": [
      "Adventure",
      " Mystery",
      " Sci-Fi"
    ],
    "imdb_score": 8.4,
    "name": "2001 : A Space Odyssey"
  },
  {
    "popularity99": 92.0,
    "director": "Francis Ford Coppola",
    "genre": [
      "Crime",
      " Drama"
    ],
    "imdb_score": 9.2,
    "name": "The Godfather"
  },
  {
    "popularity99": 71.0,
    "director": "D.W. Griffith",
    "genre": [
      "Drama",
      " History",
      " Romance",
      " War",
      " Western"
    ],
    "imdb_score": 7.1,
    "name": "The Birth of a Nation"
  },
  {
    "popularity99": 81.0,
    "director": "Alfred Hitchcock",
    "genre": [
      "Crime",
      " Film-Noir",
      " Mystery",
      " Thriller"
    ],
    "imdb_score": 8.1,
    "name": "Shadow of a Doubt"
  },
  {
    "popularity99": 83.0,
    "director": "Steven Spielberg",
    "genre": [
      "Thriller"
    ],
    "imdb_score": 8.3,
    "name": "Jaws"
  },
  {
    "popularity99": 64.0,
    "director": "J. Searle Dawley",
    "genre": [
      "Fantasy",
      " Romance"
    ],
    "imdb_score": 6.4,
    "name": "Snow White"
  },
  {
    "popularity99": 86.0,
    "director": "Francis Ford Coppola",
    "genre": [
      "Drama",
      " War"
    ],
    "imdb_score": 8.6,
    "name": "Apocalypse Now"
  },
  {
    "popularity99": 82.0,
    "director": "Victor Fleming",
    "genre": [
      "Drama",
      " Romance",
      " War"
    ],
    "imdb_score": 8.2,
    "name": "Gone with the Wind"
  },
  {
    "popularity99": 76.0,
    "director": "Ernst Lubitsch",
    "genre": [
      "Musical",
      " Comedy",
      " Romance"
    ],
    "imdb_score": 7.6,
    "name": "The Merry Widow"
  },
  {
    "popularity99": 81.0,
    "director": "John Ford",
    "genre": [
      "Adventure",
      " Drama",
      " Western"
    ],
    "imdb_score": 8.1,
    "name": "The Searchers"
  },
  {
    "popularity99": 86.0,
    "director": "Alfred Hitchcock",
    "genre": [
      "Crime",
      " Mystery",
      " Romance",
      " Thriller"
    ],
    "imdb_score": 8.6,
    "name": "Vertigo"
  },
  {
    "popularity99": 73.0,
    "director": "Terence Young",
    "genre": [
      "Action",
      " Adventure",
      " Thriller"
    ],
    "imdb_score": 7.3,
    "name": "Dr. No"
  },
  {
    "popularity99": 83.0,
    "director": "Orson Welles",
    "genre": [
      "Crime",
      " Film-Noir",
      " Thriller"
    ],
    "imdb_score": 8.3,
    "name": "Touch of Evil"
  },
  {
    "popularity99": 74.0,
    "director": "Merian C. Cooper",
    "genre": [
      "Adventure",
      " Documentary"
    ],
    "imdb_score": 7.4,
    "name": "Chang : A Drama of the Wilderness"
  },
  {
    "popularity99": 81.0,
    "director": "William Friedkin",
    "genre": [
      "Horror"
    ],
    "imdb_score": 8.1,
    "name": "The Exorcist"
  },
  {
    "popularity99": 86.0,
    "director": "Orson Welles",
    "genre": [
      "Drama",
      " Mystery"
    ],
    "imdb_score": 8.6,
    "name": "Citizen Kane"
  },
  {
    "popularity99": 81.0,
    "director": "James Cameron",
    "genre": [
      "Action",
      " Sci-Fi",
      " Thriller"
    ],
    "imdb_score": 8.1,
    "name": "The Terminator"
  },
  {
    "popularity99": 81.0,
    "director": "Roman Polanski",
    "genre": [
      "Drama",
      " Horror",
      " Mystery"
    ],
    "imdb_score": 8.1,
    "name": "Rosemarys Baby"
  },
  {
    "popularity99": 81.0,
    "director": "Sergei M. Eisenstein",
    "genre": [
      "Drama",
      " History",
      " War"
    ],
    "imdb_score": 8.1,
    "name": "Bronenosets Potyomkin"
  },
  {
    "popularity99": 88.0,
    "director": "Irvin Kershner",
    "genre": [
      "Action",
      " Adventure",
      " Sci-Fi"
    ],
    "imdb_score": 8.8,
    "name": "Star Wars : Episode V - The Empire Strikes Back"
  },
  {
    "popularity99": 71.0,
    "director": "Harry O. Hoyt",
    "genre": [
      "Adventure",
      " Fantasy",
      " Horror",
      " Sci-Fi",
      " Thriller"
    ],
    "imdb_score": 7.1,
    "name": "The Lost World"
  },
  {
    "popularity99": 85.0,
    "director": "Stanley Kubrick",
    "genre": [
      "Crime",
      " Drama",
      " Sci-Fi"
    ],
    "imdb_score": 8.5,
    "name": "A Clockwork Orange"
  },
  {
    "popularity99": 80.0,
    "director": "James Whale",
    "genre": [
      "Drama",
      " Horror",
      " Sci-Fi"
    ],
    "imdb_score": 8.0,
    "name": "Frankenstein"
  },
  {
    "popularity99": 85.0,
    "director": "Lisa Simon",
    "genre": [
      "Animation",
      " Comedy",
      " Family",
      " Fantasy",
      " Music"
    ],
    "imdb_score": 8.5,
    "name": "Sesame Street"
  },
  {
    "popularity99": 82.0,
    "director": "Jean Renoir",
    "genre": [
      "Drama",
      " War"
    ],
    "imdb_score": 8.2,
    "name": "La grande illusion"
  },
  {
    "popularity99": 87.0,
    "director": "Steven Spielberg",
    "genre": [
      "Action",
      " Adventure"
    ],
    "imdb_score": 8.7,
    "name": "Raiders of the Lost Ark"
  },
  {
    "popularity99": 80.0,
    "director": "George A. Romero",
    "genre": [
      "Horror",
      " Mystery"
    ],
    "imdb_score": 8.0,
    "name": "Night of the Living Dead"
  },
  {
    "popularity99": 53.0,
    "director": "Larry Semon",
    "genre": [
      "Comedy",
      " Family",
      " Fantasy",
      " Adventure"
    ],
    "imdb_score": 5.3,
    "name": "The Wizard of Oz"
  },
  {
    "popularity99": 68.0,
    "director": "George Lucas",
    "genre": [
      "Drama",
      " Mystery",
      " Sci-Fi",
      " Thriller"
    ],
    "imdb_score": 6.8,
    "name": "THX 1138"
  },
  {
    "popularity99": 79.0,
    "director": "Steven Spielberg",
    "genre": [
      "Adventure",
      " Drama",
      " Family",
      " Fantasy",
      " Sci-Fi"
    ],
    "imdb_score": 7.9,
    "name": "E.T. : The Extra-Terrestrial"
  },
  {
    "popularity99": 69.0,
    "director": "Maurice Tourneur",
    "genre": [
      "Comedy",
      " Drama"
    ],
    "imdb_score": 6.9,
    "name": "The Poor Little Rich Girl"
  },
  {
    "popularity99": 46.0,
    "director": "James Parrott",
    "genre": [
      "Short",
      " Adventure",
      " Comedy"
    ],
    "imdb_score": 4.6,
    "name": "The Tin Man"
  },
  {
    "popularity99": 86.0,
    "director": "Martin Scorsese",
    "genre": [
      "Drama",
      " Thriller"
    ],
    "imdb_score": 8.6,
    "name": "Taxi Driver"
  },
  {
    "popularity99": 90.0,
    "director": "Sergio Leone",
    "genre": [
      "Adventure",
      " Western"
    ],
    "imdb_score": 9.0,
    "name": "Il buono, il brutto, il cattivo."
  },
  {
    "popularity99": 66.0,
    "director": "D.W. Griffith",
    "genre": [
      "Short",
      " Action",
      " Western"
    ],
    "imdb_score": 6.6,
    "name": "The Battle at Elderbush Gulch"
  },
  {
    "popularity99": 84.0,
    "director": "Stanley Donen",
    "genre": [
      "Comedy",
      " Musical",
      " Romance"
    ],
    "imdb_score": 8.4,
    "name": "Singin in the Rain"
  },
  {
    "popularity99": 84.0,
    "director": "Elia Kazan",
    "genre": [
      "Crime",
      " Drama",
      " Romance"
    ],
    "imdb_score": 8.4,
    "name": "On the Waterfront"
  },
  {
    "popularity99": 84.0,
    "director": "Clyde Bruckman",
    "genre": [
      "Comedy",
      " Romance",
      " War",
      " Action"
    ],
    "imdb_score": 8.4,
    "name": "The General"
  },
  {
    "popularity99": 78.0,
    "director": "Ivan Reitman",
    "genre": [
      "Adventure",
      " Fantasy",
      " Mystery"
    ],
    "imdb_score": 7.8,
    "name": "Ghost Busters"
  },
  {
    "popularity99": 71.0,
    "director": "W.S. Van Dyke",
    "genre": [
      "Action",
      " Adventure",
      " Romance"
    ],
    "imdb_score": 7.1,
    "name": "Tarzan the Ape Man"
  },
  {
    "popularity99": 60.0,
    "director": "L. Frank Baum",
    "genre": [
      "Family",
      " Fantasy",
      " Adventure",
      " Comedy"
    ],
    "imdb_score": 6.0,
    "name": "His Majesty, the Scarecrow of Oz"
  },
  {
    "popularity99": 95.0,
    "director": "John Brahm",
    "genre": [
      "Drama",
      " Fantasy",
      " Mystery",
      " Sci-Fi",
      " Thriller"
    ],
    "imdb_score": 9.5,
    "name": "The Twilight Zone"
  },
  {
    "popularity99": 75.0,
    "director": "Edwin S. Porter",
    "genre": [
      "Short",
      " Western"
    ],
    "imdb_score": 7.5,
    "name": "The Great Train Robbery"
  },
  {
    "popularity99": 79.0,
    "director": "Guy Hamilton",
    "genre": [
      "Action",
      " Adventure",
      " Thriller"
    ],
    "imdb_score": 7.9,
    "name": "Goldfinger"
  },
  {
    "popularity99": 81.0,
    "director": "Federico Fellini",
    "genre": [
      "Comedy",
      " Drama"
    ],
    "imdb_score": 8.1,
    "name": "La dolce vita"
  },
  {
    "popularity99": 85.0,
    "director": "Ridley Scott",
    "genre": [
      "Adventure",
      " Horror",
      " Sci-Fi",
      " Thriller"
    ],
    "imdb_score": 8.5,
    "name": "Alien"
  },
  {
    "popularity99": 81.0,
    "director": "F.W. Murnau",
    "genre": [
      "Fantasy",
      " Horror"
    ],
    "imdb_score": 8.1,
    "name": "Nosferatu, eine Symphonie des Grauens"
  },
  {
    "popularity99": 85.0,
    "director": "Stanley Kubrick",
    "genre": [
      "Horror",
      " Mystery"
    ],
    "imdb_score": 8.5,
    "name": "The Shining"
  },
  {
    "popularity99": 86.0,
    "director": "Stanley Kubrick",
    "genre": [
      "Comedy",
      " Drama"
    ],
    "imdb_score": 8.6,
    "name": "Dr. Strangelove or : How I Learned to Stop Worrying and Love the Bomb"
  },
  {
    "popularity99": 82.0,
    "director": "Brian De Palma",
    "genre": [
      "Crime",
      " Drama",
      " Thriller"
    ],
    "imdb_score": 8.2,
    "name": "Scarface"
  },
  {
    "popularity99": 81.0,
    "director": "John G. Avildsen",
    "genre": [
      "Drama",
      " Romance",
      " Sport"
    ],
    "imdb_score": 8.1,
    "name": "Rocky"
  },
  {
    "popularity99": 90.0,
    "director": "Mark Kirkland",
    "genre": [
      "Animation",
      " Comedy"
    ],
    "imdb_score": 9.0,
    "name": "The Simpsons"
  },
  {
    "popularity99": 80.0,
    "director": "Luis Bu1uel",
    "genre": [
      "Short",
      " Fantasy"
    ],
    "imdb_score": 8.0,
    "name": "Un chien andalou"
  },
  {
    "popularity99": 77.0,
    "director": "Tod Browning",
    "genre": [
      "Fantasy",
      " Horror"
    ],
    "imdb_score": 7.7,
    "name": "Dracula"
  },
  {
    "popularity99": 75.0,
    "director": "Ted Kotcheff",
    "genre": [
      "Action",
      " Adventure",
      " Drama",
      " Thriller"
    ],
    "imdb_score": 7.5,
    "name": "First Blood"
  },
  {
    "popularity99": 80.0,
    "director": "Joseph Barbera",
    "genre": [
      "Animation",
      " Family",
      " Comedy"
    ],
    "imdb_score": 8.0,
    "name": "The Flintstones"
  },
  {
    "popularity99": 77.0,
    "director": "Oscar Rudolph",
    "genre": [
      "Action",
      " Adventure",
      " Comedy",
      " Crime",
      " Family",
      " Fantasy",
      " Mystery",
      " Sci-Fi"
    ],
    "imdb_score": 7.7,
    "name": "Batman"
  },
  {
    "popularity99": 70.0,
    "director": "John Ford",
    "genre": [
      "Adventure",
      " War"
    ],
    "imdb_score": 7.0,
    "name": "The Lost Patrol"
  },
  {
    "popularity99": 81.0,
    "director": "Mervyn LeRoy",
    "genre": [
      "Crime",
      " Drama",
      " Film-Noir"
    ],
    "imdb_score": 8.1,
    "name": "I Am a Fugitive from a Chain Gang"
  },
  {
    "popularity99": 84.0,
    "director": "Robert Zemeckis",
    "genre": [
      "Adventure",
      " Family",
      " Sci-Fi"
    ],
    "imdb_score": 8.4,
    "name": "Back to the Future"
  },
  {
    "popularity99": 79.0,
    "director": "John Boorman",
    "genre": [
      "Adventure",
      " Drama",
      " Thriller"
    ],
    "imdb_score": 7.9,
    "name": "Deliverance"
  },
  {
    "popularity99": 84.0,
    "director": "Alfred Hitchcock",
    "genre": [
      "Mystery",
      " Romance",
      " Thriller"
    ],
    "imdb_score": 8.4,
    "name": "Rebecca"
  },
  {
    "popularity99": 80.0,
    "director": "Edward F. Cline",
    "genre": [
      "Comedy",
      " Short",
      " Family"
    ],
    "imdb_score": 8.0,
    "name": "The Scarecrow"
  },
  {
    "popularity99": 75.0,
    "director": "Tobe Hooper",
    "genre": [
      "Horror",
      " Mystery",
      " Thriller"
    ],
    "imdb_score": 7.5,
    "name": "The Texas Chain Saw Massacre"
  },
  {
    "popularity99": 84.0,
    "director": "David Lean",
    "genre": [
      "Adventure",
      " Drama",
      " War"
    ],
    "imdb_score": 8.4,
    "name": "The Bridge on the River Kwai"
  },
  {
    "popularity99": 87.0,
    "director": "Frank Capra",
    "genre": [
      "Drama",
      " Fantasy",
      " Romance"
    ],
    "imdb_score": 8.7,
    "name": "Its a Wonderful Life"
  },
  {
    "popularity99": 71.0,
    "director": "Steven Soderbergh",
    "genre": [
      "Drama"
    ],
    "imdb_score": 7.1,
    "name": "Sex, Lies, and Videotape"
  },
  {
    "popularity99": 79.0,
    "director": "Don Siegel",
    "genre": [
      "Action",
      " Crime",
      " Thriller"
    ],
    "imdb_score": 7.9,
    "name": "Dirty Harry"
  },
  {
    "popularity99": 79.0,
    "director": "George Cukor",
    "genre": [
      "Drama",
      " Family",
      " Musical",
      " Romance"
    ],
    "imdb_score": 7.9,
    "name": "My Fair Lady"
  },
  {
    "popularity99": 75.0,
    "director": "Samuel Armstrong",
    "genre": [
      "Animation",
      " Family",
      " Musical"
    ],
    "imdb_score": 7.5,
    "name": "Dumbo"
  },
  {
    "popularity99": 79.0,
    "director": "Alfred Hitchcock",
    "genre": [
      "Horror",
      " Romance",
      " Thriller"
    ],
    "imdb_score": 7.9,
    "name": "The Birds"
  },
  {
    "popularity99": 72.0,
    "director": "James W. Horne",
    "genre": [
      "Comedy",
      " Drama",
      " Sport"
    ],
    "imdb_score": 7.2,
    "name": "College"
  },
  {
    "popularity99": 74.0,
    "director": "James Cameron",
    "genre": [
      "Drama",
      " History",
      " Romance"
    ],
    "imdb_score": 7.4,
    "name": "Titanic"
  },
  {
    "popularity99": 82.0,
    "director": "William Wyler",
    "genre": [
      "Action",
      " Adventure",
      " Drama",
      " History",
      " Romance"
    ],
    "imdb_score": 8.2,
    "name": "Ben-Hur"
  },
  {
    "popularity99": 90.0,
    "director": "Quentin Tarantino",
    "genre": [
      "Crime",
      " Drama"
    ],
    "imdb_score": 9.0,
    "name": "Pulp Fiction"
  },
  {
    "popularity99": 87.0,
    "director": "Alfred Hitchcock",
    "genre": [
      "Crime",
      " Mystery",
      " Romance",
      " Thriller"
    ],
    "imdb_score": 8.7,
    "name": "Rear Window"
  },
  {
    "popularity99": 85.0,
    "director": "James Cameron",
    "genre": [
      "Action",
      " Sci-Fi",
      " Thriller"
    ],
    "imdb_score": 8.5,
    "name": "Aliens"
  },
  {
    "popularity99": 70.0,
    "director": "John Cromwell",
    "genre": [
      "Drama",
      " Mystery",
      " Romance"
    ],
    "imdb_score": 7.0,
    "name": "Algiers"
  },
  {
    "popularity99": 81.0,
    "director": "Erich von Stroheim",
    "genre": [
      "Drama"
    ],
    "imdb_score": 8.1,
    "name": "Greed"
  },
  {
    "popularity99": 87.0,
    "director": "Jonathan Demme",
    "genre": [
      "Crime",
      " Thriller"
    ],
    "imdb_score": 8.7,
    "name": "The Silence of the Lambs"
  },
  {
    "popularity99": 79.0,
    "director": "Charles Chaplin",
    "genre": [
      "Comedy",
      " Family",
      " Drama",
      " Romance"
    ],
    "imdb_score": 7.9,
    "name": "The Circus"
  },
  {
    "popularity99": 90.0,
    "director": "Kim Manners",
    "genre": [
      "Drama",
      " Mystery",
      " Sci-Fi",
      " Thriller"
    ],
    "imdb_score": 9.0,
    "name": "The X Files"
  },
  {
    "popularity99": 85.0,
    "director": "James Cameron",
    "genre": [
      "Action",
      " Sci-Fi",
      " Thriller"
    ],
    "imdb_score": 8.5,
    "name": "Terminator 2 : Judgment Day"
  },
  {
    "popularity99": 60.0,
    "director": "Joseph C. Terry",
    "genre": [
      "Talk-Show"
    ],
    "imdb_score": 6.0,
    "name": "The Oprah Winfrey Show"
  },
  {
    "popularity99": 82.0,
    "director": "Mike Nichols",
    "genre": [
      "Comedy",
      " Drama",
      " Romance"
    ],
    "imdb_score": 8.2,
    "name": "The Graduate"
  },
  {
    "popularity99": 55.0,
    "director": "Henry Lehrman",
    "genre": [
      "Comedy",
      " Short"
    ],
    "imdb_score": 5.5,
    "name": "The Bangville Police"
  },
  {
    "popularity99": 87.0,
    "director": "Andy Wachowski",
    "genre": [
      "Action",
      " Adventure",
      " Sci-Fi"
    ],
    "imdb_score": 8.7,
    "name": "The Matrix"
  },
  {
    "popularity99": 70.0,
    "director": "Oscar Rudolph",
    "genre": [
      "Comedy",
      " Family"
    ],
    "imdb_score": 7.0,
    "name": "The Brady Bunch"
  },
  {
    "popularity99": 85.0,
    "director": "David Lean",
    "genre": [
      "Adventure",
      " Biography",
      " Drama",
      " History",
      " War"
    ],
    "imdb_score": 8.5,
    "name": "Lawrence of Arabia"
  },
  {
    "popularity99": 74.0,
    "director": "Wes Craven",
    "genre": [
      "Horror",
      " Mystery"
    ],
    "imdb_score": 7.4,
    "name": "A Nightmare on Elm Street"
  },
  {
    "popularity99": 78.0,
    "director": "George Schaefer",
    "genre": [
      "Comedy",
      " Drama"
    ],
    "imdb_score": 7.8,
    "name": "Pygmalion"
  },
  {
    "popularity99": 86.0,
    "director": "Alfred Hitchcock",
    "genre": [
      "Adventure",
      " Drama",
      " Mystery",
      " Romance",
      " Thriller"
    ],
    "imdb_score": 8.6,
    "name": "North by Northwest"
  },
  {
    "popularity99": 79.0,
    "director": "Robert Wise",
    "genre": [
      "Biography",
      " Drama",
      " Family",
      " Musical"
    ],
    "imdb_score": 7.9,
    "name": "The Sound of Music"
  },
  {
    "popularity99": 78.0,
    "director": "Jack Arnold",
    "genre": [
      "Comedy",
      " Family"
    ],
    "imdb_score": 7.8,
    "name": "Gilligans Island"
  },
  {
    "popularity99": 76.0,
    "director": "James Algar",
    "genre": [
      "Animation",
      " Drama",
      " Family"
    ],
    "imdb_score": 7.6,
    "name": "Bambi"
  },
  {
    "popularity99": 78.0,
    "director": "Jerome Robbins",
    "genre": [
      "Crime",
      " Drama",
      " Musical",
      " Romance"
    ],
    "imdb_score": 7.8,
    "name": "West Side Story"
  },
  {
    "popularity99": 79.0,
    "director": "Fred Zinnemann",
    "genre": [
      "Drama",
      " Romance",
      " War"
    ],
    "imdb_score": 7.9,
    "name": "From Here to Eternity"
  },
  {
    "popularity99": 79.0,
    "director": "John Carpenter",
    "genre": [
      "Horror",
      " Thriller"
    ],
    "imdb_score": 7.9,
    "name": "Halloween"
  },
  {
    "popularity99": 90.0,
    "director": "William Asher",
    "genre": [
      "Comedy",
      " Family"
    ],
    "imdb_score": 9.0,
    "name": "I Love Lucy"
  },
  {
    "popularity99": 74.0,
    "director": "Karl Freund",
    "genre": [
      "Romance",
      " Horror"
    ],
    "imdb_score": 7.4,
    "name": "Mad Love"
  },
  {
    "popularity99": 83.0,
    "director": "Ridley Scott",
    "genre": [
      "Drama",
      " Sci-Fi",
      " Thriller"
    ],
    "imdb_score": 8.3,
    "name": "Blade Runner"
  },
  {
    "popularity99": 77.0,
    "director": "Robert Stevenson",
    "genre": [
      "Comedy",
      " Family",
      " Fantasy",
      " Musical"
    ],
    "imdb_score": 7.7,
    "name": "Mary Poppins"
  },
  {
    "popularity99": 83.0,
    "director": "Richard Marquand",
    "genre": [
      "Action",
      " Adventure",
      " Fantasy",
      " Sci-Fi"
    ],
    "imdb_score": 8.3,
    "name": "Star Wars : Episode VI - Return of the Jedi"
  },
  {
    "popularity99": 78.0,
    "director": "Steven Spielberg",
    "genre": [
      "Drama",
      " Sci-Fi"
    ],
    "imdb_score": 7.8,
    "name": "Close Encounters of the Third Kind"
  },
  {
    "popularity99": 88.0,
    "director": "Akira Kurosawa",
    "genre": [
      "Adventure",
      " Drama"
    ],
    "imdb_score": 8.8,
    "name": "Shichinin no samurai"
  },
  {
    "popularity99": 80.0,
    "director": "James Whale",
    "genre": [
      "Horror",
      " Sci-Fi"
    ],
    "imdb_score": 8.0,
    "name": "Bride of Frankenstein"
  },
  {
    "popularity99": 85.0,
    "director": "John Huston",
    "genre": [
      "Adventure",
      " Drama",
      " Western",
      " Action"
    ],
    "imdb_score": 8.5,
    "name": "The Treasure of the Sierra Madre"
  },
  {
    "popularity99": 60.0,
    "director": "Phil Karlson",
    "genre": [
      "Drama",
      " Crime",
      " Film-Noir"
    ],
    "imdb_score": 6.0,
    "name": "5 Against the House"
  },
  {
    "popularity99": 79.0,
    "director": "Akira Kurosawa",
    "genre": [
      "Drama",
      " History",
      " War"
    ],
    "imdb_score": 7.9,
    "name": "Kagemusha"
  },
  {
    "popularity99": 47.0,
    "director": "D.W. Griffith",
    "genre": [
      "Short",
      " Drama"
    ],
    "imdb_score": 4.7,
    "name": "His Trust Fulfilled"
  },
  {
    "popularity99": 53.0,
    "director": "D.W. Griffith",
    "genre": [
      "Short",
      " Drama",
      " War"
    ],
    "imdb_score": 5.3,
    "name": "His Trust"
  },
  {
    "popularity99": 73.0,
    "director": "Ishirccab Honda",
    "genre": [
      "Drama",
      " Horror",
      " Sci-Fi",
      " Thriller"
    ],
    "imdb_score": 7.3,
    "name": "Gojira"
  },
  {
    "popularity99": 80.0,
    "director": "Stanley Kubrick",
    "genre": [
      "Action",
      " Adventure",
      " Biography",
      " Drama",
      " History"
    ],
    "imdb_score": 8.0,
    "name": "Spartacus"
  },
  {
    "popularity99": 71.0,
    "director": "Winsor McCay",
    "genre": [
      "Animation",
      " Short"
    ],
    "imdb_score": 7.1,
    "name": "Dreams of the Rarebit Fiend : The Pet"
  },
  {
    "popularity99": 84.0,
    "director": "John Huston",
    "genre": [
      "Crime",
      " Film-Noir",
      " Mystery"
    ],
    "imdb_score": 8.4,
    "name": "The Maltese Falcon"
  },
  {
    "popularity99": 80.0,
    "director": "Franklin J. Schaffner",
    "genre": [
      "Adventure",
      " Mystery",
      " Sci-Fi"
    ],
    "imdb_score": 8.0,
    "name": "Planet of the Apes"
  },
  {
    "popularity99": 72.0,
    "director": "Frank Lloyd",
    "genre": [
      "Adventure",
      " Drama",
      " Romance"
    ],
    "imdb_score": 7.2,
    "name": "The Sea Hawk"
  },
  {
    "popularity99": 82.0,
    "director": "Lewis Milestone",
    "genre": [
      "Action",
      " Drama",
      " History",
      " War"
    ],
    "imdb_score": 8.2,
    "name": "All Quiet on the Western Front"
  },
  {
    "popularity99": 74.0,
    "director": "Carl Boese",
    "genre": [
      "Fantasy",
      " Horror"
    ],
    "imdb_score": 7.4,
    "name": "Der Golem, wie er in die Welt kam"
  },
  {
    "popularity99": 59.0,
    "director": "Gordon Douglas",
    "genre": [
      "Action",
      " Adventure",
      " Comedy",
      " Sci-Fi"
    ],
    "imdb_score": 5.9,
    "name": "In Like Flint"
  },
  {
    "popularity99": 74.0,
    "director": "Leo McCarey",
    "genre": [
      "Drama",
      " Family"
    ],
    "imdb_score": 7.4,
    "name": "The Bells of St. Marys"
  },
  {
    "popularity99": 77.0,
    "director": "Steven Spielberg",
    "genre": [
      "Mystery",
      " Thriller"
    ],
    "imdb_score": 7.7,
    "name": "Duel"
  },
  {
    "popularity99": 78.0,
    "director": "Sergei M. Eisenstein",
    "genre": [
      "Drama"
    ],
    "imdb_score": 7.8,
    "name": "Stachka"
  },
  {
    "popularity99": 71.0,
    "director": "Fred Zinnemann",
    "genre": [
      "Musical",
      " Romance",
      " Western"
    ],
    "imdb_score": 7.1,
    "name": "Oklahoma!"
  },
  {
    "popularity99": 74.0,
    "director": "Maya Deren",
    "genre": [
      "Short"
    ],
    "imdb_score": 7.4,
    "name": "At Land"
  },
  {
    "popularity99": 79.0,
    "director": "Steven Spielberg",
    "genre": [
      "Action",
      " Adventure",
      " Family",
      " Sci-Fi"
    ],
    "imdb_score": 7.9,
    "name": "Jurassic Park"
  },
  {
    "popularity99": 79.0,
    "director": "John Ford",
    "genre": [
      "Action",
      " Drama",
      " Romance",
      " Western"
    ],
    "imdb_score": 7.9,
    "name": "Stagecoach"
  },
  {
    "popularity99": 86.0,
    "director": "Stanley Kubrick",
    "genre": [
      "Crime",
      " Drama",
      " War"
    ],
    "imdb_score": 8.6,
    "name": "Paths of Glory"
  },
  {
    "popularity99": 77.0,
    "director": "Jerry Paris",
    "genre": [
      "Comedy",
      " Family",
      " Music"
    ],
    "imdb_score": 7.7,
    "name": "Happy Days"
  },
  {
    "popularity99": 68.0,
    "director": "John Badham",
    "genre": [
      "Drama",
      " Music",
      " Romance"
    ],
    "imdb_score": 6.8,
    "name": "Saturday Night Fever"
  },
  {
    "popularity99": 81.0,
    "director": "George Cukor",
    "genre": [
      "Comedy",
      " Romance"
    ],
    "imdb_score": 8.1,
    "name": "The Philadelphia Story"
  },
  {
    "popularity99": 82.0,
    "director": "Federico Fellini",
    "genre": [
      "Drama",
      " Fantasy"
    ],
    "imdb_score": 8.2,
    "name": "8xe5"
  },
  {
    "popularity99": 86.0,
    "director": "Douglas Camfield",
    "genre": [
      "Adventure",
      " Drama",
      " Sci-Fi"
    ],
    "imdb_score": 8.6,
    "name": "Doctor Who"
  },
  {
    "popularity99": 86.0,
    "director": "Fritz Lang",
    "genre": [
      "Crime",
      " Thriller"
    ],
    "imdb_score": 8.6,
    "name": "M"
  },
  {
    "popularity99": 74.0,
    "director": "John Huston",
    "genre": [
      "Adventure",
      " Drama"
    ],
    "imdb_score": 7.4,
    "name": "Moby Dick"
  },
  {
    "popularity99": 74.0,
    "director": "Brian De Palma",
    "genre": [
      "Horror",
      " Thriller"
    ],
    "imdb_score": 7.4,
    "name": "Carrie"
  },
  {
    "popularity99": 79.0,
    "director": "Nicholas Ray",
    "genre": [
      "Drama",
      " Romance"
    ],
    "imdb_score": 7.9,
    "name": "Rebel Without a Cause"
  },
  {
    "popularity99": 73.0,
    "director": "Richard Donner",
    "genre": [
      "Action",
      " Adventure",
      " Family",
      " Sci-Fi"
    ],
    "imdb_score": 7.3,
    "name": "Superman"
  },
  {
    "popularity99": 88.0,
    "director": "Peter Harris",
    "genre": [
      "Comedy",
      " Family",
      " Music"
    ],
    "imdb_score": 8.8,
    "name": "The Muppet Show"
  },
  {
    "popularity99": 77.0,
    "director": "Norman Ferguson",
    "genre": [
      "Animation",
      " Drama",
      " Family",
      " Fantasy",
      " Music"
    ],
    "imdb_score": 7.7,
    "name": "Pinocchio"
  },
  {
    "popularity99": 75.0,
    "director": "Arthur Lipsett",
    "genre": [
      "Short"
    ],
    "imdb_score": 7.5,
    "name": "21-87"
  },
  {
    "popularity99": 81.0,
    "director": "Joseph Barbera",
    "genre": [
      "Animation",
      " Family",
      " Mystery",
      " Comedy",
      " Adventure"
    ],
    "imdb_score": 8.1,
    "name": "Scooby Doo, Where Are You!"
  },
  {
    "popularity99": 71.0,
    "director": "Joy Batchelor",
    "genre": [
      "Animation",
      " Drama"
    ],
    "imdb_score": 7.1,
    "name": "Animal Farm"
  },
  {
    "popularity99": 48.0,
    "director": "Ray Enright",
    "genre": [
      "Comedy",
      " Music",
      " Romance",
      " Sport"
    ],
    "imdb_score": 4.8,
    "name": "Swing Your Lady"
  },
  {
    "popularity99": 78.0,
    "director": "George Stevens",
    "genre": [
      "Drama",
      " Western"
    ],
    "imdb_score": 7.8,
    "name": "Shane"
  },
  {
    "popularity99": 69.0,
    "director": "John G. Avildsen",
    "genre": [
      "Drama",
      " Family",
      " Sport"
    ],
    "imdb_score": 6.9,
    "name": "The Karate Kid"
  },
  {
    "popularity99": 86.0,
    "director": "Kevin McCarthy",
    "genre": [
      "Game-Show"
    ],
    "imdb_score": 8.6,
    "name": "Jeopardy!"
  },
  {
    "popularity99": 82.0,
    "director": "Norman Tokar",
    "genre": [
      "Comedy",
      " Family"
    ],
    "imdb_score": 8.2,
    "name": "Leave It to Beaver"
  },
  {
    "popularity99": 80.0,
    "director": "Arthur Penn",
    "genre": [
      "Biography",
      " Crime",
      " Drama",
      " Romance"
    ],
    "imdb_score": 8.0,
    "name": "Bonnie and Clyde"
  },
  {
    "popularity99": 89.0,
    "director": "Milos Forman",
    "genre": [
      "Drama"
    ],
    "imdb_score": 8.9,
    "name": "One Flew Over the Cuckoos Nest"
  },
  {
    "popularity99": 81.0,
    "director": "Dave Wilson",
    "genre": [
      "Comedy",
      " Music"
    ],
    "imdb_score": 8.1,
    "name": "Saturday Night Live"
  },
  {
    "popularity99": 88.0,
    "director": "Sergio Leone",
    "genre": [
      "Western"
    ],
    "imdb_score": 8.8,
    "name": "Cera una volta il West"
  },
  {
    "popularity99": 84.0,
    "director": "F.W. Murnau",
    "genre": [
      "Drama",
      " Romance"
    ],
    "imdb_score": 8.4,
    "name": "Sunrise : A Song of Two Humans"
  },
  {
    "popularity99": 82.0,
    "director": "Roger Allers",
    "genre": [
      "Animation",
      " Adventure",
      " Drama",
      " Family",
      " Musical"
    ],
    "imdb_score": 8.2,
    "name": "The Lion King"
  },
  {
    "popularity99": 75.0,
    "director": "Walt Disney",
    "genre": [
      "Animation",
      " Family",
      " Comedy",
      " Short"
    ],
    "imdb_score": 7.5,
    "name": "Plane Crazy"
  },
  {
    "popularity99": 64.0,
    "director": "Rob Klug",
    "genre": [
      "Documentary",
      " News"
    ],
    "imdb_score": 6.4,
    "name": "60 Minutes"
  },
  {
    "popularity99": 77.0,
    "director": "Stanley Kubrick",
    "genre": [
      "Drama",
      " Romance"
    ],
    "imdb_score": 7.7,
    "name": "Lolita"
  },
  {
    "popularity99": 83.0,
    "director": "John McTiernan",
    "genre": [
      "Action",
      " Crime",
      " Thriller"
    ],
    "imdb_score": 8.3,
    "name": "Die Hard"
  },
  {
    "popularity99": 82.0,
    "director": "Otto Preminger",
    "genre": [
      "Crime",
      " Film-Noir",
      " Mystery",
      " Romance",
      " Thriller"
    ],
    "imdb_score": 8.2,
    "name": "Laura"
  },
  {
    "popularity99": 73.0,
    "director": "Dennis Hopper",
    "genre": [
      "Crime",
      " Drama"
    ],
    "imdb_score": 7.3,
    "name": "Easy Rider"
  },
  {
    "popularity99": 80.0,
    "director": "Don Siegel",
    "genre": [
      "Horror",
      " Sci-Fi",
      " Thriller"
    ],
    "imdb_score": 8.0,
    "name": "Invasion of the Body Snatchers"
  },
  {
    "popularity99": 78.0,
    "director": "Alain Resnais",
    "genre": [
      "Drama",
      " Mystery",
      " Romance"
    ],
    "imdb_score": 7.8,
    "name": "Lanncca9e derniccacre ccca Marienbad"
  },
  {
    "popularity99": 68.0,
    "director": "Walter Grauman",
    "genre": [
      "Drama",
      " Thriller"
    ],
    "imdb_score": 6.8,
    "name": "Lady in a Cage"
  },
  {
    "popularity99": 76.0,
    "director": "Sam Raimi",
    "genre": [
      "Horror"
    ],
    "imdb_score": 7.6,
    "name": "The Evil Dead"
  },
  {
    "popularity99": 83.0,
    "director": "Bobby Quinn",
    "genre": [
      "Comedy",
      " Music",
      " Talk-Show"
    ],
    "imdb_score": 8.3,
    "name": "The Tonight Show Starring Johnny Carson"
  },
  {
    "popularity99": 66.0,
    "director": "Tony Scott",
    "genre": [
      "Action",
      " Drama",
      " Romance"
    ],
    "imdb_score": 6.6,
    "name": "Top Gun"
  },
  {
    "popularity99": 69.0,
    "director": "Lewis Gilbert",
    "genre": [
      "Action",
      " Adventure",
      " Sci-Fi",
      " Thriller"
    ],
    "imdb_score": 6.9,
    "name": "You Only Live Twice"
  },
  {
    "popularity99": 75.0,
    "director": "Terence Young",
    "genre": [
      "Action",
      " Adventure",
      " Romance",
      " Thriller"
    ],
    "imdb_score": 7.5,
    "name": "From Russia with Love"
  },
  {
    "popularity99": 81.0,
    "director": "Hollingsworth Morse",
    "genre": [
      "Adventure",
      " Western",
      " Family"
    ],
    "imdb_score": 8.1,
    "name": "The Lone Ranger"
  },
  {
    "popularity99": 52.0,
    "director": "Gerard Damiano",
    "genre": [
      "Adult",
      " Comedy"
    ],
    "imdb_score": 5.2,
    "name": "Deep Throat"
  },
  {
    "popularity99": 76.0,
    "director": "Samuel Fuller",
    "genre": [
      "Drama",
      " Mystery"
    ],
    "imdb_score": 7.6,
    "name": "Shock Corridor"
  },
  {
    "popularity99": 76.0,
    "director": "Robert Clouse",
    "genre": [
      "Action",
      " Crime",
      " Drama",
      " Thriller"
    ],
    "imdb_score": 7.6,
    "name": "Enter the Dragon"
  },
  {
    "popularity99": 78.0,
    "director": "John Sturges",
    "genre": [
      "Western",
      " Adventure",
      " Drama"
    ],
    "imdb_score": 7.8,
    "name": "The Magnificent Seven"
  },
  {
    "popularity99": 77.0,
    "director": "Josef von Sternberg",
    "genre": [
      "Crime",
      " Drama"
    ],
    "imdb_score": 7.7,
    "name": "Underworld"
  },
  {
    "popularity99": 73.0,
    "director": "John Ford",
    "genre": [
      "Western"
    ],
    "imdb_score": 7.3,
    "name": "She Wore a Yellow Ribbon"
  },
  {
    "popularity99": 67.0,
    "director": "Edouard Molinaro",
    "genre": [
      "Drama",
      " Thriller"
    ],
    "imdb_score": 6.7,
    "name": "Un dans la ville"
  },
  {
    "popularity99": 76.0,
    "director": "Tim Burton",
    "genre": [
      "Crime",
      " Drama",
      " Thriller"
    ],
    "imdb_score": 7.6,
    "name": "Batman"
  },
  {
    "popularity99": 74.0,
    "director": "Clyde Geronimi",
    "genre": [
      "Animation",
      " Family",
      " Fantasy",
      " Musical",
      " Romance"
    ],
    "imdb_score": 7.4,
    "name": "Cinderella"
  },
  {
    "popularity99": 55.0,
    "director": "Lee Sholem",
    "genre": [
      "Action",
      " Adventure",
      " Fantasy",
      " Romance"
    ],
    "imdb_score": 5.5,
    "name": "Tarzans Magic Fountain"
  },
  {
    "popularity99": 83.0,
    "director": "Fred Zinnemann",
    "genre": [
      "Drama",
      " Western"
    ],
    "imdb_score": 8.3,
    "name": "High Noon"
  },
  {
    "popularity99": 77.0,
    "director": "Leni Riefenstahl",
    "genre": [
      "Documentary",
      " War"
    ],
    "imdb_score": 7.7,
    "name": "Triumph des Willens"
  },
  {
    "popularity99": 84.0,
    "director": "Frank Capra",
    "genre": [
      "Drama"
    ],
    "imdb_score": 8.4,
    "name": "Mr. Smith Goes to Washington"
  },
  {
    "popularity99": 70.0,
    "director": "Randal Kleiser",
    "genre": [
      "Musical",
      " Romance"
    ],
    "imdb_score": 7.0,
    "name": "Grease"
  },
  {
    "popularity99": 81.0,
    "director": "D.W. Griffith",
    "genre": [
      "Drama",
      " History",
      " Romance"
    ],
    "imdb_score": 8.1,
    "name": "Intolerance : Loves Struggle Throughout the Ages"
  },
  {
    "popularity99": 84.0,
    "director": "Quentin Tarantino",
    "genre": [
      "Crime",
      " Mystery",
      " Thriller"
    ],
    "imdb_score": 8.4,
    "name": "Reservoir Dogs"
  },
  {
    "popularity99": 78.0,
    "director": "George Stevens",
    "genre": [
      "Drama",
      " Romance"
    ],
    "imdb_score": 7.8,
    "name": "A Place in the Sun"
  },
  {
    "popularity99": 85.0,
    "director": "Carol Reed",
    "genre": [
      "Film-Noir",
      " Mystery",
      " Thriller"
    ],
    "imdb_score": 8.5,
    "name": "The Third Man"
  },
  {
    "popularity99": 83.0,
    "director": "Charles Chaplin",
    "genre": [
      "Adventure",
      " Comedy",
      " Family",
      " Romance",
      " Western"
    ],
    "imdb_score": 8.3,
    "name": "The Gold Rush"
  },
  {
    "popularity99": 79.0,
    "director": "Cecil B. DeMille",
    "genre": [
      "Adventure",
      " Drama",
      " History"
    ],
    "imdb_score": 7.9,
    "name": "The Ten Commandments"
  },
  {
    "popularity99": 79.0,
    "director": "John Ford",
    "genre": [
      "Drama",
      " Western"
    ],
    "imdb_score": 7.9,
    "name": "My Darling Clementine"
  },
  {
    "popularity99": 87.0,
    "director": "Billy Wilder",
    "genre": [
      "Drama",
      " Film-Noir"
    ],
    "imdb_score": 8.7,
    "name": "Sunset Blvd."
  },
  {
    "popularity99": 63.0,
    "director": "Sean S. Cunningham",
    "genre": [
      "Horror",
      " Mystery",
      " Thriller"
    ],
    "imdb_score": 6.3,
    "name": "Friday the 13th"
  },
  {
    "popularity99": 83.0,
    "director": "John Sturges",
    "genre": [
      "Adventure",
      " Drama",
      " History",
      " War"
    ],
    "imdb_score": 8.3,
    "name": "The Great Escape"
  },
  {
    "popularity99": 70.0,
    "director": "Clint Eastwood",
    "genre": [
      "Crime",
      " Drama",
      " Romance",
      " Thriller"
    ],
    "imdb_score": 7.0,
    "name": "Play Misty for Me"
  },
  {
    "popularity99": 73.0,
    "director": "Cameron Crowe",
    "genre": [
      "Comedy",
      " Drama",
      " Romance",
      " Sport"
    ],
    "imdb_score": 7.3,
    "name": "Jerry Maguire"
  },
  {
    "popularity99": 73.0,
    "director": "Bretaigne Windust",
    "genre": [
      "Drama",
      " Crime",
      " Film-Noir"
    ],
    "imdb_score": 7.3,
    "name": "The Enforcer"
  },
  {
    "popularity99": 68.0,
    "director": "Richard Fleischer",
    "genre": [
      "Adventure",
      " Sci-Fi"
    ],
    "imdb_score": 6.8,
    "name": "Fantastic Voyage"
  },
  {
    "popularity99": 82.0,
    "director": "George Roy Hill",
    "genre": [
      "Adventure",
      " Crime",
      " Drama",
      " Western"
    ],
    "imdb_score": 8.2,
    "name": "Butch Cassidy and the Sundance Kid"
  },
  {
    "popularity99": 86.0,
    "director": "Bob Sweeney",
    "genre": [
      "Comedy",
      " Family"
    ],
    "imdb_score": 8.6,
    "name": "The Andy Griffith Show"
  },
  {
    "popularity99": 79.0,
    "director": "John Landis",
    "genre": [
      "Action",
      " Comedy",
      " Music",
      " Musical"
    ],
    "imdb_score": 7.9,
    "name": "The Blues Brothers"
  },
  {
    "popularity99": 86.0,
    "director": "Robert Zemeckis",
    "genre": [
      "Drama",
      " Romance"
    ],
    "imdb_score": 8.6,
    "name": "Forrest Gump"
  },
  {
    "popularity99": 84.0,
    "director": "Billy Wilder",
    "genre": [
      "Comedy"
    ],
    "imdb_score": 8.4,
    "name": "Some Like It Hot"
  },
  {
    "popularity99": 48.0,
    "director": "Bruce Gowers",
    "genre": [
      "Game-Show",
      " Music",
      " Reality-TV"
    ],
    "imdb_score": 4.8,
    "name": "American Idol : The Search for a Superstar"
  },
  {
    "popularity99": 88.0,
    "director": "David Fincher",
    "genre": [
      "Drama",
      " Mystery",
      " Thriller"
    ],
    "imdb_score": 8.8,
    "name": "Fight Club"
  },
  {
    "popularity99": 51.0,
    "director": "Jack Arnold",
    "genre": [
      "Horror",
      " Sci-Fi"
    ],
    "imdb_score": 5.1,
    "name": "Revenge of the Creature"
  },
  {
    "popularity99": 85.0,
    "director": "Roman Polanski",
    "genre": [
      "Drama",
      " Mystery",
      " Thriller"
    ],
    "imdb_score": 8.5,
    "name": "Chinatown"
  },
  {
    "popularity99": 81.0,
    "director": "Sam Peckinpah",
    "genre": [
      "Action",
      " Western"
    ],
    "imdb_score": 8.1,
    "name": "The Wild Bunch"
  },
  {
    "popularity99": 88.0,
    "director": "Peter Jackson",
    "genre": [
      "Action",
      " Adventure",
      " Fantasy"
    ],
    "imdb_score": 8.8,
    "name": "The Lord of the Rings : The Fellowship of the Ring"
  },
  {
    "popularity99": 79.0,
    "director": "Frank Lloyd",
    "genre": [
      "Adventure",
      " Drama",
      " History"
    ],
    "imdb_score": 7.9,
    "name": "Mutiny on the Bounty"
  },
  {
    "popularity99": 78.0,
    "director": "Luis el",
    "genre": [
      "Drama",
      " Romance"
    ],
    "imdb_score": 7.8,
    "name": "El"
  },
  {
    "popularity99": 84.0,
    "director": "Stanley Kubrick",
    "genre": [
      "Drama",
      " War"
    ],
    "imdb_score": 8.4,
    "name": "Full Metal Jacket"
  },
  {
    "popularity99": 55.0,
    "director": "Stanley Kramer",
    "genre": [
      "Action",
      " Adventure",
      " Drama",
      " Romance",
      " War"
    ],
    "imdb_score": 5.5,
    "name": "The Pride and the Passion"
  },
  {
    "popularity99": 80.0,
    "director": "Rob Reiner",
    "genre": [
      "Comedy",
      " Music"
    ],
    "imdb_score": 8.0,
    "name": "This Is Spinal Tap"
  },
  {
    "popularity99": 78.0,
    "director": "Anthony Mann",
    "genre": [
      "Western"
    ],
    "imdb_score": 7.8,
    "name": "Winchester 73"
  },
  {
    "popularity99": 88.0,
    "director": "Cliff Bole",
    "genre": [
      "Action",
      " Adventure",
      " Sci-Fi"
    ],
    "imdb_score": 8.8,
    "name": "Star Trek : The Next Generation"
  },
  {
    "popularity99": 73.0,
    "director": "Charles S. Dubin",
    "genre": [
      "Crime",
      " Drama",
      " Mystery"
    ],
    "imdb_score": 7.3,
    "name": "Kojak"
  },
  {
    "popularity99": 74.0,
    "director": "Yevgeni Bauer",
    "genre": [
      "Drama",
      " Short"
    ],
    "imdb_score": 7.4,
    "name": "Gryozy"
  },
  {
    "popularity99": 49.0,
    "director": "Gregory J. Bonann",
    "genre": [
      "Drama",
      " Action",
      " Adventure"
    ],
    "imdb_score": 4.9,
    "name": "Baywatch"
  },
  {
    "popularity99": 64.0,
    "director": "Gerald Potterton",
    "genre": [
      "Animation",
      " Action",
      " Adventure",
      " Comedy",
      " Crime",
      " Fantasy",
      " Horror",
      " Sci-Fi"
    ],
    "imdb_score": 6.4,
    "name": "Heavy Metal"
  },
  {
    "popularity99": 80.0,
    "director": "Robert Wise",
    "genre": [
      "Drama",
      " Sci-Fi",
      " Thriller"
    ],
    "imdb_score": 8.0,
    "name": "The Day the Earth Stood Still"
  },
  {
    "popularity99": 77.0,
    "director": "Burt Gillett",
    "genre": [
      "Animation",
      " Musical",
      " Family",
      " Comedy",
      " Short"
    ],
    "imdb_score": 7.7,
    "name": "Three Little Pigs"
  },
  {
    "popularity99": 78.0,
    "director": "William A. Wellman",
    "genre": [
      "Action",
      " Crime",
      " Drama"
    ],
    "imdb_score": 7.8,
    "name": "The Public Enemy"
  },
  {
    "popularity99": 71.0,
    "director": "Jim Sharman",
    "genre": [
      "Comedy",
      " Musical"
    ],
    "imdb_score": 7.1,
    "name": "The Rocky Horror Picture Show"
  },
  {
    "popularity99": 80.0,
    "director": "Barry Levinson",
    "genre": [
      "Drama"
    ],
    "imdb_score": 8.0,
    "name": "Rain Man"
  },
  {
    "popularity99": 80.0,
    "director": "Jean Vigo",
    "genre": [
      "Drama",
      " Romance"
    ],
    "imdb_score": 8.0,
    "name": "Latalante"
  },
  {
    "popularity99": 82.0,
    "director": "Ingmar Bergman",
    "genre": [
      "Drama",
      " Fantasy"
    ],
    "imdb_score": 8.2,
    "name": "Persona"
  },
  {
    "popularity99": 80.0,
    "director": "George A. Romero",
    "genre": [
      "Action",
      " Horror"
    ],
    "imdb_score": 8.0,
    "name": "Dawn of the Dead"
  },
  {
    "popularity99": 74.0,
    "director": "William F. Claxton",
    "genre": [
      "Action",
      " Comedy",
      " Drama",
      " Romance",
      " War",
      " Western"
    ],
    "imdb_score": 7.4,
    "name": "Bonanza"
  },
  {
    "popularity99": 68.0,
    "director": "Adrian Lyne",
    "genre": [
      "Drama",
      " Thriller"
    ],
    "imdb_score": 6.8,
    "name": "Fatal Attraction"
  },
  {
    "popularity99": 60.0,
    "director": "Edward L. Cahn",
    "genre": [
      "Horror",
      " Sci-Fi"
    ],
    "imdb_score": 6.0,
    "name": "It! The Terror from Beyond Space"
  },
  {
    "popularity99": 83.0,
    "director": "John Moffitt",
    "genre": [
      "Comedy",
      " Music"
    ],
    "imdb_score": 8.3,
    "name": "Toast of the Town"
  },
  {
    "popularity99": 79.0,
    "director": "William Friedkin",
    "genre": [
      "Action",
      " Crime",
      " Thriller"
    ],
    "imdb_score": 7.9,
    "name": "The French Connection"
  },
  {
    "popularity99": 73.0,
    "director": "Clyde Geronimi",
    "genre": [
      "Animation",
      " Adventure",
      " Family",
      " Fantasy",
      " Music"
    ],
    "imdb_score": 7.3,
    "name": "Peter Pan"
  },
  {
    "popularity99": 78.0,
    "director": "John Nicolella",
    "genre": [
      "Action",
      " Crime",
      " Drama",
      " Thriller"
    ],
    "imdb_score": 7.8,
    "name": "Miami Vice"
  },
  {
    "popularity99": 64.0,
    "director": "George Lucas",
    "genre": [
      "Action",
      " Adventure",
      " Fantasy",
      " Sci-Fi"
    ],
    "imdb_score": 6.4,
    "name": "Star Wars : Episode I - The Phantom Menace"
  },
  {
    "popularity99": 88.0,
    "director": "Martin Scorsese",
    "genre": [
      "Crime",
      " Drama",
      " Thriller"
    ],
    "imdb_score": 8.8,
    "name": "Goodfellas"
  },
  {
    "popularity99": 62.0,
    "director": "Michael Curtiz",
    "genre": [
      "Drama",
      " History"
    ],
    "imdb_score": 6.2,
    "name": "The Egyptian"
  },
  {
    "popularity99": 76.0,
    "director": "Michael OHerlihy",
    "genre": [
      "Crime",
      " Drama",
      " Mystery"
    ],
    "imdb_score": 7.6,
    "name": "Hawaii Five-O"
  },
  {
    "popularity99": 66.0,
    "director": "Dennis Donnelly",
    "genre": [
      "Action",
      " Adventure",
      " Crime",
      " Drama",
      " Mystery"
    ],
    "imdb_score": 6.6,
    "name": "Charlies Angels"
  }
]

url = "http://127.0.0.1:8000/movies/movies_api/movies_api/"
print(help(requests))