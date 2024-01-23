// Survey.tsx

import React from 'react';
import { useNavigate } from 'react-router-dom';
import '../styles/Survey.css';


const Survey: React.FC = () => {
  const navigate = useNavigate();
  
  const redirectToTest = (test: string) => {
    navigate(`/${test.toLowerCase()}`);
  };

  const renderTestInfo = (section: string, description: string, estimatedTime: string) => (
    <div key={section} className="test-info">
      <div className="test-description">
        <p>{description}</p>
      </div>
      <div className="test-buttons">
        <span>{`Estimated Time: ${estimatedTime}`}</span>
        <button className="test-start" onClick={() => redirectToTest(section)}>Start</button>
      </div>
    </div>
  );

  const renderSectionButton = (section: string) => {
    let description = '';
    let estimatedTime = '';

    // Add descriptions and estimated times for each test
    if (section === 'Test1') {
      description = 'Mental Health Assessment';
      estimatedTime = '10-15 minutes';
    } else if (section === 'Test2') {
      description = 'ADHD/ADD Assessment';
      estimatedTime = '15-20 minutes';
    } else if (section === 'Test3') {
      description = 'Depression Assessment';
      estimatedTime = '12-18 minutes';
    }

    return renderTestInfo(section, description, estimatedTime);
  };

  const renderIntroText = () => (
    <div className="intro-text">
      <h1>Hello Saber!</h1>
      <p>
        Welcome to our mental health assessment. Please select a section below to begin the
        corresponding test. Your honest responses will help us provide personalized insights.
      </p>
    </div>
  );

  return (
    <div className="survey-container">
      {renderIntroText()}

      <div className="section-buttons">
        {['Test1', 'Test2', 'Test3'].map((section) => renderSectionButton(section))}
      </div>

      <button className="survey-submit" /*onClick={() => console.log(answers)}*/>Submit</button>
    </div>
  );
};

export default Survey;
