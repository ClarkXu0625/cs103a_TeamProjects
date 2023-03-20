'''
Demo code for interacting with GPT-3 in Python.

To run this you need to 
* first visit openai.com and get an APIkey, 
* which you export into the environment as shown in the shell code below.
* next create a folder and put this file in the folder as gpt.py
* finally run the following commands in that folder

On Mac
% pip3 install openai
% export APIKEY="......."  # in bash
% python3 gpt.py

On Windows:
% pip install openai
% $env:APIKEY="....." # in powershell
% python gpt.py
'''
import openai
openai.api_key = "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"

class GPT():
    ''' make queries to gpt from a given API '''
    def __init__(self,apikey):
        ''' store the apikey in an instance variable '''
        self.apikey=apikey
        # Set up the OpenAI API client
        openai.api_key = apikey #os.environ.get('APIKEY')

        # Set up the model and prompt
        self.model_engine = "text-davinci-003"

    def getResponse(self,prompt):
        ''' Generate a GPT response '''
        completion = openai.Completion.create(
            engine=self.model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.8,
        )

        response = completion.choices[0].text
        return response

    def get_summary(self, text, length=100):#method by John, generate a summary from gpt.
        ''' Generate a summary of a long article or text '''
        prompt = "Summarize the following text:\n\n" + text
        summary = self.getResponse(prompt)
        # Extract the summary from the response
        return summary
    

    def generate_linkedin_response(self, input, length=1200) -> str: #Created by Ephraim; bullets for resume/LinkedIn.
        """Generate bullet points in a LinkedIn style from an anecdotal summary of a job."""

        prompt = "Generate a series of bullet points for LinkedIn from this job description:\n\n" + input + "\n Separate each bullet by a line-break and expand on details, but limit it to 4-5 bullets. "
        return self.getResponse(prompt)
    
    def rewrite_tenth_grade_readability(self, input) ->str: # Written by Clark, rewrite the prompt in 10th grade readability
        prompt = "Hi GPT, can you help me rewrite the following promt in tenth grade readability:\n\n" + input
        return self.getResponse(prompt)

if __name__=='__main__':
    '''
    '''
    import os
    g = GPT("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")

    # print(g.getResponse("what does openai's GPT stand for?"))
    # text = "Blockchain technology is a distributed ledger system that allows for secure and transparent transactions between parties (Swan, 2015). Initially created to support Bitcoin, the first cryptocurrency, it has since expanded to various use cases, from financial services to supply chain management. Ethereum, unlike Bitcoin, was designed to support smart contracts and decentralized applications, making it a popular platform for developers. However, Ethereum, like other blockchain networks, faces scalability challenges, and Layer 2 scaling solutions have been developed to address this issue. One key innovation that has been enabled by blockchain technology is the concept of smart contracts, which are self-executing contracts with the terms of the agreement written directly into code (Buterin, 2014)."
    # print(g.get_summary(text))

    summary = "I am a teaching assistant for Introduction to Economics and Brandeis University with course ID ECON10a. I grade exams, essays, and homework assignments, and also help people out in general when needed. I also help the professor with lesson plans.  "
    print(g.get_summary(summary))