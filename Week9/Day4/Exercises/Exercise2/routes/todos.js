const express = require('express');
const router = express.Router();
const todos = [];

router.get('/', (req, res) => {
    res.json(todos);
});

router.post('/', (req, res) => {
    const newItem = req.body;
    newItem.id = todos.length + 1;
    todos.push(newItem);
    res.json(newItem);
});

router.put('/:id', (req, res) => {
    const id = parseInt(req.params.id);
    const updatedItem = req.body;
    const index = todos.findIndex(todo => todo.id === id);
    
    if (index >= 0) {
      todos[index] = { ...todos[index], ...updatedItem, id: id };
      res.json(todos[index]);
    } else {
      res.status(404).json({ message: 'Item not found' });
    }
  });
  
router.delete('/:id', (req, res) => {
    const id = parseInt(req.params.id);
    const index = todos.findIndex(todo => todo.id === id);

    if (index >= 0) {
        const removedItem = todos.splice(index, 1);
        res.json(removedItem[0]);
    } else {
        res.status(404).json({ message: 'Item not found' });
    }
});
  
  module.exports = router;
