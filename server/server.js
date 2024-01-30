const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const { sequelize } = require('./config/dbConfig');
const User = require('./models/UserModel');
const { spawn } = require('child_process');


const app = express();
const port = 3001;

app.use(cors());
app.use(bodyParser.json());

// Endpoint to handle login requests
app.post('/login', async (req, res) => {
    const { email, password } = req.body;

    try {
        // Query the database to check if the user exists with the provided credentials
        const user = await User.findOne({ where: { email, password } });

        if (user) {
            // User exists and credentials are correct, redirect to the home page
            res.redirect('/home');
        } else {
            // User does not exist or credentials are incorrect
            res.status(401).json({ error: 'Invalid email or password' });
        }
    } catch (error) {
        console.error('Error:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

// Endpoint to handle test submission
app.post('/submitTest', (req, res) => {
    // Retrieve submitted data from the request body
    const formData = req.body;

    // Spawn a Python process to execute the script with the form data as JSON
    const pythonProcess = spawn('python3', ['../pythonApi/app.py']);

    // Send the form data as JSON to the Python script's stdin
    pythonProcess.stdin.write(JSON.stringify(formData));
    pythonProcess.stdin.end();

    pythonProcess.stdout.on('data', (data) => {
        console.log(`Python stdout: ${data}`);
    });

    pythonProcess.stderr.on('data', (data) => {
        console.error(`Python stderr: ${data}`);
    });

    pythonProcess.on('close', (code) => {
        console.log(`Python process exited with code ${code}`);
        if (code === 0) {
            res.send('Form submitted successfully!');
        } else {
            res.status(500).json({ error: 'Internal server error' });
        }
    });
});

// Endpoint for the home page
app.get('/home', (req, res) => {
    res.send('Welcome to the home page');
});

// Start the server
app.listen(port, async () => {
    // Sync Sequelize models with the database
    await sequelize.sync();
    console.log(`Server is running on http://localhost:${port}`);
});
