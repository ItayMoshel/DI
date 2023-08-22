// Exercise 1
function displayNumbersDivisible(divisor) {
  if (divisor <= 0) {
    console.log("Divisor should be a positive non-zero number.");
    return;
  }

  let sum = 0;

  for (let i = 0; i <= 500; i++) {
    if (i % divisor === 0) {
      console.log(i);
      sum += i;
    }
  }

  console.log("Sum of numbers divisible by", divisor, ":", sum);
}

displayNumbersDivisible(23);


// Exercise 2
const stock = {
  "banana": 6,
  "apple": 0,
  "pear": 12,
  "orange": 32,
  "blueberry": 1
};

const prices = {
  "banana": 4,
  "apple": 2,
  "pear": 1,
  "orange": 1.5,
  "blueberry": 10
};

const shoppingList = ["banana", "orange", "apple"];

function myBill() {
  let total = 0;

  for (const item of shoppingList) {
    if (item in stock && stock[item] > 0) {
      total += prices[item];
      stock[item] -= 1;
    }
  }

  return total;
}

const totalPrice = myBill();
console.log("Total Price:", totalPrice);
console.log("Updated Stock:", stock);


// Exercise 3
function changeEnough(itemPrice, amountOfChange) {
    const quarters = amountOfChange[0] * 0.25;
    const dimes = amountOfChange[1] * 0.10;
    const nickels = amountOfChange[2] * 0.05;
    const pennies = amountOfChange[3] * 0.01;
    
    const totalChange = quarters + dimes + nickels + pennies;
  
    return totalChange >= itemPrice;
  }
  
  console.log(changeEnough(4.25, [25, 20, 5, 0]));
  console.log(changeEnough(14.11, [2, 100, 0, 0]));
  console.log(changeEnough(0.75, [0, 0, 20, 5]));
  

  // Exercise 4
  function hotelCost() {
    let nights = parseInt(prompt("How many nights would you like to stay in the hotel?"));
    
    while (isNaN(nights)) {
      nights = parseInt(prompt("Please enter a valid number for the number of nights."));
    }
    
    const hotelPricePerNight = 140;
    return nights * hotelPricePerNight;
  }
  
  function planeRideCost() {
    let destination = prompt("Where would you like to go?").toLowerCase();
  
    while (destination !== "london" && destination !== "paris" && destination !== "") {
      destination = prompt("Please enter a valid destination (London, Paris, or leave blank).").toLowerCase();
    }
  
    switch (destination) {
      case "london":
        return 183;
      case "paris":
        return 220;
      default:
        return 300;
    }
  }
  
  function rentalCarCost() {
    let days = parseInt(prompt("How many days would you like to rent the car?"));
  
    while (isNaN(days)) {
      days = parseInt(prompt("Please enter a valid number for the number of days."));
    }
  
    const dailyCarPrice = 40;
    let totalCarPrice = days * dailyCarPrice;
  
    if (days > 10) {
      totalCarPrice *= 0.95;
    }
  
    return totalCarPrice;
  }
  
  function totalVacationCost() {
    const hotel = hotelCost();
    const plane = planeRideCost();
    const car = rentalCarCost();
  
    const totalCost = hotel + plane + car;
    
    console.log(`The hotel cost: $${hotel}, the plane tickets cost: $${plane}, the car rental cost: $${car}.`);
    console.log(`Total vacation cost: $${totalCost}`);
  }
  
  totalVacationCost();
  

// Exercise 5/6/7 is in a subfolder.
