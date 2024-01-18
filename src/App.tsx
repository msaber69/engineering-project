// App.tsx (React Router v6)
import React from 'react';
import { BrowserRouter as Router } from 'react-router-dom';
import Layout from './components/Layout';
import Pages from './routes/pagesRoutes';

const App: React.FC = () => {
  return (
    <Router>
      <Layout>
        <Pages />
      </Layout>
    </Router>
  );
};

export default App;
