const _ = require('lodash');
const math = require('./math');
const result1 = math.add(5, 3);
const result2 = math.multiply(4, 6);
const result3 = _.sum([1, 2, 3, 4, 5]);

console.log('Result of addition:', result1);
console.log('Result of multiplication:', result2);
console.log('Sum using lodash:', result3);
