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

const uri = process.env.ATLAS_URI;
mongoose.connect(uri, {useUnifiedTopology: true, useNewUrlParser: true, useCreateIndex: true })
    .then(() => console.log("It works now"))
    .catch((err) => console.log("no it does not work", err));
const connection = mongoose.connection;
connection.once('open', () => {
    console.log("MongoDB database connection success")
})

const userRouter = require('./routes/users')
app.use('/user', userRouter)

server.listen(port, () => {
  console.log('Server running on port ', port)
})