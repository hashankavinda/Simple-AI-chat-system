from flask import Flask, render_template

import sys
#register directory paths
sys.path.insert(1, '/assets')

#import OpenAIApiKey as a variable to be used
import assets.openAIapikey as apiKey

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/error")
def error():
    return render_template("error.html")

if __name__ == "__main__":
    app.run(debug=True)