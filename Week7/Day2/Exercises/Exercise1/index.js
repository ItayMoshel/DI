const h1Element = document.querySelector('h1');
console.log(h1Element.textContent);

const paragraphs = document.querySelectorAll('article p');
const lastParagraph = paragraphs[paragraphs.length - 1];
lastParagraph.remove();

const h2Element = document.querySelector('h2');
h2Element.addEventListener('click', () => {
    h2Element.style.backgroundColor = 'red';
});

const h3Element = document.querySelector('h3');
h3Element.addEventListener('click', () => {
    h3Element.style.display = 'none';
});

const boldButton = document.getElementById('boldButton');
boldButton.addEventListener('click', () => {
    paragraphs.forEach(paragraph => {
        paragraph.style.fontWeight = 'bold';
    });
});

h1Element.addEventListener('mouseover', () => {
    const randomSize = Math.floor(Math.random() * 101); // Random size between 0 and 100
    h1Element.style.fontSize = `${randomSize}px`;
});

const secondParagraph = paragraphs[1];
secondParagraph.addEventListener('mouseover', () => {
    secondParagraph.classList.add('fade-out');
});
