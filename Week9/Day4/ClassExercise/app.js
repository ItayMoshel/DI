const express = require('express');
const app = express();
const port = 3000;


function datetimeMiddleware(req, res, next) {
  const currentDate = new Date();
  const date = currentDate.toDateString();
  const time = currentDate.toTimeString().split(' ')[0];

  req.currentDate = date;
  req.currentTime = time;

  next();
}

app.use(datetimeMiddleware);

app.get('/route1', (req, res) => {
  res.send(`Route 1 - Today's date is ${req.currentDate} and current time is ${req.currentTime}`);
});

app.get('/route2', datetimeMiddleware, (req, res) => {
  res.send(`Route 2 - Today's date is ${req.currentDate} and current time is ${req.currentTime}`);
});

app.listen(port, () => {
  console.log(`Server running on http://localhost:${port}`);
});
