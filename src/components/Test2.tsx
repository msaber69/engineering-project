// Test2.tsx
import React, { useState } from 'react';
import questions from '../questions';
import '../styles/Survey.css'; // Update the path based on your project structure

interface Answers {
  [key: string]: string;
}

const Test2: React.FC = () => {
  const [answers, setAnswers] = useState<Answers>({});

  const handleAnswerChange = (questionId: string, value: string) => {
    setAnswers((prevAnswers) => ({ ...prevAnswers, [questionId]: value }));
  };

  const handleSubmit = () => {
    // Assuming you have a function to handle the submission
    submitTest(answers);
  };

  const submitTest = async (answers: Answers) => {
    try {
      // Extract question IDs and selected option IDs
      const responseArray = Object.entries(answers).map(([questionId, selectedOption]) => ({
        questionId,
        selectedOption,
      }));

      const response = await fetch('http://localhost:3001/submitTest', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          testType: 'test2', // Assuming 'test2' is the correct test type
          responses: responseArray,
        }),
      });

      if (response.ok) {
        console.log('User responses submitted successfully');
        const result = await response.json();
        console.log('Scoring Result:', result);
      } else {
        console.error('Failed to submit user responses');
      }
    } catch (error) {
      console.error('Error submitting user responses:', error);
    }
  };

  return (
    <div className="test-container">
      {questions
        .filter((question) => question.section === 'Test2')
        .map((question) => (
          <div key={question.id} className="question">
            <p>{question.text}</p>
            {question.options?.map((option, index) => (
              <div key={index} className="radio-option">
                <input
                  type="radio"
                  id={`${question.id}-${index}`}
                  name={question.id}
                  value={option}
                  checked={answers[question.id] === option}
                  onChange={() => handleAnswerChange(question.id, option)}
                />
                <label htmlFor={`${question.id}-${index}`}>{option}</label>
              </div>
            ))}
          </div>
        ))}
      <button onClick={handleSubmit}>Submit Test 2</button>
    </div>
  );
};

export default Test2;
