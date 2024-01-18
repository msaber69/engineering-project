// components/Home.tsx

import React from 'react';
import { Link } from 'react-router-dom';
import Layout from './Layout';
import '../styles/Home.css';

const Home: React.FC = () => {
    return (
        <Layout>
            <div className="home">
                <section className="hero">
                    <div className="overlay"></div>
                    <div className="hero-content">
                        <h1>Welcome to the ML Project</h1>
                        <p>Advancing healthcare through machine learning technology.</p>
                        <Link to="/userform">Get Started</Link>
                    </div>
                </section>

                <section className="navigation">
                    {/* Navigation links for About Us, Services, Contact, Products, Articles, and Languages */}
                    {/* Add your logo here */}
                </section>

                {/* Add content sections for About Us, Services, Contact, Products, Articles */}
            </div>
        </Layout>
    );
};

export default Home;
