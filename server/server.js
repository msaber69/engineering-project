const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const { sequelize } = require('./config/dbConfig');
const User = require('./models/UserModel');

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
app.post('/submitTest', async (req, res) => {
    const { testType, responses } = req.body;

    try {
        let result;

        // Perform operations based on the testType
        switch (testType) {
            case 'asrs_old':
                // Perform scoring logic for ASRS old test
                break;
            case 'asrs_new':
                // Perform scoring logic for ASRS new test
                break;
            case 'dsm5':
                // Perform scoring logic for DSM5 test
                break;
            case 'qids_sr16':
                // Perform scoring logic for QIDS-SR16 test
                break;
            case 'test1':
                // Mock response for testing purposes
                result = { test1Score: 42 };
                break;
            default:
                result = { error: 'Invalid test type' };
        }

        // Send the result back to the client
        res.json({ result });
    } catch (error) {
        console.error('Error:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
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
