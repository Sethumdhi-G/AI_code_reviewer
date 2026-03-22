from flask import Flask, render_template, request, jsonify
from anthropic import Anthropic
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

SYSTEM_PROMPT = """You are an expert code reviewer with deep knowledge across multiple programming languages.
When given code, analyze it and provide structured feedback in the following format:

## Summary
A one-line overall assessment.

## Bugs & Errors
List any bugs, logic errors, or potential runtime issues. If none, say "None found."

## Code Quality
Comment on readability, naming conventions, structure, and style.

## Performance
Highlight any inefficiencies or improvements.

## Security
Flag any security vulnerabilities (SQL injection, hardcoded secrets, etc.). If none, say "None found."

## Suggestions
3-5 concrete, actionable improvements with brief code examples where helpful.

## Score
Rate the code from 1–10 and explain why.

Be constructive, specific, and educational. Tailor feedback to the language used."""


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/review", methods=["POST"])
def review():
    data = request.get_json()
    code = data.get("code", "").strip()
    language = data.get("language", "auto-detect")

    if not code:
        return jsonify({"error": "No code provided."}), 400

    user_message = f"Language: {language}\n\nCode to review:\n```\n{code}\n```"

    try:
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1500,
            system=SYSTEM_PROMPT,
            messages=[{"role": "user", "content": user_message}],
        )
        review_text = response.content[0].text
        return jsonify({"review": review_text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
