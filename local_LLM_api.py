"""
Experiment for connecting to localy ran LLM.
Before start:
1) install LM Studio
2) download any model, start it, check that chat with localy runing LLM works well
3) start local LM Studio server to open LLM API, be sure it is on http://localhost:1234
"""
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load credentials as environment variables from .env file
load_dotenv()

llm = OpenAI(
    api_key="no-needed",
    base_url="http://localhost:1234/v1"
)
system_prompt = """Given the following topic description
              write 3 attention-grabbing headlines for an article.
                Reply only with the titles, one on each line, with no additional text"""
user_prompt = "The Importance of the Earthworm"

response = llm.chat.completions.create(
    model="local-model",
    max_tokens=64,
    temperature=0.8,
    messages=[
        {
            "role": "system",
            "content":system_prompt
        },
        {
            "role": "user",
            "content": user_prompt
        }
    ]
)

result = str(response.choices[0].message.content).strip('`')
print(result)