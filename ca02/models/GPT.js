'use strict';
const mongoose = require( 'mongoose' );
const Schema = mongoose.Schema;

var gptSchema = Schema( {
  input:String,
  output: String,
  userId: {type:ObjectId, ref:'user' }
});

module.exports = mongoose.model( 'GPTModel', gptSchema );
