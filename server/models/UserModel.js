const { DataTypes } = require('sequelize');
const { sequelize } = require('../config/dbConfig');

const User = sequelize.define('user', {
    first_name: {
        type: DataTypes.STRING,
        allowNull: false
    },
    last_name: {
        type: DataTypes.STRING,
        allowNull: false
    },
    email: {
        type: DataTypes.STRING,
        allowNull: false,
        unique: true
    },
    password: {
        type: DataTypes.STRING,
        allowNull: false
    },
    MHA_score: {
        type: DataTypes.INTEGER,
        allowNull: true
    },
    ADHD_score: {
        type: DataTypes.INTEGER,
        allowNull: true
    },
    Dep_score: {
        type: DataTypes.INTEGER,
        allowNull: true
    }
}, {
    tableName: 'user',
    timestamps: false 
  });

module.exports = User;
