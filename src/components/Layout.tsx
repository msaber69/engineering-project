// components/Layout.tsx

import React, { ReactNode } from 'react';
import { Link } from 'react-router-dom';
import '../styles/Layout.css';

interface LayoutProps {
  children: ReactNode;
}

const Layout: React.FC<LayoutProps> = ({ children }) => {
  return (
    <div className="layout">
      <header>
        <div className="logo">Your Logo</div>
        <nav>
          <Link to="/">Home</Link>
          <Link to="/about">About Us</Link>
          <Link to="/services">Services</Link>
          <Link to="/products">Products</Link>
          <Link to="/services">Articles</Link>
          <Link to="/products">Contact</Link>
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
