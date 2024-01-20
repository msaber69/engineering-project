// Pages.tsx 
import React from 'react';
import { Route, Routes } from 'react-router-dom';
import Home from '../components/Home';
import Login from '../components/Login';
import Contact from '../components/Contact';
import Survey from '../components/Survey';
import Test1 from '../components/Test1';
import Test2 from '../components/Test2';
import Test3 from '../components/Test3';


const Pages: React.FC = () => {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/login" element={<Login />} />
      <Route path="/contact" element={<Contact />} />      
      <Route path="/login" element={<Login />} />
      <Route path="/survey" element={<Survey />} />
      <Route path="/test1" element={<Test1 />} />      
      <Route path="/test2" element={<Test2 />} />
      <Route path="/test3" element={<Test3 />} />
      {/* Add more routes for other pages as needed */}
    </Routes>
  );
};

export default Pages;
