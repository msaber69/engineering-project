import React, { useState } from 'react';
import questions from '../questions';
import '../styles/Survey.css'; // Update the path based on your project structure

interface Answers {
  [key: string]: string;
}

const Test3: React.FC = () => {
  const [answers, setAnswers] = useState<Answers>({});

  const handleAnswerChange = (questionId: string, value: string) => {
    setAnswers((prevAnswers) => ({ ...prevAnswers, [questionId]: value }));
  };

  const handleSubmit = async () => {
    try {
      const response = await fetch('http://localhost:3001/submitTest', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(answers),
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
        .filter((question) => question.section === 'Test3')
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
      <button onClick={handleSubmit}>Submit Test 3</button>
    </div>
  );
};

export default Test3;
