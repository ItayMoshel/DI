const containerDiv = document.getElementById("container");
console.log(containerDiv);

const peteLi = document.querySelector(".list:nth-child(1) li:nth-child(2)");
peteLi.textContent = "Richard";

const secondUl = document.querySelector(".list:nth-child(2)");
const secondLi = secondUl.querySelector("li:nth-child(2)");
secondUl.removeChild(secondLi);

const listElements = document.querySelectorAll(".list li");
for (const li of listElements) {
  li.textContent = "Itay Moshel";
}

const ulElements = document.querySelectorAll(".list");
for (const ul of ulElements) {
  ul.classList.add("student_list");
}
document.querySelector(".list:nth-child(1)").classList.add("university", "attendance");

containerDiv.style.backgroundColor = "lightblue";
containerDiv.style.padding = "10px";
document.querySelector(".list:nth-child(1) li:last-child").style.display = "none";
document.querySelector(".list:nth-child(1) li:nth-child(2)").style.border = "1px solid black";
document.body.style.fontSize = "16px";

if (containerDiv.style.backgroundColor === "lightblue") {
  const userList = document.querySelectorAll(".list li");
  let users = "";
  for (const user of userList) {
    users += user.textContent + " and ";
  }
  users = users.slice(0, -5);
  alert(`Hello ${users}`);
}
