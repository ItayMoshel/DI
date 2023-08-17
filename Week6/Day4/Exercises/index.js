const people = ["Greg", "Mary", "Devon", "James"];

// 1
people.shift();

// 2
const jamesIndex = people.indexOf("James");
if (jamesIndex !== -1) {
    people[jamesIndex] = "Jason";
}

// 3
const yourName = "Itay";
people.push(yourName);

// 4
const maryIndex = people.indexOf("Mary");
console.log("Mary's index:", maryIndex);

// 5
const peopleCopy = people.slice(1, -1);

// 6
const fooIndex = people.indexOf("Foo");
console.log("Index of 'Foo':", fooIndex);

// 7
const last = people[people.length - 1];

// 8
for (const person of people) {
    console.log(person);
}

// 9
for (const person of people) {
    console.log(person);
    if (person === "Devon") {
        break;
    }
}

// 10
const colors = ["blue", "red", "green", "purple", "yellow"];
const suffixes = ["st", "nd", "rd", "th", "th"];

for (let i = 0; i < colors.length; i++) {
    const suffixIndex = i > 2 ? 3 : i;
    console.log(`My ${i + 1}${suffixes[suffixIndex]} choice is ${colors[i]}`);
}


// 11
let userInput = prompt("Please enter a number:");
let number = parseFloat(userInput);

while (typeof number === "number" && number < 10) {
    userInput = prompt("Please enter a new number:");
    number = parseFloat(userInput);
}

console.log("Input is not a number or is greater than or equal to 10. Exiting loop.");


// 12
const building = {
    numberOfFloors: 4,
    numberOfAptByFloor: {
        firstFloor: 3,
        secondFloor: 4,
        thirdFloor: 9,
        fourthFloor: 2,
    },
    nameOfTenants: ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent:  {
        sarah: [3, 990],
        dan:  [4, 1000],
        david: [1, 500],
    },
}

console.log("Number of floors:", building.numberOfFloors);

console.log("Number of apartments on the first floor:", building.numberOfAptByFloor.firstFloor);
console.log("Number of apartments on the third floor:", building.numberOfAptByFloor.thirdFloor);

const secondTenant = building.nameOfTenants[1];
const secondTenantRooms = building.numberOfRoomsAndRent[secondTenant][0];
console.log(`Second tenant: ${secondTenant}, Number of rooms: ${secondTenantRooms}`);

const sarahRent = building.numberOfRoomsAndRent.sarah[1];
const davidRent = building.numberOfRoomsAndRent.david[1];
const danRent = building.numberOfRoomsAndRent.dan[1];

if (sarahRent + davidRent > danRent) {
    building.numberOfRoomsAndRent.dan[1] = 1200;
}

console.log("Updated Dan's rent:", building.numberOfRoomsAndRent.dan[1]);


// 13 
const family = {
    father: "John",
    mother: "Jane",
    son: "Jake",
    daughter: "Emily"
};

console.log("Keys of the family object:");
for (const key in family) {
    console.log(key);
}

console.log("Values of the family object:");
for (const key in family) {
    console.log(family[key]);
}


// 14
const details = {
    my: 'name',
    is: 'Rudolf',
    the: 'raindeer'
  };
  
  let output = '';
  
  for (const key in details) {
    output += details[key] + ' ';
  }
  
  console.log(output.trim());


// 15
  const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
const secretSocietyName = names.map(name => name[0]).sort().join('');

console.log(secretSocietyName);




  