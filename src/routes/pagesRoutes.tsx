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
import Results1 from '../components/Results1';
import Results2 from '../components/Results2';
import Results3 from '../components/Results3';
import Infos from '../components/Infos';
import Signup from '../components/Signup';



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
      <Route path="/results1" element={<Results1 />} />      
      <Route path="/results2" element={<Results2 />} />
      <Route path="/results3" element={<Results3 />} />
      <Route path="/infos/:testNumber" element={<Infos />} />
      <Route path="/signup" element={<Signup />} />
    </Routes>
  );
};

export default Pages;
