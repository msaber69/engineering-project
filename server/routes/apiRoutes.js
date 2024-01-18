// backend/routes/apiRoutes.js
const express = require('express');
const router = express.Router();

// Example user data (replace this with a database in a real application)
const users = [
  { id: 1, username: 'user1', password: 'password1' },
  { id: 2, username: 'user2', password: 'password2' },
];

// Route to handle user login
router.post('/login', (req, res) => {
  const { username, password } = req.body;

  // Simple authentication logic (replace this with actual authentication)
  const user = users.find((user) => user.username === username && user.password === password);

  if (user) {
    // Successful login
    res.json({ success: true, message: 'Login successful', user });
  } else {
    // Failed login
    res.status(401).json({ success: false, message: 'Invalid username or password' });
  }
});

module.exports = router;
