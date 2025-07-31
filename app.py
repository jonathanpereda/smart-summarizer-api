from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api/summarize", methods=["POST"])
def summarize():
    data = request.get_json()

    if not data or "text" not in data:
        return jsonify({"error": "Missing 'text' field"}), 400
    
    inputText = data["text"]

    summary = f"(Filler summary of {len(inputText.split())} words.)"

    return jsonify({
        "original": inputText,
        "summary": summary
    })

print("Booting up app...")
if __name__ == "__main__":
    app.run(debug=True)