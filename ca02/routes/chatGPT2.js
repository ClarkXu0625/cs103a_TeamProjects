const express = require('express');
const axios = require('axios');
const GPTModel = require('../models/GPT');
const router = express.Router();
const baseURL = 'https://api.openai.com/v1/engines/davinci-codex/completions';
const apiKey = "you key"


/*const chatGPT = async (inputText, userId) => {
    
    const instance = axios.create({
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${apiKey}`
        }
    });

    const payload = {
        prompt: inputText,
        max_tokens: 150,
        temperature: 0.7,
        top_p: 1,
        frequency_penalty: 0,
        presence_penalty: 0
      };

    try {
        const response = await instance.post(baseURL, payload);
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
};*/


const generateResponse = async (prompt) => {
    const apiKey = "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"; // Replace with your valid API key
    const baseURL = 'https://api.openai.com/v1/engines/davinci-codex/completions';
  
    // Set up the payload for the GPT-3 API
    const payload = {
      prompt: prompt,
      max_tokens: 150,
      temperature: 0.7,
      top_p: 1,
      frequency_penalty: 0,
      presence_penalty: 0,
    };
  
    try {
      const response = await fetch(baseURL, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${apiKey}`,
        },
        body: JSON.stringify(payload),
      });
  
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
  
      const data = await response.json();
      const output = data.choices[0].text;
      return output;
    } catch (error) {
      console.error('Error calling GPT-3 API:', error);
      return 'Sorry, an error occurred while processing your request.';
    }
  };

router.get('/chat2', (req, res)=> {
    res.render("chat2")
})

router.post('/chat2', async (req, res) => {
    console.log(req.body.inputText)
    const inputText = req.body.inputText;
    const userId = req.user._id;
    const response = await generateResponse(inputText, userId);
    res.send(response);
});

module.exports = router;
