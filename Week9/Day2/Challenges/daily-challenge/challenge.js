// const greet = require('./greeting');
// const displayColorfulMessage = require('./colorful-message');
// const readFile = require('./files/read-file');
import greet from './greeting.js';
import displayColorfulMessage from './colorful-message.js';
import readFile from './files/read-file.js';

const userName = 'Itay';

const greetingMessage = greet(userName);

console.log(greetingMessage);

displayColorfulMessage();

readFile();
