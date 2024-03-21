const express = require('express')
const router = express.Router()

const Post = require('../models/Post')

router.get('/', async(req,res) => {
   const posts = await Post.find()
   console.log('hello')
})

// router.get('/',(req,res) =>{
//     res.send('You are in movies router!')
// })

module.exports = router
