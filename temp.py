import os
from openai import AzureOpenAI

# Initialize Azure OpenAI client with key-based authentication
client = AzureOpenAI(
    azure_endpoint = "https://dmitr-m1q9cxme-francecentral.openai.azure.com/",
    api_key = "216c776191104b86a014089dc303d4ac",
    api_version = "2024-05-01-preview",
)

completion = client.chat.completions.create(
    model="gpt-35-turbo",
    messages= [
    {
        "role": "system",
        "content": "You are an AI assistant that helps people find information."
    },
    {
        "role": "user",
        "content": "Hello"
    },
    {
        "role": "assistant",
        "content": "Hello! How can I assist you today?"
    }
],
    # past_messages=10,
    max_tokens=800,
    temperature=0.7,
    top_p=0.95,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None,
    stream=False
)

print(completion.to_json())