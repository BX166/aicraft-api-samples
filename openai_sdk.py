"""Minimal AICraft API example.

    pip install openai
    export AICRAFT_API_KEY="your key"
    python openai_sdk.py
"""

import os

from openai import OpenAI

BASE_URL = "https://aicraftapi.com/v1"


def main() -> None:
    api_key = os.environ.get("AICRAFT_API_KEY")
    if not api_key:
        raise SystemExit("Set AICRAFT_API_KEY first.")

    client = OpenAI(base_url=BASE_URL, api_key=api_key)

    # The ids this key can actually call. Read the model from here rather than
    # copying one out of a table, ours included - the catalog changes.
    models = client.models.list()
    print(f"{len(models.data)} models available")
    for model in models.data[:5]:
        print(f"  {model.id}")

    response = client.chat.completions.create(
        model="anthropic/claude-sonnet-5",
        messages=[{"role": "user", "content": "Reply with the single word: ok"}],
        max_tokens=16,
    )
    print("reply:", response.choices[0].message.content)


if __name__ == "__main__":
    main()
