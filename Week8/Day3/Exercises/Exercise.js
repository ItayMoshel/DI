// Exercise 1
const apiUrl = "https://api.giphy.com/v1/gifs/search?q=hilarious&rating=g&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My";

fetch(apiUrl)
  .then(response => {
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    return response.json();
  })
  .then(data => {
    console.log(data);
  })
  .catch(error => {
    console.error('Fetch error:', error);
  });

  // Exercise 2
  const apiKey = 'hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My';
const searchTerm = 'sun';
const startingPosition = 2;
const numberOfResults = 10;

const apiUrl2 = `https://api.giphy.com/v1/gifs/search?api_key=${apiKey}&q=${searchTerm}&offset=${startingPosition}&limit=${numberOfResults}`;

fetch(apiUrl2)
  .then(response => {
    if (!response.ok) {
      throw new Error(`Network response was not ok: ${response.status} ${response.statusText}`);
    }
    return response.json();
  })
  .then(data => {
    console.log(data);
  })
  .catch(error => {
    console.error('Fetch error:', error);
  });

  // Exercise 3
  async function fetchStarship() {
    try {
      const response = await fetch("https://www.swapi.tech/api/starships/9/");
      if (!response.ok) {
        throw new Error(`Network response was not ok: ${response.status} ${response.statusText}`);
      }
      const objectStarWars = await response.json();
      console.log(objectStarWars.result);
    } catch (error) {
      console.error('Fetch error:', error);
    }
  }
  
  fetchStarship();

  // Exercise 4
  function resolveAfter2Seconds() {
    return new Promise(resolve => {
        setTimeout(() => {
            resolve('resolved');
        }, 2000);
    });
}

async function asyncCall() {
    console.log('calling');
    let result = await resolveAfter2Seconds();
    console.log(result);
}

asyncCall();

//   'calling' will be logged to the console immediately.
// After a 2-second delay, 'resolved' will be logged to the console.