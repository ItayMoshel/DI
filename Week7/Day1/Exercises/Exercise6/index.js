const navBar = document.getElementById("navBar");
navBar.setAttribute("id", "socialNetworkNavigation");

const newListItem = document.createElement("li");
const logoutText = document.createTextNode("Logout");
newListItem.appendChild(logoutText);
navBar.firstElementChild.appendChild(newListItem);

const firstLinkText = navBar.firstElementChild.firstElementChild.textContent;
const lastLinkText = navBar.firstElementChild.lastElementChild.textContent;
console.log("First Link:", firstLinkText);
console.log("Last Link:", lastLinkText);
