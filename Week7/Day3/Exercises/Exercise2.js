// Exercise 2
const winBattle = () => true;

const experiencePoints = winBattle() ? 10 : 1;

console.log(experiencePoints);

// Exercise 3
const isString = value => typeof value === 'string';

console.log(isString('hello'));
console.log(isString([1, 2, 4, 0]));

// Exercise 4
const add = (a, b) => a + b;

console.log(add(5, 7));
console.log(add(10, -3));

// Exercise 5

function kgToGramsDeclaration(weightInKg) {
    return weightInKg * 1000;
}

console.log(kgToGramsDeclaration(2));

const kgToGramsExpression = function(weightInKg) {
    return weightInKg * 1000;
};

console.log(kgToGramsExpression(2));

const kgToGramsArrow = weightInKg => weightInKg * 1000;

console.log(kgToGramsArrow(2));

// Function declarations are hoisted, 
// function expressions are not hoisted, so they can only be called after they are assigned a value

// Exercise 6
(function(numberOfChildren, partnerName, geographicLocation, jobTitle) {
    const sentence = `You will be a ${jobTitle} in ${geographicLocation}, and married to ${partnerName} with ${numberOfChildren} kids.`;

    console.log(sentence);
})(3, "Emma", "New York", "Software Engineer");
