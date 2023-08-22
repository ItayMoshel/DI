document.addEventListener("DOMContentLoaded", function() {
    const planetsData = [
      { name: "Mercury", color: "gray", moons: 0 },
      { name: "Venus", color: "orange", moons: 1 },
      { name: "Earth", color: "blue", moons: 2 },
      { name: "Mars", color: "red", moons: 3 },
      { name: "Jupiter", color: "orange", moons: 4 },
      { name: "Saturn", color: "gold", moons: 5 },
      { name: "Uranus", color: "lightblue", moons: 6 },
      { name: "Neptune", color: "blue", moons: 7 }
    ];
  
    const listPlanets = document.querySelector(".listPlanets");
  
    planetsData.forEach(planetData => {
      const planetDiv = document.createElement("div");
      planetDiv.className = "planet " + planetData.name.toLowerCase();
      planetDiv.style.backgroundColor = planetData.color;
      
      if (planetData.moons > 0) {
        for (let i = 1; i <= planetData.moons; i++) {
          const moonDiv = document.createElement("div");
          moonDiv.className = "moon";
          moonDiv.style.left = `${10 + i * 40}px`;
          moonDiv.style.top = `${10 + i * 40}px`;
          planetDiv.appendChild(moonDiv);
        }
      }
      
      listPlanets.appendChild(planetDiv);
    });
  });
  