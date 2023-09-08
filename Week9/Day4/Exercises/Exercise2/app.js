const express = require('express');
const router = require("./routes/todos");
const app = express();
const port = 8000;

app.use(express.json);
app.use('/todos', router);
app.listen(port, () => {
    console.log(`Server is running at http://localhost:${port}`);
});
