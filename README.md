# Smart Summarizer API

Python Flask API using OpenAI’s GPT model to generate smart summaries.

## Features

- AI-generated summaries using GPT-3.5
- Adjustable summary length: `short`, `medium`, or `long`
- Optional style tone: `formal` or `casual`
- JSON-based POST endpoint for easy integration

## Example Request

```bash
curl -X POST http://127.0.0.1:5000/api/summarize \
-H "Content-Type: application/json" \
-d '{
  "text": "Your long input text here...",
  "length": "short",
  "style": "casual"
}'
```

## Setup

1. Clone this repo:

```bash
git clone https://github.com/jonathanpereda/smart-summarizer-api.git
cd smart-summarizer-api
```

2. Create a virtual environment and activate it:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Add your OpenAI API key to a `.env` file:

```
OPEN_API_KEY=your_key_here
```

5. Run the app:

```bash
python app.py
```

## Notes

- Must have an OpenAI API key with available credits.
- You can change the summary style and length using the optional request fields.

## Author

Jonathan Pereda