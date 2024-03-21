const mongoose = require('mongoose')

const PostSchema = mongoose.Schema({
    title:{
        type:String,
        required:true
    },
    /*text:{
        type:String,
        required:true
    },
    time:{
        type:Date,
        default:Date.now
    }*/
})

module.exports = mongoose.model('posts',PostSchema)