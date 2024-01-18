import React from 'react';
import '../styles/UserForm.css';


const UserForm: React.FC = () => {
    return (
            <div className="user-form">
                <h1>User Input Form</h1>
                <form action="#" method="post">
                    <label htmlFor="name">Name:</label>
                    <input type="text" id="name" name="name" required />
                    <br />
                    <label htmlFor="age">Age:</label>
                    <input type="number" id="age" name="age" required />
                    <br />
                    {/* Add more form fields as needed */}
                    <br />
                    <button type="submit">Submit</button>
                </form>
            </div>
    );
};

export default UserForm;
