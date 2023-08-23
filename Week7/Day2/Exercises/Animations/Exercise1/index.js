// Part I
setTimeout(function() {
    alert("Hello World");
}, 2000);

// Part II
setTimeout(function() {
    var container = document.getElementById("container");
    var paragraph = document.createElement("p");
    paragraph.textContent = "Hello World";
    container.appendChild(paragraph);
}, 2000);

// Part III
var intervalId = setInterval(function() {
    var container = document.getElementById("container");
    var paragraph = document.createElement("p");
    paragraph.textContent = "Hello World";
    container.appendChild(paragraph);

    if (container.querySelectorAll("p").length === 5) {
        clearInterval(intervalId);
    }
}, 2000);

// Clear Interval Button
var clearButton = document.getElementById("clear");
clearButton.addEventListener("click", function() {
    clearInterval(intervalId);
});
