import React, { useState } from 'react';
import questions from '../questions';
import '../styles/Survey.css';

const Test2: React.FC = () => {
  const [answers, setAnswers] = useState<{ [key: string]: string }>({});

  const handleOptionChange = (questionId: string, value: string) => {
    setAnswers((prevAnswers) => ({ ...prevAnswers, [questionId]: value }));
  };

  const handleSubmit = async () => {
    // Check if all questions have been answered
    const answeredQuestions = Object.keys(answers);
    const allQuestions = questions.filter((question) => question.section === 'Test2');
    if (answeredQuestions.length !== allQuestions.length) {
      alert('Please answer all questions before submitting.');
      return;
    }
  
    // Check if all questions have a selected option
    const unansweredQuestions = allQuestions.filter((question) => !answers[question.id]);
    if (unansweredQuestions.length > 0) {
      alert('Please select an option for all questions before submitting.');
      return;
    }
  
    try {
      const response = await fetch('http://localhost:3001/submitTest2', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(answers),
      });
  
      if (response.ok) {
        console.log('User responses submitted successfully');
        // Redirect to the survey page
        window.location.href = '/results2';
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
          <div key={question.id} className="question-container">
            <div className="question">
              <p>{question.text}</p>
            </div>
            <div className="options">
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
            ))}</div>
          </div>
        ))}
      <button onClick={handleSubmit}>Submit Test 2</button>
    </div>
  );
};

export default Test2;
