from flask import Flask, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()
api_key = os.getenv("OPEN_API_KEY")

client = OpenAI(api_key=api_key)


def generateSummary(text, length, style):
    #Message sent to GPT
    prompt = f""
    match style:
        case "formal":
            prompt = f"Formally summarize the following text in 2-3 sentences:\n\n{text}"
        case "casual":
            prompt = f"Casually summarize the following text in 2-3 sentences:\n\n{text}"
        case _:
            prompt = f"Summarize the following text in 2-3 sentences:\n\n{text}"
    #Determine desired summary length
    lengthControl = 150
    match length:
        case "short":
            lengthControl=75
        case "medium":
            lengthControl=150
        case "long":
            lengthControl=250

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            #message from 'system' to GPT to set behavior
            {"role": "system", "content": "You are a text summarization assistant."},
            #message from 'user' to GPT prompting a response.
            {"role": "user", "content": prompt}
        ],
        #Creativity/randomness determiner [0=dry] -> [1=creative]
        temperature=0.7,
        #Control max length of response summary
        max_tokens=lengthControl
    )
    summary = response.choices[0].message.content.strip()
    return summary

@app.route("/api/summarize", methods=["POST"])
def summarize():
    #read in from user
    data = request.get_json()
    length = data.get("length", "medium").lower()
    style = data.get("style", "formal").lower()

    #make sure user inputs good data
    if not data or "text" not in data:
        return jsonify({"error": "Missing 'text' field"}), 400
    
    #get string from user input
    inputText = data["text"]

    summary = generateSummary(inputText, length, style)

    return jsonify({
        "original": inputText,
        "summary": summary
    })

print("Booting up app...")
if __name__ == "__main__":
    app.run(debug=True)