// Pages.tsx 
import React from 'react';
import { Route, Routes } from 'react-router-dom';
import Home from '../components/Home';
import Login from '../components/Login';
import Contact from '../components/Contact';

const Pages: React.FC = () => {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/login" element={<Login />} />
      <Route path="/contact" element={<Contact />} />      
      <Route path="/login" element={<Login />} />
      {/* Add more routes for other pages as needed */}
    </Routes>
  );
};

export default Pages;
