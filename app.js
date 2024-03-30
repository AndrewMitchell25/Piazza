const express = require('express')
const app = express()

const mongoose =require('mongoose')
require('dotenv/config')

const bodyParser = require('body-parser')
app.use(bodyParser.json())

const postRoute = require('./routes/post')
app.use('/post',postRoute)

mongoose.connect(process.env.DB_CONNECTOR)

app.get('/', async(req,res) =>{
    res.send("Main Page: try /post")
})

app.listen(3000, ()=>{
    console.log('Server is up and running...')
})