const GPTModel = require('../models/GPT');
const express = require('express');
const router = express.Router();
const openai = require('openai');

openai.apiKey = 'your_openai_api_key';

router.get('/generate-paragraph', async (req, res) => {
  try {
    const previousResponses = await GPTModel.find({ userId: req.user._id }); // Assuming 'req.user' contains the logged-in user information

    res.render('generate-paragraph', { previousResponses });
  } catch (error) {
    console.error(error);
    res.status(500).send('Error fetching previous responses. Please try again later.');
  }
});

router.post('/generate-paragraph', async (req, res) => {
  const topic = req.body.topic;

  try {
    const result = await openai.Completion.create({
      engine: 'text-davinci-002',
      prompt: `Write a paragraph about ${topic}`,
      max_tokens: 100,
      n: 1,
      stop: null,
      temperature: 0.7,
    });

    const generatedParagraph = result;

    // Save the user response to the database
    const gptResponse = new GPTModel({
      prompt: `Write a paragraph about ${topic}`,
      input: topic,
      output: generatedParagraph,
      userId: req.user._id, // Assuming 'req.user' contains the logged-in user information
    });

    await gptResponse.save();

    res.render('generated-paragraph', { paragraph: generatedParagraph });
  } catch (error) {
    console.error(error);
    res.status(500).send('Error generating paragraph. Please try again later.');
  }
});
