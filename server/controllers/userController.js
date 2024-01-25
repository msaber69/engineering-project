const User = require('../models/UserModel');

async function login(req, res) {
    const { email, password } = req.body;

    try {
        const user = await User.findOne({ where: { email, password } });

        if (user) {
            res.redirect('/home');
        } else {
            res.status(401).json({ error: 'Invalid email or password' });
        }
    } catch (error) {
        console.error('Error:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
}

module.exports = { login };
