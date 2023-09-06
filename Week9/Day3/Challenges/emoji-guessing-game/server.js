const express = require('express');
const bodyParser = require('body-parser');

const app = express();
app.use(bodyParser.json());
app.use(express.static('public'));

const port = 3000;

const emojis = [
  { emoji: '😀', name: 'grinning' },
  { emoji: '😃', name: 'smiley' },
  { emoji: '😄', name: 'smile' },
  { emoji: '😁', name: 'beaming' },
  { emoji: '😆', name: 'laughing' },
  { emoji: '😅', name: 'sweat_smile' },
  { emoji: '🤣', name: 'rofl' },
  { emoji: '😂', name: 'joy' },
  { emoji: '🙂', name: 'slightly_smiling_face' },
  { emoji: '🙃', name: 'upside_down' },
  { emoji: '😉', name: 'wink' },
  { emoji: '😊', name: 'blush' },
  { emoji: '😇', name: 'innocent' },
  { emoji: '🥰', name: 'smiling_face_with_hearts' },
  { emoji: '😍', name: 'heart_eyes' },
  { emoji: '🤩', name: 'star_struck' },
  { emoji: '😘', name: 'kissing_heart' },
  { emoji: '😗', name: 'kissing' },
  { emoji: '☺️', name: 'relaxed' },
  { emoji: '😚', name: 'kissing_closed_eyes' },
  { emoji: '😙', name: 'kissing_smiling_eyes' },
  { emoji: '😋', name: 'yum' },
  { emoji: '😛', name: 'stuck_out_tongue' },
  { emoji: '😜', name: 'stuck_out_tongue_winking_eye' },
  { emoji: '🤪', name: 'zany' },
  { emoji: '😝', name: 'stuck_out_tongue_closed_eyes' },
  { emoji: '🤑', name: 'money_mouth' },
  { emoji: '🤗', name: 'hugs' },
  { emoji: '🤭', name: 'hand_over_mouth' },
  { emoji: '🤫', name: 'shushing' },
  { emoji: '🤔', name: 'thinking' },
  { emoji: '🤐', name: 'zipper_mouth' },
  { emoji: '🤨', name: 'raised_eyebrow' },
  { emoji: '😐', name: 'neutral_face' },
  { emoji: '😑', name: 'expressionless' },
  { emoji: '😶', name: 'no_mouth' },
  { emoji: '😏', name: 'smirk' },
  { emoji: '😒', name: 'unamused' },
  { emoji: '🙄', name: 'eye_roll' },
  { emoji: '😬', name: 'grimacing' },
  { emoji: '🤥', name: 'lying' },
  { emoji: '😌', name: 'relieved' },
  { emoji: '😔', name: 'pensive' },
  { emoji: '😪', name: 'sleepy' },
  { emoji: '🤤', name: 'drooling' },
  { emoji: '😴', name: 'sleeping' },
  { emoji: '😷', name: 'mask' },
  { emoji: '🤒', name: 'thermometer_face' },
  { emoji: '🤕', name: 'head_bandage' },
  { emoji: '🤢', name: 'nauseated' }
];

function getRandomEmojiAndDistractors() {
  const randomIndex = Math.floor(Math.random() * emojis.length);
  const randomEmoji = emojis[randomIndex];

  const distractors = emojis
    .filter(e => e.name !== randomEmoji.name)
    .sort(() => 0.5 - Math.random())
    .slice(0, 3);

  return { randomEmoji, distractors };
}

app.get('/emoji', (req, res) => {
  res.json(getRandomEmojiAndDistractors());
});

app.post('/guess', (req, res) => {
  const userGuess = req.body.guess;
  const correctAnswer = req.body.correctAnswer;

  if (userGuess === correctAnswer) {
    res.json({ correct: true });
  } else {
    res.json({ correct: false });
  }
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}/`);
});
