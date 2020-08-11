if(process.env.NODE_ENV !== 'production'){
 require('dotenv').config()
}

const express = require("express");
const app = express();
const path = require("path");
const bodyParser = require("body-parser");
const cors = require("cors")
// function for turning the db.
const connectDB = require("./config/db");

// PORT
const PORT = 8080 || process.env.PORT;

// Connection to the database....
connectDB();


// Middlewares
app.use(bodyParser.urlencoded({extended:false}));
app.use(bodyParser.json())
app.use(cors())

// setting local variable for password
app.use((req, res, next) => { 
 res.locals.password = "kitten"
 next()
})

// ----------Router Middlewares-----------------
app.use('/api/user', require('./src/routes/user.route'));


// listen to a port........
app.listen(PORT, () => {
 console.log(`listening to the port ${PORT}`);
});