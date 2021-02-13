const express = require('express') //express framework
const cors = require('cors') //enable cors
const mongoose = require('mongoose') //mongodb
require('dotenv').config({path: __dirname + '/.env'}); //dotenv config
const app = express() //init app function

const server = require('http').createServer(app) //supply to http server

const port = process.env.PORT || 5000;

app.set('view engine', 'ejs')
app.use(express.static('public'))
app.use(cors())
app.use(express.json())

const uri = "mongodb+srv://aman:7dT8bZGnaAPmL6rS@cluster0.mjlo9.mongodb.net/treehacks?retryWrites=true&w=majority";
mongoose.connect(uri, {useUnifiedTopology: true, useNewUrlParser: true, useCreateIndex: true });
const connection = mongoose.connection;
connection.once('open', () => {
    console.log("MongoDB database connection success")
})

server.listen(port, () => {
  console.log('Server running on port ', port)
})