const apiKey = "hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My";
const gifForm = document.getElementById("gifForm");
const categoryInput = document.getElementById("categoryInput");
const gifContainer = document.getElementById("gifContainer");
const deleteAllButton = document.getElementById("deleteAll");

gifForm.addEventListener("submit", async (event) => {
  event.preventDefault();
  const category = categoryInput.value.trim();
  if (category !== "") {
    try {
      const gifData = await fetchGif(category);
      const gifUrl = gifData.images.original.url;
      appendGif(category, gifUrl);
      categoryInput.value = "";
    } catch (error) {
      console.error("Error fetching GIF:", error);
    }
  }
});

deleteAllButton.addEventListener("click", () => {
  gifContainer.innerHTML = "";
});

function fetchGif(category) {
  const apiUrl = `https://api.giphy.com/v1/gifs/random?api_key=${apiKey}&tag=${category}`;
  return fetch(apiUrl)
    .then((response) => response.json())
    .then((data) => data.data)
    .catch((error) => {
      throw error;
    });
}

function appendGif(category, gifUrl) {
  const gifElement = document.createElement("div");
  gifElement.className = "gif";
  gifElement.innerHTML = `
    <img src="${gifUrl}" alt="${category}">
    <button class="deleteButton">Delete</button>
  `;
  gifContainer.appendChild(gifElement);

  const deleteButton = gifElement.querySelector(".deleteButton");
  deleteButton.addEventListener("click", () => {
    gifContainer.removeChild(gifElement);
  });
}
