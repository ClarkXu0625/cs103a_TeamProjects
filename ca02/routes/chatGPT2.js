const express = require('express');
const axios = require('axios');
const GPTModel = require('../models/GPT');
const router = express.Router();
const baseURL = "you key";
const apiKey = "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";

const chatGPT = async (inputText, userId) => {
    
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
};

router.get('/chat2', (req, res)=> {
    res.render("chat2")
})

router.post('/chat2', async (req, res) => {
    console.log(req.body.inputText)
    const inputText = req.body.inputText;
    const userId = req.user._id;
    const response = await chatGPT(inputText, userId);
    res.send(response);
});

module.exports = router;
