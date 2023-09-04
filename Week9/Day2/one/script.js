// const fs = require('fs');

// fs.readFile('menu.txt', 'utf-8', function (err, data) {
//     if (err) {
//         console.error(err)
//         return
//     }
//     console.log(data);
// });

// console.log("-----Restaurant Menu---------", '\n',);
// const fs = require("fs").promises;

// const start = async () => {
//   const data = await fs.readFile("menu.txt", "utf8");
//   console.log(data);
// };

// start();
// const fs = require('fs');
// //new content
// const newContent = "House Salad"

// //writeFile method
// fs.writeFile('menu.txt', newContent, function (err) {
//     if (err) {
//         console.error(err)
//         return
//     }
// });

// //readFile method
// fs.readFile('menu.txt', 'utf-8', function (err, data) {
//     if (err) {
//         console.error(err)
//         return
//     }

//     console.log(data)
// });

// console.log("-----Restaurant Menu---------", '\n',);
const fs = require('fs');
const newContent = "Caesar Salad"

fs.appendFile('menu.txt',newContent + '\n', function (err) {
    if (err) {
        console.error(err)
        return
    }
});

fs.readFile('menu.txt', 'utf-8', function (err, data) {
    if (err) {
        console.error(err)
        return
    }

    console.log(data)
});

console.log("-----Restaurant Menu---------", '\n',);
