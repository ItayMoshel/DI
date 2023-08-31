const fetchButton = document.getElementById("fetch-character");
const characterInfo = document.getElementById("character-info");
const loadingDiv = document.getElementById("loading");

fetchButton.addEventListener("click", fetchCharacter);
async function fetchCharacter() {
    loadingDiv.classList.remove("hidden");
    fetchButton.disabled = true;

    const randomNumber = Math.floor(Math.random() * 83) + 1;
    const response = await fetch(`https://www.swapi.tech/api/people/${randomNumber}`);
    const data = await response.json();

    displayCharacter(data.result.properties);
}
function displayCharacter(character) {
    characterInfo.innerHTML = `
        <h2>${character.name}</h2>
        <p>Height: ${character.height}</p>
        <p>Gender: ${character.gender}</p>
        <p>Birth Year: ${character.birth_year}</p>
    `;

    fetchHomeworld(character.homeworld);
}
async function fetchHomeworld(homeworldURL) {
    if (homeworldURL === "unknown") {
        loadingDiv.classList.add("hidden");
        fetchButton.disabled = false;
        return;
    }

    try {
        const response = await fetch(homeworldURL);
        const data = await response.json();
        const homeworld = data.result.properties.name;

        characterInfo.innerHTML += `<p>Homeworld: ${homeworld}</p>`;
    } catch (error) {
        characterInfo.innerHTML += `<p>Error fetching homeworld data.</p>`;
    }

    loadingDiv.classList.add("hidden");
    fetchButton.disabled = false;
}
loadingDiv.classList.add("hidden");
