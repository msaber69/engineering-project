const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const { sequelize } = require('./config/dbConfig');
const User = require('./models/UserModel');
const { spawn } = require('child_process');
const fs = require('fs');
const path = require('path');


const app = express();
const port = 3001;

app.use(cors());
app.use(bodyParser.json());

const bcrypt = require('bcrypt'); // Import bcrypt

app.post('/login', async (req, res) => {
    const { email, password } = req.body;

    try {
        // Query the database to find the user by email
        const user = await User.findOne({ where: { email } });

        if (!user) {
            // User not found or email does not exist
            return res.status(401).json({ error: 'Invalid email or password' });
        }

        // Compare the provided password with the hashed password stored in the database
        const passwordMatch = await bcrypt.compare(password, user.password);

        if (!passwordMatch) {
            // Passwords don't match
            return res.status(401).json({ error: 'Invalid email or password' });
        }

        // Passwords match, user is authenticated
        res.redirect('/home');
    } catch (error) {
        console.error('Error:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
});


// Endpoint to handle user signup
app.post('/signup', async (req, res) => {
  // Extract signup data from the request body
  const { first_name, last_name, email, password, confirmPassword } = req.body;

  try {
      // Check if all required fields are provided
      if (!first_name || !last_name || !email || !password || !confirmPassword) {
          return res.status(400).json({ error: 'All fields are required' });
      }

      // Check if passwords match
      if (password !== confirmPassword) {
          return res.status(400).json({ error: 'Passwords do not match' });
      }

      // Check if the user already exists
      const existingUser = await User.findOne({ where: { email } });
      if (existingUser) {
          return res.status(400).json({ error: 'User already exists with this email' });
      }

      // Hash the password
      // You'll need to use a library like bcrypt to securely hash passwords
      // Here's an example using bcrypt
      const bcrypt = require('bcrypt');
      const saltRounds = 10;
      const hashedPassword = await bcrypt.hash(password, saltRounds);

      // Create the user in the database
      await User.create({
          first_name,
          last_name,
          email,
          password: hashedPassword
      });

      // Return success response
      res.status(201).json({ message: 'User created successfully' });
  } catch (error) {
      console.error('Error:', error);
      res.status(500).json({ error: 'Internal server error' });
  }
});



// Define the paths to the CSV files
const csvFilePaths = {
  test1: path.join(__dirname, '/dataset_server/test1_responses.csv'),
  test2: path.join(__dirname, '/dataset_server/test2_responses.csv'),
  test3: path.join(__dirname, '/dataset_server/test3_responses.csv'),
};

// Function to write data to CSV file
const writeToCSV = (filePath, data) => {
  // Prepare the CSV row
  const csvRow = Object.values(data).join(',') + '\n';

  // Truncate the file before appending new data
  fs.truncate(filePath, 0, (err) => {
    if (err) {
      console.error('Error truncating CSV file:', err);
    } else {
      console.log('CSV file truncated successfully');
      
      // Write the row to the CSV file
      fs.appendFile(filePath, csvRow, (err) => {
        if (err) {
          console.error('Error writing to CSV file:', err);
        } else {
          console.log('Response written to CSV file');
        }
      });
    }
  });
};

// Endpoint to handle test 1 submission
app.post('/submitTest1', (req, res) => {
  // Retrieve submitted data from the request body
  const formData = req.body;

  // Write the form data to the test1 CSV file
  writeToCSV(csvFilePaths.test1, formData);

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
          res.send('Form submitted and parsed successfully!');
      } else {
          res.status(500).json({ error: 'Internal server error' });
      }
  });
});

// Endpoint to handle test 2 submission
app.post('/submitTest2', (req, res) => {
  // Retrieve submitted data from the request body
  const formData = req.body;

  // Write the form data to the test2 CSV file
  writeToCSV(csvFilePaths.test2, formData);

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
          res.send('Test 2 form submitted and parsed successfully!');
      } else {
          res.status(500).json({ error: 'Internal server error' });
      }
  });
});

// Endpoint to handle test 3 submission
app.post('/submitTest3', (req, res) => {
  // Retrieve submitted data from the request body
  const formData = req.body;

  // Write the form data to the test3 CSV file
  writeToCSV(csvFilePaths.test3, formData);

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
          res.send('Test 3 form submitted and parsed successfully!');
      } else {
          res.status(500).json({ error: 'Internal server error' });
      }
  });
});

// Define a route to serve test1_results.json
app.get('/api/test1_results', (req, res) => {
  // Path to the JSON file
  const filePath = path.join(__dirname, 'dataset_server', 'test1_results.json');

  // Read the JSON file
  fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
      console.error('Error reading file:', err); // Log the error
      res.status(500).json({ error: 'Internal server error' });
      return;
    }

    // Parse the JSON data and send it in the response
    const jsonData = JSON.parse(data);
    res.json(jsonData);
  });
});

app.get('/api/test2_results', (req, res) => {
  // Path to the JSON file
  const filePath = path.join(__dirname, 'dataset_server', 'test2_results.json');

  // Read the JSON file
  fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
      console.error('Error reading file:', err); // Log the error
      res.status(500).json({ error: 'Internal server error' });
      return;
    }

    // Parse the JSON data and send it in the response
    const jsonData = JSON.parse(data);
    res.json(jsonData);
  });
});

app.get('/api/test3_results', (req, res) => {
  // Path to the JSON file
  const filePath = path.join(__dirname, 'dataset_server', 'test3_results.json');

  // Read the JSON file
  fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
      console.error('Error reading file:', err); // Log the error
      res.status(500).json({ error: 'Internal server error' });
      return;
    }

    // Parse the JSON data and send it in the response
    const jsonData = JSON.parse(data);
    res.json(jsonData);
  });
});



/*// Endpoint to handle test submission
app.post('/parseResults', (req, res) => {
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
});*/

// Catch-all route for non-existing endpoints
app.use((req, res) => {
  res.status(404).json({ error: 'Resource not found' });
});

// Start the server
app.listen(port, async () => {
  // Sync Sequelize models with the database
  await sequelize.sync();
  console.log(`Server is running on http://localhost:${port}`);
});