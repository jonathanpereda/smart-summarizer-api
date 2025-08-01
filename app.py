from flask import Flask, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()
api_key = os.getenv("OPEN_API_KEY")

client = OpenAI(api_key=api_key)


def generateSummary(text):
    #Message sent to GPT
    prompt = f"Summarize the following text in 2-3 sentences:\n\n{text}"

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            #message from 'system' to GPT to set behavior
            {"role": "system", "content": "You are a text summaization assistant."},
            #message from 'user' to GPT prompting a response.
            {"role": "user", "content": prompt}
        ],
        #Creativity/randomness determiner [0=dry] -> [1=creative]
        temperature=0.7,
        #Control max length of response summary
        max_tokens=150
    )
    summary = response.choices[0].message.content.strip()
    return summary

@app.route("/api/summarize", methods=["POST"])
def summarize():
    #read in from user
    data = request.get_json()

    #make sure user inputs good data
    if not data or "text" not in data:
        return jsonify({"error": "Missing 'text' field"}), 400
    
    #get string from user input
    inputText = data["text"]

    summary = generateSummary(inputText)

    return jsonify({
        "original": inputText,
        "summary": summary
    })

print("Booting up app...")
if __name__ == "__main__":
    app.run(debug=True)