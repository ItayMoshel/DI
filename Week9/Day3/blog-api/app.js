const express = require('express');
const app = express();
const port = 3000;
const posts = require('./data');


app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});


app.get('/api/posts', (req, res) => {
  res.json(posts);
});


app.get('/api/posts/:postID', (req, res) => {
  const postID = parseInt(req.params.postID);
  const post = posts.find((post) => post.id === postID);

  if (!post) {
    res.status(404).json({ message: 'Post not found' });
  } else {
    res.json(post);
  }
});


app.get('/api/search', (req, res) => {
  const { title } = req.query;
  const filteredPosts = posts.filter((post) =>
    post.title.toLowerCase().includes(title.toLowerCase())
  );

  if (filteredPosts.length === 0) {
    res.json({ message: 'No matching posts found' });
  } else {
    res.json(filteredPosts);
  }
});
