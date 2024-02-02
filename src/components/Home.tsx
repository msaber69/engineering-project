// components/Home.tsx

import React from 'react';
import { Link } from 'react-router-dom';
import '../styles/Home.css';

const Home: React.FC = () => {
    return (
            <div className="home">
                <section className="hero">
                    <div className="overlay"></div>
                    <div className="hero-content">
                        <h1>Discover Your Mental Health Profile</h1>
                        <p>Embark on a journey of self-discovery with our quick and insightful mental health questionnaire. 
                            Start now to gain personalized insights and take a proactive step towards your well-being.</p>
                        <Link to="/login">Start now</Link>
                    </div>
                </section>

                <section className="navigation">
                    <div><p>hellooo</p></div>
                    {/* Navigation links for About Us, Services, Contact, Products, Articles, and Languages */}
                    {/* Add your logo here */}
                </section>

                {/* Add content sections for About Us, Services, Contact, Products, Articles */}
            </div>
    );
};

export default Home;
