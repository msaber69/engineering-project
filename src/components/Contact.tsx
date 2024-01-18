// components/ContactUs.tsx
import React, { useState } from 'react';
import '../styles/Contact.css';

const ContactUs: React.FC = () => {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [message, setMessage] = useState('');

  const handleContactSubmit = () => {
    // Add your contact form submission logic here
    console.log(`Contact Form Submitted: Name - ${name}, Email - ${email}, Message - ${message}`);
    // Optionally, you can send the form data to a server for processing.
  };

  return (
      <div className="contact-container">
        <h2>Contact Us</h2>
        <form className="contact-form" onSubmit={handleContactSubmit}>
          <div className="form-group">
            <label htmlFor="name">Name:</label>
            <input
              type="text"
              id="name"
              value={name}
              onChange={(e) => setName(e.target.value)}
              required
            />
          </div>
          <div className="form-group">
            <label htmlFor="email">Email:</label>
            <input
              type="email"
              id="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
            />
          </div>
          <div className="form-group">
            <label htmlFor="message">Message:</label>
            <textarea
              id="message"
              value={message}
              onChange={(e) => setMessage(e.target.value)}
              required
            ></textarea>
          </div>
          <button type="submit">Submit</button>
        </form>
        <div className="emergency-hotline">
          <h3>Emergency Hotline</h3>
          <p>For immediate assistance, call our 24/7 emergency hotline:</p>
          <p className="hotline-number">123-456-7890</p>
        </div>
      </div>
  );
};

export default ContactUs;
