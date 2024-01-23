// Test1.tsx
import React, { useState } from 'react';
import questions from '../questions';
import '../styles/Survey.css';

const Test1: React.FC = () => {
  const [answers, setAnswers] = useState<{ [key: string]: string }>({});

  const handleOptionChange = (questionId: string, value: string) => {
    setAnswers((prevAnswers) => ({ ...prevAnswers, [questionId]: value }));
  };

  interface Answers {
    [questionId: string]: string; 
  };

  const handleSubmit = async (answers: Answers) => {
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
                testType: 'test1',
                responses: responseArray,
            }),
        });

        if (response.ok) {
            console.log('User responses submitted successfully');
            const result = await response.json();
            console.log('Scoring Result:', result);

            // Interpret the result and update your UI as needed
            // For example, you can display the scores in the UI
            alert(`ADHD Score: ${result.result[0].Final_ADHD_score}`);
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
                  value={option}
                  checked={answers[question.id] === option}
                  onChange={() => handleOptionChange(question.id, option)}
                />
                <label htmlFor={`${question.id}-${index}`}>{option}</label>
              </div>
            ))}
          </div>
        ))}
      <button onClick={() => handleSubmit(answers)}>Submit Test 1</button>
    </div>
  );
};

export default Test1;
