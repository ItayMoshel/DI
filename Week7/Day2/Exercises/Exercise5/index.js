document.addEventListener('DOMContentLoaded', () => {
    const myElement = document.getElementById('myElement');

    myElement.addEventListener('click', () => {
        const newX = Math.random() * (window.innerWidth - myElement.offsetWidth);
        myElement.style.left = `${newX}px`;
    });

    myElement.addEventListener('mouseover', () => {
        const newY = Math.random() * (window.innerHeight - myElement.offsetHeight);
        myElement.style.top = `${newY}px`;
    });

    myElement.addEventListener('mouseout', () => {
        const randomColor = getRandomColor();
        myElement.style.backgroundColor = randomColor;
    });

    myElement.addEventListener('dblclick', () => {
        const newSize = Math.floor(Math.random() * 50) + 10;
        myElement.style.fontSize = `${newSize}px`;
    });
});

function getRandomColor() {
    const letters = '0123456789ABCDEF';
    let color = '#';
    for (let i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}
