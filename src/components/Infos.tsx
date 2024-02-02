import React from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import '../styles/Infos.css';

const Infos = () => {
  const { testNumber } = useParams();
  const navigate = useNavigate();

  const handleAgree = () => {
    // Redirect to the corresponding test page based on the testNumber parameter
    navigate(`/test${testNumber}`);
  };

  const handleDisagree = () => {
    // Redirect to survey page
    navigate(`/survey`);
  };

  return (
    <div className="centered-container">
      <h2>ADULT ADHD TEST</h2>
      <p className='infos-grid'>
         By clicking "I Agree" below you acknowledge that this is not a diagnostic instrument and is only to 
         be used by you if you are 18 years or older. You agree that this application is for information purposes 
         only and is not intended to replace a consultation with your doctor or a mental health professional. 
         Mind Diagnostics, sponsors, partners, and advertisers disclaim any liability, loss, or risk incurred 
         as a consequence, directly or indirectly, from the use and application of this test. If you are in need 
         of immediate assistance, please dial 15 or the National Suicide Prevention Lifeline at (+33) (0)1 40 09 15 22
      </p>
      <div className="button-container">
        <button onClick={handleDisagree}>I Disagree</button>
        <button onClick={handleAgree}>I Agree</button>
      </div>
    </div>
  );
};

export default Infos;
