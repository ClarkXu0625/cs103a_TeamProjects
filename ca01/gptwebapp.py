'''
gptwebapp shows how to create a web app which ask the user for a prompt
and then sends it to openai's GPT API to get a response. You can use this
as your own GPT interface and not have to go through openai's web pages.

We assume that the APIKEY has been put into the shell environment.
Run this server as follows:

On Mac
% pip3 install openai
% pip3 install flask
% export APIKEY="......."  # in bash
% python3 gptwebapp.py

On Windows:
% pip install openai
% pip install flask
% $env:APIKEY="....." # in powershell
% python gptwebapp.py
'''
from flask import request, redirect, url_for, Flask, render_template
from gpt import GPT
import os


app = Flask(__name__)
gptAPI = GPT(os.environ.get('APIKEY'))

# Set the secret key to some random bytes. Keep this really secret!
# app.secret_key = b'_5#y2L"F4Q789789uioujkkljkl...8z\n\xec]/'

# @app.route('/')
# def index():
#  ''' display a link to the general query page '''
# print('processing / route')
#  return f'''
#    <h1>GPT Demo</h1>
#     <a href="{url_for('gptdemo')}">Ask questions to GPT</a>
# '''


@app.route('/')
def index():
    ''' display a link to each team member's page '''
    return f'''
        <html style="font-family: Arial, Helvetica, sans-serif;">
        <h1>COSI 103a Team 2</h1>

        <figure>
        <figcaption>Website Breakdown</figcaption>
        <ul>

        <li><a href="/about">About us</a></li>
        <li><a href="/team">Team Biographies</a></li>

        </ul>
        </figure>

        <figure>
        <figcaption>Team Member GPT Prompts</figcaption>
        <ul>
        <li><a href="/EphraimZimmerman">Ephraim Zimmerman</a></li>
        <li><a href="/JohnXie">John Xie</a></li>
        <li><a href="/ClarkXu">Clark Xu</a></li>
        </ul>
        </figure>
        </html>
    '''
# render_template("index.html")


@app.route('/about')
def about():
    ''' display information about the program '''

    return f'''
    <!DOCTYPE html>
        <html style="font-family: Arial, Helvetica, sans-serif;">
        <head>
            <title>About Us</title>
        </head>
        <body>
            <h1>About Us</h1>
            <h4>Here is some information about our program and what it does.</h4>
            <p>We have designed a webapp that interacts with the OpenAI API.
            Each of our team member designed a function to help you get response in specific scenario
                <li><a>Ephraim Zimmerman: bullets for resume, could be used for LinkedIn</a></li>
                <li><a>John Xie: generate a summary from gpt </a></li>
                <li><a>Clark Xu: rewrite the prompt in 10th grade readability when you read complex papers or articles</a></li>
            </p>
        </body>
        </html>

    '''


@app.route('/team')
def team():
    ''' display a page with information about the team '''
    return f'''
    
    <!doctype html>
        <html style="font-family: Arial, Helvetica, sans-serif;">
    <head>
        <title>Team Page</title>
    </head>
    <body>
        <h1>Our Team</h1>
        <h2>John Xie</h2>
        <p>I've initialize the project, such create all folders,files, and basic layout. I also finish my own page.</p>
        
        <h2>Ephraim Zimmerman</h2>
        <p>As a short introduction, I am a sophomore majoring in Computer Science! I stylized the HTML pages and improved on the files linked throughout the site. Also fixed various bugs having to do with loading the HTML and connecting ChatGPT with our site.  </p>
        
        <h2>Clark Xu</h2>
        <p>I wrote the 'About us' HTML page and styled it. I also wrote my function page for reformating text readability.</p>
    </body>
    </html>
    
    '''


@app.route('/<member>', methods=['GET', 'POST'])
def gptdemo(member):
    ''' handle a get request by sending a form 
        and a post request by returning the GPT response
    '''
    
    description = None
    john_description = "enter article or a piece of text, then it will return a summary of it."
    ephraim_description = "Enter what you do for work, and we will give you  bullet points you can put on your resume/LinkedIn!"
    clark_description = "Rewrite the prompt in 10th grade readability"

    if member == "EphraimZimmerman":
        description = ephraim_description
    elif member == "JohnXie":
        description = john_description
    elif member == "ClarkXu":
        description = clark_description
    else:
        description = "Invalid member! Please go back and try again."


    if request.method == 'POST':
        prompt = request.form['prompt']
        if member == 'JohnXie':
            description = ""
            answer = gptAPI.get_summary(prompt)
        elif member == 'ClarkXu':
            # modify here for your own method
            description = ""

            answer = gptAPI.rewrite_tenth_grade_readability(prompt)
        elif member == 'EphraimZimmerman':
            # modify here for your own method
            description = "Hello!"
            answer = gptAPI.generate_linkedin_response(prompt)
        else:
            answer = "Invalid member"
        return f'''

    <html style="font-family: Arial, Helvetica, sans-serif;">

        <h1>GPT Demo for {member}</h1>
        <pre style="bgcolor:yellow">{prompt}</pre>
        <hr>
        Here is the answer in text mode:
        <div style="border:thin solid black">{answer}</div>
        Here is the answer in "pre" mode:
        <pre style="border:thin solid black">{answer}</pre>
        <a href='/{member}'> make another query</a>
                    </html>

        '''
    else:
        return f'''
        
        <html style="font-family: Arial, Helvetica, sans-serif;">

        <h1>GPT Demo for {member}</h1>
        <i>{description}</i>
        <br></br>
        <form method="post">
            <textarea style= 'width:50%; height:10%' name="prompt"></textarea>
            <p><input type=submit value="Get Response">
            <p>It may take up to 30 seconds to get a response! </p>
        </form>
            </html>

        '''


if __name__ == '__main__':
    # run the code on port 5001, MacOS uses port 5000 for its own service :(
    app.run(debug=True, port=5001)
