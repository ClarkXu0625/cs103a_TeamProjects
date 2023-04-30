const { Configuration, OpenAIApi } = require("openai");

const configuration = new Configuration({
  apiKey: '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'
});

async function getAiResponse(topic) {
  const openai = new OpenAIApi(configuration);
  const completion = await openai.createCompletion({
    model: "text-davinci-003",
    prompt: topic,
    max_tokens: 1024,
    n: 1,
    stop: null,
    temperature: 0.7
  });
  console.log(completion.data.choices[0].text);
}
getAiResponse("Your Prompt here");