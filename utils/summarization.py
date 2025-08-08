import openai

def summarize_file(text):
    """
    Generate a concise summary from the provided text using OpenAI completion API.

    Args:
        text (str): Text to summarize.

    Returns:
        str: Generated summary.
    """
    prompt = (
        "Please produce a concise summary of the following conversation transcript:\n\n"
        + text
        + "\n\nSummary:"
    )

    response = openai.ChatCompletion.create(
        model="gpt-4",  # Or "gpt-3.5-turbo"
        messages=[
            {"role": "system", "content": "You are a helpful assistant that summarizes conversations."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=150,
        temperature=0.5,
    )

    summary = response.choices[0].message.content.strip()
    return summary
