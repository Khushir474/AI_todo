from flask import Flask, render_template, request, jsonify
from ai_summarizer import ai_summarize

app = Flask(__name__)

# This will hold the user's lines of text (our "array")
notes_array = []


# def dummy_summarize(text: str) -> str:
#     """
#     Very simple 'fake AI' summarizer for now:
#     - If too long, show first 3 lines and count.
#     - This lets you build the app without any API keys.
#     """
#     lines = [line.strip() for line in text.split("\n") if line.strip()]
#     if not lines:
#         return "No notes to summarize yet."

#     if len(lines) <= 3:
#         return "Summary (simple):\n" + "\n".join(lines)

#     first_three = "\n".join(lines[:3])
#     return f"Summary (simple):\n{first_three}\n\n...and {len(lines) - 3} more line(s)."



@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/summarize", methods=["POST"])
def summarize():
    global notes_array

    data = request.get_json(force=True)
    text = data.get("text", "")

    # Convert to array (list) of lines
    notes_array = [line.strip() for line in text.split("\n") if line.strip()]

    # Call our dummy "AI"
    summary = ai_summarize(text)

    return jsonify({
        "lines": notes_array,
        "summary": summary,
    })


if __name__ == "__main__":
    app.run(debug=True)