const GPTModel = require('../models/GPT');
const express = require('express');
const router = express.Router();
const { Configuration, OpenAIApi } = require("openai");

const configuration = new Configuration({
  apiKey: '',
});
const openai = new OpenAIApi(configuration);

router.get('/chat2', async (req, res) => {
  try {
    const previousResponses = await GPTModel.find({ userId: req.user._id });
    res.render("chat2/new");
  } catch (error) {
    console.error(error);
    res.status(500).send('Error fetching previous responses. Please try again later.');
  }
});

// Get the prompt and input message from new.ejs
// Sending message to GPT to generate output
// Save the output into database to call later.
router.post('/chat2', async (req, res) => {
  const {inputPrompt, inputText} = req.body;
  try {
    console.log('Sending request to OpenAI API...');
    const result = await openai.createCompletion({
      model: "text-davinci-003",
      prompt: `${inputPrompt} : ${inputText}`,
      max_tokens: 1024,
      n: 1,
      stop: null,
      temperature: 0.7,
    });

    // generated output
    const generatedParagraph = result.data.choices[0].text.trim();
    //console.log(generatedParagraph);
    
    const gptResponse = new GPTModel({
      prompt: inputPrompt,
      input: inputText,
      output: generatedParagraph,
      userId: req.user._id,
    });

    await gptResponse.save();

    res.render('generated-paragraph', { paragraph: generatedParagraph });
  } catch (error) {
    console.error(error);
    res.status(500).send('Error generating paragraph. Please try again later.');
  }
});

router.post('/history', async (req, res) => {

});

module.exports = router;