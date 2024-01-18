// components/Login.tsx
import React, { useState } from 'react';
import '../styles/Login.css';

const Login: React.FC = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [fullName, setFullName] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [isSignIn, setIsSignIn] = useState(true);

  const handleLogin = () => {
    // Add your login logic here
    console.log(`Logging in with email: ${email} and password: ${password}`);
  };

  const handleSignUp = () => {
    // Add your sign-up logic here
    console.log(`Signing up with email: ${email}, password: ${password}, full name: ${fullName}`);
  };

  const toggleForm = () => {
    setIsSignIn((prev) => !prev);
  };

  return (
      <div className="login-container">
        <h2>{isSignIn ? 'Login to Your Account' : 'Sign Up for an Account'}</h2>
        <form className="login-form">
          <div className="form-group">
            <label htmlFor="email">Email:</label>
            <input
              type="email"
              id="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
            />
          </div>
          <div className="form-group">
            <label htmlFor="password">Password:</label>
            <input
              type="password"
              id="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />
          </div>
          {!isSignIn && (
            <>
              {/* Additional fields for the sign-up form */}
              <div className="form-group">
                <label htmlFor="fullName">Full Name:</label>
                <input
                  type="text"
                  id="fullName"
                  value={fullName}
                  onChange={(e) => setFullName(e.target.value)}
                />
              </div>
              <div className="form-group">
                <label htmlFor="confirmPassword">Confirm Password:</label>
                <input
                  type="password"
                  id="confirmPassword"
                  value={confirmPassword}
                  onChange={(e) => setConfirmPassword(e.target.value)}
                />
              </div>
            </>
          )}
          <button type="button" onClick={isSignIn ? handleLogin : handleSignUp}>
            {isSignIn ? 'Login' : 'Sign Up'}
          </button>
        </form>
        <p>
          {isSignIn ? "Don't have an account?" : 'Already have an account?'}{' '}
          <button type="button" onClick={toggleForm}>
            {isSignIn ? 'Sign up here' : 'Login here'}
          </button>
        </p>
      </div>
  );
};

export default Login;
