function makeAllCaps(words) {
    return new Promise((resolve, reject) => {
      const uppercasedWords = words.map(word => {
        if (typeof word === 'string') {
          return word.toUpperCase();
        } else {
          reject('All elements in the array must be strings.');
        }
      });
      
      resolve(uppercasedWords);
    });
  }
  
  function sortWords(uppercasedWords) {
    return new Promise((resolve, reject) => {
      if (uppercasedWords.length > 4) {
        resolve(uppercasedWords.sort());
      } else {
        reject('Array length must be bigger than 4.');
      }
    });
  }
  
  makeAllCaps([1, "pear", "banana"])
    .then((arr) => sortWords(arr))
    .then((result) => console.log(result))
    .catch(error => console.log(error));
  
  makeAllCaps(["apple", "pear", "banana"])
    .then((arr) => sortWords(arr))
    .then((result) => console.log(result))
    .catch(error => console.log(error));
  
  makeAllCaps(["apple", "pear", "banana", "melon", "kiwi"])
    .then((arr) => sortWords(arr))
    .then((result) => console.log(result))
    .catch(error => console.log(error));
  