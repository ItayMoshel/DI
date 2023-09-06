const express = require('express');
const app = express();
const port = 8000

app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
})

app.get('/api/greetings', (req, res) => {
    const greeting = { message: 'Hello'};
    res.json(greeting);
})