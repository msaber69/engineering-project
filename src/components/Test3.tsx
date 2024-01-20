// Test3.tsx
import React, { useState } from 'react';
import questions from '../questions';
import '../styles/Survey.css'; // Update the path based on your project structure

const Test3: React.FC = () => {
  const [answers, setAnswers] = useState<{ [key: string]: string }>({});

  const handleAnswerChange = (questionId: string, value: string) => {
    setAnswers((prevAnswers) => ({ ...prevAnswers, [questionId]: value }));
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
      <button onClick={() => console.log(answers)}>Submit Test 1</button>
    </div>
  );
};

export default Test3;
