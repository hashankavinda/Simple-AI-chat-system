from flask import Flask, render_template
import openai

import sys
#register directory paths
sys.path.insert(1, '/assets')

#import OpenAIApiKey as a variable to be used
import assets.configurations as config

app = Flask(__name__)

openai.api_key = config.OPENAI_API_KEY

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/error")
def error():
    return render_template("error.html")

if __name__ == "__main__":
    app.run(debug=True)