const hhttp = require('http');
const json =
{
    "menu": {
        "firstCourse": "Vegetable Soup",
        "mainCourse": "Hamburger",
        "dessert": "Fruit salad"
    }
}
const server = hhttp.createServer((req, res) => {
    if (req.url == '/') {
        res.writeHead(200, { 'Content-Type': 'text/html'});
        res.end("<h1>Hello</h1>");
    } else if (req.url == '/home') {
        res.end("<h1>Welcom</h1>");
    } else if (req.url == '/menu') {
        res.writeHead(200, { 'Content-Type': 'application/json'})
        res.end(JSON.stringify(json));
    } else {
        res.end("NOT FOUND");
    }


})
server.listen(8000, 'localhost', () => {
    console.log("Awating orders!");
})