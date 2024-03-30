const express = require('express')
const router = express.Router()

const Post = require('../models/Post')

// POST (Create data)
router.post('/',async(req,res)=>{
    //console.log(req.body)

    const postData = new Post({
        title:req.body.title,
        topic:req.body.topic,
        message:req.body.message
    })

    try{
        const postToSave = await postData.save()
        res.send(postToSave)
    }catch(err){
        res.send({message:err})
    }
})

// GET 1 (Read all)
router.get('/', async(req,res) =>{
    try{
        const getPosts = await Post.find().limit(10)
        res.send(getPosts)
    }catch(err){
        res.send({message:err})
    }
})

// GET 2 (Read by ID)
router.get('/:postId', async(req,res) =>{
    try{
        const getPostById = await Post.findById(req.params.postId);
        res.send(getPostById)
    }catch(err){
        res.send({message:err})
    }
})

//DELETE ALL
router.delete('/', async (req,res) => {
    try {
        const deleteAll = await Post.deleteMany({});
        res.send(deleteAll);
    } catch (err) {
        res.send({message:err})
    }
})

// DELETE (Delete)
router.delete('/:postId',async(req,res)=>{
    try{
        const deletePostById = await Post.deleteOne({_id:req.params.postId})
        res.send(deletePostById)
    }catch(err){
        res.send({message:err})
    }
})

// PATCH (Update)
router.patch('/:postId', async(req,res) =>{
    try{
        const updatePostById = await Post.updateOne(
            {_id:req.params.postId},
            {$set:{
                title:req.body.title,
                topic:req.body.topic,
                message:req.body.message
                }
            })
        res.send(updatePostById)
    }catch(err){
        res.send({message:err})
    }
})

module.exports = router
