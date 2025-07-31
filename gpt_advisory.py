from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def load_prompt_template():
    with open("prompt_template.txt") as f:
        return f.read()

def get_advice_from_gpt(market_data):
    prompt = load_prompt_template().replace("{{market_data}}", market_data)

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )

    print(response.choices[0].message.content)
    return response.choices[0].message.content
