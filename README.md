# AICraft API samples

Minimal examples for the AICraft API. It speaks the OpenAI wire format, so an OpenAI client works once you change the base URL and the key.

- Base URL — `https://aicraftapi.com/v1`
- Key — create one at <https://aicraftapi.com>

## List the models your key can call

```bash
export AICRAFT_API_KEY="your key"

curl https://aicraftapi.com/v1/models \
  -H "Authorization: Bearer $AICRAFT_API_KEY"
```

The response lists the ids your key can actually call. Read the id from there rather than copying one out of a table, ours included — the catalog changes.

## Chat completion

[`openai_sdk.py`](openai_sdk.py) uses the official OpenAI Python SDK:

```python
import os

from openai import OpenAI

client = OpenAI(
    base_url="https://aicraftapi.com/v1",
    api_key=os.environ["AICRAFT_API_KEY"],
)

response = client.chat.completions.create(
    model="anthropic/claude-sonnet-5",
    messages=[{"role": "user", "content": "Reply with the single word: ok"}],
    max_tokens=16,
)

print(response.choices[0].message.content)
```

Both calls were run against the live endpoint while writing this file: `GET /v1/models` returned 200, and the chat call above returned 200 with `finish_reason: "stop"`.
