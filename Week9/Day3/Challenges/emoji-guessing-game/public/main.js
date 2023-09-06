document.addEventListener('DOMContentLoaded', () => {
  let correctAnswer = '';
  let score = localStorage.getItem('score') || 0;
  const scoreSpan = document.getElementById('score');
  scoreSpan.textContent = score;

  async function initialize() {
    correctAnswer = await fetchEmojiAndOptions();
  }

  initialize();

  const form = document.getElementById('emojiForm');
  const feedback = document.getElementById('feedback');

  form.addEventListener('submit', async event => {
    event.preventDefault();

    const formData = new FormData(form);
    const guess = formData.get('emojiName');

    const res = await fetch('http://localhost:3000/guess', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ guess, correctAnswer }),
    });

    const data = await res.json();

    if (data.correct) {
      feedback.textContent = 'Correct!';
      score++;
      localStorage.setItem('score', score);
    } else {
      feedback.textContent = 'Incorrect!';
    }

    scoreSpan.textContent = score;
    correctAnswer = await fetchEmojiAndOptions();
  });

  async function fetchEmojiAndOptions() {
    const res = await fetch('http://localhost:3000/emoji');
    const data = await res.json();

    const emojiDiv = document.getElementById('emoji');
    const optionsDiv = document.getElementById('options');

    emojiDiv.textContent = data.randomEmoji.emoji;

    const allOptions = [...data.distractors, data.randomEmoji].sort(() => 0.5 - Math.random());

    optionsDiv.innerHTML = '';
    allOptions.forEach(option => {
      optionsDiv.innerHTML += `
        <label>
          <input type="radio" name="emojiName" value="${option.name}">
          ${option.name}
        </label><br>
      `;
    });

    return data.randomEmoji.name;
  }
});
