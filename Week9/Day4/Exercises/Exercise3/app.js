const express = require('express');
const app = express();
const port = 3000;
const bookRouter = require('./routes/books');

app.use(express.json());
app.use('/books', bookRouter);

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
