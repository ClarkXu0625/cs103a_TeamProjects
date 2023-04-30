const express = require('express');
const router = express.Router();
const GPTModel = require('../models/GPT');

// Middleware to check if user is logged in
function isLoggedIn(req, res, next) {
    if (res.locals.loggedIn) {
      next();
    } else {
      res.redirect('/login');
    }
}

router.get('/chatgpt', isLoggedIn, async (req, res) => {
    gpt = await GPTModel.find({ userId: req.user._id })
    res.render('chatgpt', { gpt });
});

// POST route for creating a new chat with openAI
router.post('/chatgpt', isLoggedIn, async (req, res) => {
    const newGPT = new GPTModel({
      input : req.body.input,
      output : req.body.output,
      userId: req.user._id,
    });
  
    await newGPT.save();
    res.redirect('/chatgpt');
  });