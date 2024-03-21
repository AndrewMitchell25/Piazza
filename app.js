const express = require('express')
const app = express()

const mongoose =require('mongoose')
require('dotenv/config')

const bodyParser = require('body-parser')

const Post = require('./models/Post')

app.use(bodyParser.json())

// POST (Create data)
app.post('/',async(req,res)=>{
    //console.log(req.body)

    const postData = new Post({
        title:req.body.title,
    })

    try{
        const postToSave = await postData.save()
        res.send(postToSave)
    }catch(err){
        res.send({message:err})
    }
})

// GET 1 (Read all)
app.get('/', async(req,res) =>{
    try{
        const getPosts = await Post.find().limit(10)
        res.send(getPosts)
    }catch(err){
        res.send({message:err})
    }
})

// GET 2 (Read by ID)
app.get('/:postId', async(req,res) =>{
    try{
        const getPostById = await Post.findById(req.params.postId)
        res.send(getPostById)
    }catch(err){
        res.send({message:err})
    }
})

//TODO: DELETE ALL

// DELETE (Delete)
app.delete('/:postId',async(req,res)=>{
    try{
        const deletePostById = await Post.deleteOne({_id:req.params.postId})
        res.send(deletePostById)
    }catch(err){
        res.send({message:err})
    }
})

// PATCH (Update)
app.patch('/:postId', async(req,res) =>{
    try{
        const updatePostById = await Post.updateOne(
            {_id:req.params.postId},
            {$set:{
                user:req.body.user,
                title:req.body.title,
                text:req.body.text,
                hashtag:req.body.hashtag,
                location:req.body.location,
                url:req.body.url
                }
            })
        res.send(updatePostById)
    }catch(err){
        res.send({message:err})
    }
})

mongoose.connect(process.env.DB_CONNECTOR)

app.listen(3000, ()=>{
    console.log('Server is up and running...')
})