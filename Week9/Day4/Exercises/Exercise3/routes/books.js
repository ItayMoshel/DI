const express = require('express');
const router = express.Router();
const books = [];


router.get('/', (req, res) => {
  res.json(books);
});

router.post('/', (req, res) => {
  const newBook = req.body;
  newBook.id = books.length + 1;
  books.push(newBook);
  res.json(newBook);
});

router.put('/:id', (req, res) => {
  const id = parseInt(req.params.id);
  const updatedBook = req.body;
  const index = books.findIndex(book => book.id === id);

  if (index >= 0) {
    books[index] = { ...books[index], ...updatedBook, id: id };
    res.json(books[index]);
  } else {
    res.status(404).json({ message: 'Book not found' });
  }
});

router.delete('/:id', (req, res) => {
  const id = parseInt(req.params.id);
  const index = books.findIndex(book => book.id === id);

  if (index >= 0) {
    const removedBook = books.splice(index, 1);
    res.json(removedBook[0]);
  } else {
    res.status(404).json({ message: 'Book not found' });
  }
});

module.exports = router;
