const express = require('express');
const bodyParser = require('body-parser');
const bcrypt = require('bcryptjs');
const fs = require('fs');

const app = express();

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static('public'));
const USERS_FILE = './users.json';

if (!fs.existsSync(USERS_FILE)) {
    fs.writeFileSync(USERS_FILE, JSON.stringify([]));
}

const router = express.Router();

router.post('/register', (req, res) => {
    const { name, lastName, email, username, password } = req.body;

    const users = JSON.parse(fs.readFileSync(USERS_FILE));

    const existingUser = users.find(user => user.username === username || user.email === email);

    if (existingUser) {
        return res.send('error1');
    }

    const hashedPassword = bcrypt.hashSync(password, 10);

    const newUser = {
        id: users.length + 1,
        name,
        lastName,
        email,
        username,
        password: hashedPassword
    };

    users.push(newUser);

    fs.writeFileSync(USERS_FILE, JSON.stringify(users));

    res.send('register');
});

router.post('/login', (req, res) => {
    const { username, password } = req.body;

    const users = JSON.parse(fs.readFileSync(USERS_FILE));

    const user = users.find(user => user.username === username);

    if (!user || !bcrypt.compareSync(password, user.password)) {
        return res.send('error2');
    }

    res.send('login');
});

router.get('/users', (req, res) => {
    const users = JSON.parse(fs.readFileSync(USERS_FILE));
    res.json(users);
});

router.get('/users/:id', (req, res) => {
    const users = JSON.parse(fs.readFileSync(USERS_FILE));
    const user = users.find(user => user.id == req.params.id);
    if (user) {
        res.json(user);
    } else {
        res.status(404).send('User not found.');
    }
});

router.put('/users/:id', (req, res) => {
    const users = JSON.parse(fs.readFileSync(USERS_FILE));
    const index = users.findIndex(user => user.id == req.params.id);

    if (index !== -1) {
        const updatedUser = { ...users[index], ...req.body };
        users[index] = updatedUser;
        fs.writeFileSync(USERS_FILE, JSON.stringify(users));
        res.json(updatedUser);
    } else {
        res.status(404).send('User not found.');
    }
});

app.use('/', router);

const PORT = 8000;
app.listen(PORT, () => {
    console.log(`Server started on http://localhost:${PORT}`);
});

