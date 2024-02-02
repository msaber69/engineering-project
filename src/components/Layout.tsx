// components/Layout.tsx
import React, { ReactNode } from 'react';
import { Link } from 'react-router-dom';
import '../styles/Layout.css';
import logo from '../img/image-removebg-preview_1.png';

interface LayoutProps {
  children: ReactNode;
}

const Layout: React.FC<LayoutProps> = ({ children }) => {
  return (
    <div className="layout">
      <header>
        <img src={logo} alt="Your Logo" className="logo" />
        <nav>
          <Link to="/">Home</Link>
          <Link to="/login">Sign In / Sign Up</Link>
          <Link to="/contact">Contact Us</Link>
          <Link to="/help">Help</Link>
          {/* Add more navigation links as needed */}
        </nav>
      </header>
      <main>{children}</main>
      <footer>
        <p>&copy; 2024 ML Project</p>
      </footer>
    </div>
  );
};

export default Layout;
