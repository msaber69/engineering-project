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
import resultsTest1 from '../components/Results1';
import resultsTest2 from '../components/Results2';
import resultsTest3 from '../components/Results3';


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
      <Route path="/resultsTest1" element={<resultsTest1 />} />      
      <Route path="/resultsTest2" element={<resultsTest2 />} />
      <Route path="/resultsTest3" element={<resultsTest3 />} />
      {/* Add more routes for other pages as needed */}
    </Routes>
  );
};

export default Pages;
