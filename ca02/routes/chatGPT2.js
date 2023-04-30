const express = require('express');
const axios = require('axios');
const GPTModel = require('../models/GPT');
const router = express.Router();

const chatGPT = async (inputText, userId) => {
    // Check if the input already exists in the database
  const existingEntry = await GPTModel.findOne({ input: inputText, userId });
  if (existingEntry) {
    // If it exists, return the stored output
    return existingEntry.output;
  }
  
    // If it doesn't exist, make a request to the ChatGPT API
    const apiKey = process.env.CHATGPT_API_KEY;
    const instance = axios.create({
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${apiKey}`
      }
    });
  
    const payload = {
      // Your payload specific to the ChatGPT API you're using
    };
  
    try {
      const response = await instance.post('https://api.openai.com/v1/engines/davinci-codex/completions', payload);
      output = response.data.choices[0].text;
    } catch (error) {
      console.error('Error calling ChatGPT API:', error);
      output = 'Sorry, an error occurred while processing your request.';
    }
  

  

  // Save the output to the database
  const newEntry = new GPTModel({
    prompt: 'ChatGPT',
    input: inputText,
    output,
    userId,
  });
  await newEntry.save();

  return output;
};

router.get('/chat2', (req, res)=> {
    res.render("chat2")
})

router.post('/chat2', async (req, res) => {
  const inputText = req.body.inputText;
  const userId = req.user._id;
  const response = await chatGPT(inputText, userId);
  res.send(response);
});

module.exports = router;
