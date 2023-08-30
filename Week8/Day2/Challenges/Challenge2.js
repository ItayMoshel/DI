const morse = `{
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-"
  }`
  
  function toJs() {
    return new Promise((resolve, reject) => {
      try {
        const morseObj = JSON.parse(morse);
        if (Object.keys(morseObj).length === 0) {
          reject(new Error("Morse object is empty"));
        } else {
          resolve(morseObj);
        }
      } catch (error) {
        reject(error);
      }
    });
  }
  
  function toMorse(morseJS) {
    return new Promise((resolve, reject) => {
      const userInput = prompt("Enter a word or sentence:");
      if (!userInput) {
        reject(new Error("No input provided"));
      } else {
        const morseTranslation = [];
        const sanitizedInput = userInput.toLowerCase();
        for (const char of sanitizedInput) {
          if (char in morseJS) {
            morseTranslation.push(morseJS[char]);
          } else {
            reject(new Error(`Character '${char}' not found in Morse object`));
            return;
          }
        }
        resolve(morseTranslation);
      }
    });
  }
  
  function joinWords(morseTranslation) {
    const morseText = morseTranslation.join(" ");
    const translatedElement = document.createElement("p");
    translatedElement.textContent = morseText;
    document.body.appendChild(translatedElement);
  }
  
  toJs()
    .then(morseJS => toMorse(morseJS))
    .then(morseTranslation => joinWords(morseTranslation))
    .catch(error => console.error("Error:", error));
  