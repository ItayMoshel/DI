const board = document.getElementById('board');
const playerXButton = document.getElementById('playerX');
const playerOButton = document.getElementById('playerO');
const restartButton = document.getElementById('restart');
const resetScoreButton = document.getElementById('reset-score');
const xScoreElement = document.getElementById('x-score');
const oScoreElement = document.getElementById('o-score');

let currentPlayer = '';
let computerPlayer = '';
let cells = Array.from({ length: 9 }, () => '');
const winCombos = [
  [0, 1, 2],
  [3, 4, 5],
  [6, 7, 8],
  [0, 3, 6],
  [1, 4, 7],
  [2, 5, 8],
  [0, 4, 8],
  [6, 4, 2]
];

let gameEnded = false;
let xScore = 0;
let oScore = 0;

playerXButton.addEventListener('click', () => {
  if (gameEnded) return;
  currentPlayer = 'X';
  computerPlayer = 'O';
  initializeGame();
});

playerOButton.addEventListener('click', () => {
  if (gameEnded) return;
  currentPlayer = 'O';
  computerPlayer = 'X';
  initializeGame();
});

restartButton.addEventListener('click', initializeGame);

resetScoreButton.addEventListener('click', () => {
  xScore = 0;
  oScore = 0;
  updateScores();
});

function initializeGame() {
  gameEnded = false;
  cells = Array.from({ length: 9 }, () => '');
  board.innerHTML = '';
  restartButton.style.display = 'none';
  buildBoard();
}

function buildBoard() {
  for (let i = 0; i < 9; i++) {
    const cell = document.createElement('div');
    cell.classList.add('cell');
    cell.dataset.index = i;
    cell.addEventListener('click', handleCellClick);
    board.appendChild(cell);
  }
}

function handleCellClick(event) {
  if (gameEnded) return;

  const clickedCell = event.target;
  const index = clickedCell.dataset.index;

  if (!cells[index]) {
    cells[index] = currentPlayer;
    clickedCell.textContent = currentPlayer;
    checkWinner();
    currentPlayer = currentPlayer === 'X' ? 'O' : 'X';
    computerMove();
  }
}

function checkWinner() {
  for (const combo of winCombos) {
    const [a, b, c] = combo;
    if (cells[a] && cells[a] === cells[b] && cells[a] === cells[c]) {
      displayResult(cells[a] + ' wins!');
      return;
    }
  }
  if (cells.every(cell => cell !== '')) {
    displayResult('Tie game');
  }
}

function displayResult(message) {
  gameEnded = true;
  if (message.includes('X wins')) {
    xScore++;
  } else if (message.includes('O wins')) {
    oScore++;
  }
  updateScores();
  restartButton.style.display = 'block';
  const resultElement = document.createElement('div');
  resultElement.textContent = message;
  resultElement.classList.add('result');
  board.appendChild(resultElement);
}

function updateScores() {
  xScoreElement.textContent = `X: ${xScore}`;
  oScoreElement.textContent = `O: ${oScore}`;
}
