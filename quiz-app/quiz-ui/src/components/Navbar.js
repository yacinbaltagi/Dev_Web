// src/components/Navbar.js
import React from 'react';
import './Navbar.css';

const Navbar = () => {
  return (
    <nav className="navbar">
      <div className="navbar-logo">
        <a href="/">Quiz Télétravail</a>
      </div>
      <div className="navbar-links">
        <a href="/">Home</a>
        <a href="/login">Login</a>
      </div>
    </nav>
  );
}

export default Navbar;
