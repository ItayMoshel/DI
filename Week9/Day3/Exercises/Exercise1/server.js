const express = require('express');
const app = express();
const port = 3000;

app.use(express.json());

const blogPosts = [
  { id: 1, title: 'First Post', content: 'This is the first blog post.' 
},
  { id: 2, title: 'Second Post', content: 'This is the second blog post.' 
},
];


app.get('/posts', (req, res) => {
  res.json(blogPosts);
});


app.get('/posts/:id', (req, res) => {
  const postId = parseInt(req.params.id);
  const post = blogPosts.find((post) => post.id === postId);

  if (!post) {
    res.status(404).json({ error: 'Post not found' });
  } else {
    res.json(post);
  }
});


app.post('/posts', (req, res) => {
  const { title, content } = req.body;
  const postId = blogPosts.length + 1;
  const newPost = { id: postId, title, content };
  blogPosts.push(newPost);
  res.status(201).json(newPost);
});


app.put('/posts/:id', (req, res) => {
  const postId = parseInt(req.params.id);
  const updatedPost = req.body;
  const existingPost = blogPosts.find((post) => post.id === postId);

  if (!existingPost) {
    res.status(404).json({ error: 'Post not found' });
  } else {
    existingPost.title = updatedPost.title || existingPost.title;
    existingPost.content = updatedPost.content || existingPost.content;
    res.json(existingPost);
  }
});


app.delete('/posts/:id', (req, res) => {
  const postId = parseInt(req.params.id);
  const index = blogPosts.findIndex((post) => post.id === postId);

  if (index === -1) {
    res.status(404).json({ error: 'Post not found' });
  } else {
    blogPosts.splice(index, 1);
    res.status(204).send(); // No content, successful deletion
  }
});


app.use((req, res) => {
  res.status(404).json({ error: 'Not found' });
});


app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ error: 'Internal server error' });
});


app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
