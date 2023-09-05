const greet = require('./greeting');
const displayColorfulMessage = require('./colorful-message');
const readFile = require('./files/read-file');

const userName = 'Itay';

const greetingMessage = greet(userName);

console.log(greetingMessage);

displayColorfulMessage();

readFile();
