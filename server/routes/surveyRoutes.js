const express = require('express');
const router = express.Router();
const mlModel = require('../model/mlModel');
const questions = require('../../src/questions');

router.post('/submit', async (req, res) => {
  try {
    const answers = req.body.answers;
    // Call your machine learning model with answers
    const results = await mlModel.predict(answers);
    res.json({ results });
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

router.get('/questions', (req, res) => {
  res.json({ questions });
});

module.exports = router;
