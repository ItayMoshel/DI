const express = require('express');
const bodyParser = require('body-parser');
const fs = require('fs');
const path = require('path');

const app = express();
app.use(bodyParser.json());

const tasksFilePath = path.join(__dirname, 'tasks.json');

const router = express.Router();

router.get('/tasks', (req, res) => {
  fs.readFile(tasksFilePath, 'utf8', (err, data) => {
    if (err) {
      return res.status(500).send({ error: 'Failed to read tasks' });
    }
    res.send(JSON.parse(data));
  });
});

router.get('/tasks/:id', (req, res) => {
  const taskId = req.params.id;
  fs.readFile(tasksFilePath, 'utf8', (err, data) => {
    if (err) {
      return res.status(500).send({ error: 'Failed to read tasks' });
    }
    const tasks = JSON.parse(data);
    const task = tasks.find(t => t.id === taskId);
    if (!task) {
      return res.status(404).send({ error: 'Task not found' });
    }
    res.send(task);
  });
});

router.post('/tasks', (req, res) => {
  const { id, description } = req.body;

  if (!id || !description) {
    return res.status(400).send({ error: 'Task ID and description are required' });
  }

  fs.readFile(tasksFilePath, 'utf8', (err, data) => {
    if (err) {
      return res.status(500).send({ error: 'Failed to read tasks' });
    }
    const tasks = JSON.parse(data);
    tasks.push({ id, description });
    fs.writeFile(tasksFilePath, JSON.stringify(tasks), (err) => {
      if (err) {
        return res.status(500).send({ error: 'Failed to write tasks' });
      }
      res.status(201).send({ id, description });
    });
  });
});

router.put('/tasks/:id', (req, res) => {
  const taskId = req.params.id;
  const { description } = req.body;

  if (!description) {
    return res.status(400).send({ error: 'New description is required' });
  }

  fs.readFile(tasksFilePath, 'utf8', (err, data) => {
    if (err) {
      return res.status(500).send({ error: 'Failed to read tasks' });
    }
    const tasks = JSON.parse(data);
    const taskIndex = tasks.findIndex(t => t.id === taskId);

    if (taskIndex === -1) {
      return res.status(404).send({ error: 'Task not found' });
    }

    tasks[taskIndex].description = description;
    fs.writeFile(tasksFilePath, JSON.stringify(tasks), (err) => {
      if (err) {
        return res.status(500).send({ error: 'Failed to update task' });
      }
      res.send(tasks[taskIndex]);
    });
  });
});

router.delete('/tasks/:id', (req, res) => {
  const taskId = req.params.id;
  fs.readFile(tasksFilePath, 'utf8', (err, data) => {
    if (err) {
      return res.status(500).send({ error: 'Failed to read tasks' });
    }
    const tasks = JSON.parse(data);
    const taskIndex = tasks.findIndex(t => t.id === taskId);

    if (taskIndex === -1) {
      return res.status(404).send({ error: 'Task not found' });
    }

    tasks.splice(taskIndex, 1);
    fs.writeFile(tasksFilePath, JSON.stringify(tasks), (err) => {
      if (err) {
        return res.status(500).send({ error: 'Failed to delete task' });
      }
      res.status(200).send({ message: 'Task deleted' });
    });
  });
});

app.use('/api', router);

const PORT = process.env.PORT || 8000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

