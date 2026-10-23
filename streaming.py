"""Streaming AICraft API example.

    pip install openai
    export AICRAFT_API_KEY="your key"
    python streaming.py
"""

import os

from openai import OpenAI

BASE_URL = "https://aicraftapi.net/v1"


def main() -> None:
    api_key = os.environ.get("AICRAFT_API_KEY")
    if not api_key:
        raise SystemExit("Set AICRAFT_API_KEY first.")

    client = OpenAI(base_url=BASE_URL, api_key=api_key)

    stream = client.chat.completions.create(
        model="anthropic/claude-sonnet-5",
        messages=[{"role": "user", "content": "Count to five, one word per line."}],
        max_tokens=64,
        stream=True,
    )

    for chunk in stream:
        delta = chunk.choices[0].delta.content
        if delta:
            print(delta, end="", flush=True)
    print()


if __name__ == "__main__":
    main()
