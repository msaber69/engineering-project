import { useEffect, useState } from "react";
import axios from 'axios'; // Import Axios
import '../styles/Results.css';

interface TestData {
  [key: string]: {
    [key: string]: number | string;
  };
}

export const Results1 = () => {
  const [data, setData] = useState<TestData | null>(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('http://localhost:3001/api/test1_results'); // Use Axios to fetch data
        setData(response.data);
      } catch (error) {
        console.error('Error fetching JSON:', error);
      }
    };

    fetchData(); // Call the fetch function when the component mounts
  }, []); // Empty dependency array ensures this effect runs only once on mount

  return (
    <div className="centered-container">
      <h2>Test Results</h2>
      {!data ? (
        <p>Loading...</p>
      ) : (
        <div className="result-data">
          {Object.entries(data).map(([category, values]) => (
            <div key={category} className="category">
              <h3>{category}</h3>
              <ul>
                {Object.entries(values).map(([key, value]) => (
                  <li key={key}>
                    <strong>{key}:</strong> {value}
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default Results1;
