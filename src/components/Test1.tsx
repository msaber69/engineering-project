import React, { useState } from 'react';
import questions from '../questions';
import '../styles/Survey.css';

const Test1: React.FC = () => {
  const [answers, setAnswers] = useState<{ [key: string]: string }>({});

  const handleOptionChange = (questionId: string, value: string) => {
    setAnswers((prevAnswers) => ({ ...prevAnswers, [questionId]: value }));
  };

  const handleSubmit = async () => {
    try {
      const response = await fetch('http://localhost:3001/submitTest1', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(answers),
      });

      if (response.ok) {
        console.log('User responses submitted successfully');
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
        .filter((question) => question.section === 'Test1')
        .map((question) => (
          <div key={question.id} className="question">
            <p>{question.text}</p>
            {question.options?.map((option, index) => (
              <div key={index} className="radio-option">
                <input
                  type="radio"
                  id={`${question.id}-${index}`}
                  name={question.id}
                  value={index + 1} // Assign values as 1, 2, 3, 4 instead of option text
                  checked={answers[question.id] === String(index + 1)}
                  onChange={() => handleOptionChange(question.id, String(index + 1))}
                />
                <label htmlFor={`${question.id}-${index}`}>{option}</label>
              </div>
            ))}
          </div>
        ))}
      <button onClick={handleSubmit}>Submit Test 1</button>
    </div>
  );
};

export default Test1;
