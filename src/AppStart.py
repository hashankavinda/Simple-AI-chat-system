from flask import Flask, render_template, request, jsonify
from openai import OpenAI

#import OpenAIApiKey as a variable to be used
import assets.configurations as config

client = OpenAI(api_key=config.OPENAI_API_KEY)

import sys
#register directory paths
sys.path.insert(1, '/assets')


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/query", methods=["POST", "GET"])
def query():
    try:
        userInput = request.json.get("query", "")
        if not userInput:
            return jsonify({ "error": "Text value is empty."}), 400

        response = client.chat.completions.create(model = "gpt-3.5-turbo",
        messages = [{
            "role": "user",
            "content": userInput
        }])

        output = response.choices[0].message.content.strip()
        return jsonify({ "output": output })

    except Exception as e:
        return jsonify({ "error": str(e) }), 500

@app.route("/error")
def error():
    return render_template("error.html")

if __name__ == "__main__":
    app.run(debug=True)