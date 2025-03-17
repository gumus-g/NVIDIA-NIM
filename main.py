import os
from dotenv import load_dotenv
from openai import OpenAI

# load the .env file
load_dotenv()

# Access the API key
api_key = os.getenv('nim_api_key')

client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  #api_key = "$API_KEY_REQUIRED_IF_EXECUTING_OUTSIDE_NGC"
  api_key = api_key
)
completion = client.chat.completions.create(
  model="meta/llama-3.3-70b-instruct",
  messages=[{"role":"user","content":"Write a limerick about the wonders of GPU computing."}],
  temperature=0.2,
  top_p=0.7,
  max_tokens=1024,
  stream=True
)
for chunk in completion:
  if chunk.choices[0].delta.content is not None:
    print(chunk.choices[0].delta.content, end="")