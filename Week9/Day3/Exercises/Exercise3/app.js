const { fetchPosts } = require('./data/dataService');
const express = require('express');
const app = express();
const port = 8000;

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});

app.get('/api/posts', async (req, res) => {
  try {
    const posts = await fetchPosts();
    res.json(posts);
    console.log('Data successfully retrieved and sent as a response.');
  } catch (error) {
    console.error('Error fetching data:', error.message);
    res.status(500).json({ error: 'Internal server error' });
  }
});



