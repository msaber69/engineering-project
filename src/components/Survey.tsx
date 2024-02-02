import React from 'react';
import { useNavigate } from 'react-router-dom';
import '../styles/Survey.css';

const Survey: React.FC = () => {
  const navigate = useNavigate();
  
  const redirectToInfos = (testNumber: number) => {
    navigate(`/infos/${testNumber}`);
  };

  const renderTestInfo = (testNumber: number, description: string, estimatedTime: string) => (
    <div key={testNumber} className="test-info">
      <div className="test-description">
        <p>{description}</p>
      </div>
      <div className="test-buttons">
        <span>{`Estimated Time: ${estimatedTime}`}</span>
        <button className="test-start" onClick={() => redirectToInfos(testNumber)}>Start</button>
      </div>
    </div>
  );

  const renderSectionButton = (testNumber: number) => {
    let description = '';
    let estimatedTime = '';

    // Add descriptions and estimated times for each test
    if (testNumber === 1) {
      description = 'Mental Health Assessment';
      estimatedTime = '10-15 minutes';
    } else if (testNumber === 2) {
      description = 'ADHD/ADD Assessment';
      estimatedTime = '15-20 minutes';
    } else if (testNumber === 3) {
      description = 'Depression Assessment';
      estimatedTime = '12-18 minutes';
    }

    return renderTestInfo(testNumber, description, estimatedTime);
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
        {[1, 2, 3].map((testNumber) => renderSectionButton(testNumber))}
      </div>

      <button className="survey-submit">Submit</button> {/* No action needed for submit button */}
    </div>
  );
};

export default Survey;
