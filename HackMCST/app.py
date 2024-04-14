from openai import OpenAI
from flask import Flask, render_template, request

client = OpenAI(
    api_key="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"
)

def gpt(prompt):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful, kind, and sensitive model acting as a model for people to talk to and vent their frustrations. You should always be as helpful as possible and respond with a conversational tone, with a focus on minimal length."},
            {"role": "user", "content": prompt+" Based on the above text, generate a percentage representing the mental health of the user. If this percentage is under 60, provide the user with a short list of resources pertaining to their specific mental health situation"}
        ]
    )
    return completion.choices[0].message.content

app = Flask(__name__) 
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/", methods=['POST'])
def second_page():
    html_data = request.form["entry"]
    return render_template("index2.html", response=gpt(html_data))
app.run(host="0.0.0.0")