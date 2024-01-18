const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');

const app = express();
const port = process.env.PORT || 5000;

// Middleware
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(cors());

// Define your routes here

app.get('/', (req, res) => {
  res.send('Welcome to the Mental Health Diagnosis Tool API');
});

// Example route for handling questionnaire data
app.post('/api/questionnaire', (req, res) => {
  // Process the questionnaire data
  const questionnaireData = req.body;

  // Perform any necessary computations or use machine learning models here

  // Return a response
  res.json({ result: 'Diagnosis suggestion goes here' });
});

// Handle other routes or middleware as needed

// Start the server
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
