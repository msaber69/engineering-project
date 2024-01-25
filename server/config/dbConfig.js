const { Sequelize } = require('sequelize');

const sequelize = new Sequelize({
  database: 'engineering_project_database',
  username: 'root',
  password: 'password',
  host: 'localhost',
  dialect: 'mysql',
});


module.exports = { sequelize };
