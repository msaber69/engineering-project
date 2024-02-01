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

// Import necessary modules
const fs = require('fs');
const path = require('path');

// Define the paths to the CSV files
const csvFilePaths = {
  test1: path.join(__dirname, 'test1_responses.csv'),
  test2: path.join(__dirname, 'test2_responses.csv'),
  test3: path.join(__dirname, 'test3_responses.csv'),
};

// Function to write data to CSV file
const writeToCSV = (filePath, data) => {
  // Prepare the CSV row
  const csvRow = Object.values(data).join(',') + '\n';

  // Write the row to the CSV file
  fs.appendFile(filePath, csvRow, (err) => {
    if (err) {
      console.error('Error writing to CSV file:', err);
    } else {
      console.log('Response written to CSV file');
    }
  });
};

// Endpoint to handle test 1 submission
/*app.post('/submitTest1', (req, res) => {
  // Retrieve submitted data from the request body
  const formData = req.body;
  

  // Write the form data to the test1 CSV file
  writeToCSV(csvFilePaths.test1, formData);

  // Send response
  res.send('Test 1 form submitted successfully!');
});*/

// Endpoint to handle test 2 submission
app.post('/submitTest2', (req, res) => {
  // Retrieve submitted data from the request body
  const formData = req.body;

  // Write the form data to the test2 CSV file
  writeToCSV(csvFilePaths.test2, formData);

  // Send response
  res.send('Test 2 form submitted successfully!');
});

// Endpoint to handle test 3 submission
app.post('/submitTest3', (req, res) => {
  // Retrieve submitted data from the request body
  const formData = req.body;

  // Write the form data to the test3 CSV file
  writeToCSV(csvFilePaths.test3, formData);

  // Send response
  res.send('Test 3 form submitted successfully!');
});


// Endpoint to handle test submission
app.post('/submitTest1', (req, res) => {
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
