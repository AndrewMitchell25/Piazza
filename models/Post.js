const mongoose = require('mongoose')

const PostSchema = mongoose.Schema({
    title:{
        type:String,
        required:true
    },
    topic: [{
        type: String,
        enum: ['politics', 'health', 'sport', 'tech'],
        required: true
    }],
    timestamp: {
        type:Date,
        default:Date.now
    },
    message: {
        type:String,
        required:true
    }
})

module.exports = mongoose.model('posts',PostSchema)