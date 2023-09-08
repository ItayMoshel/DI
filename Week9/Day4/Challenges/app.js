const express = require('express');
const app = express();
const router = express.Router();

app.use(express.json());
app.use('/quiz', router);

const triviaQuestions = [
  {
    question: "What is the capital of France?",
    answer: "Paris",
  },
  {
    question: "Which planet is known as the Red Planet?",
    answer: "Mars",
  },
  {
    question: "What is the largest mammal in the world?",
    answer: "Blue whale",
  },
];

let score = 0;
let currentQuestionIndex = 0;

router.get('/', (req, res) => {
  if (currentQuestionIndex >= triviaQuestions.length) {
    return res.send("The quiz is over. Please check your score.");
  }
  
  res.json({
    question: triviaQuestions[currentQuestionIndex].question,
  });
});

router.post('/', (req, res) => {
  const userAnswer = req.body.answer;
  
  if (userAnswer === triviaQuestions[currentQuestionIndex].answer) {
    score++;
    res.json({ correct: true, message: "Correct answer!" });
  } else {
    res.json({ correct: false, message: "Wrong answer!" });
  }
  
  currentQuestionIndex++;
});

router.get('/score', (req, res) => {
  res.json({ score });
});

const port = 3000;
app.listen(port, () => {
  console.log(`Listening on port ${port}...`);
});
