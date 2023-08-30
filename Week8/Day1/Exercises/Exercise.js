// Exercise 1
person = {
    name: 'John Doe',
    age: 25,
    location: {
        country: 'Canada',
        city: 'Vancouver',
        coordinates: [49.2827, -123.1207]
    }
}
const {name, location: {country, city, coordinates: [lat, lng]}} = person;
console.log(`I am ${name} from ${city}, ${country}. Latitude(${lat}), Longitude(${lng})`);

// Exercise 2
function displayStudentInfo(objUser) {
    const { first, last } = objUser;
    
    const fullName = `${first} ${last}`;
    const output = `Your full name is ${fullName}`;
    
    return output;
}

const result = displayStudentInfo({ first: 'Elie', last: 'Schoppik' });

console.log(result);

// Exercise 3
// 1.
const users = { user1: 18273, user2: 92833, user3: 90315 };

const usersArray = Object.entries(users);
console.log(usersArray);

// 2.
const multipliedUsersArray = usersArray.map(([user, id]) => [user, id * 2]);
console.log(multipliedUsersArray);

// Exercise 4
// Output: object

// Exercise 5
class Dog {
    constructor(name) {
      this.name = name;
    }
  };
// Option 2
class Labrador extends Dog {
    constructor(name, size) {
      super(name);
      this.size = size;
    }
  }
  
// Exercise 6
// 1. both are False
// 2. objects 2 and 3 have the value of object 1, which is the number 4.
//    object 4 have the value of 5.
//    We set objects two and three to be equal to object one. and we set object one to have a value of 4.
//    Object 4 have the value of 5 and we dont change it.

// 3.
class Animal {
    constructor(name, type, color) {
        this.name = name;
        this.type = type;
        this.color = color;
    }
}

class Mammal extends Animal {
    sound(sound) {
        return `Moooo I'm a ${this.type}, named ${this.name} and I'm ${this.color}. ${sound}`;
    }
}

const farmerCow = new Mammal('Lily', 'cow', 'brown and white');
const soundOutput = farmerCow.sound('Moo');
console.log(soundOutput);

