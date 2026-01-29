# ai_summarizer.py
from openai import OpenAI
from config import OPENAI_API_KEY, OPENAI_MODEL


# Create a single client that can be reused
client = OpenAI(api_key=OPENAI_API_KEY)


def ai_summarize(text: str) -> str:
    """
    Use OpenAI to summarize the user's notes.
    """
    text = text.strip()
    if not text:
        return "No notes to summarize yet."

    try:
        response = client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=[
                {
                    "role": "system",
                    "content": "You summarize the user's to-do list into a short, clear note.",
                },
                {
                    "role": "user",
                    "content": f"Summarize these notes into a concise note:\n\n{text}",
                },
            ],
            temperature=0.4,
        )

        summary = response.choices[0].message.content.strip()
        return summary or "The AI returned an empty summary."

    except Exception as e:
        # Basic fallback if something goes wrong
        return f"Summarization failed: {e}"