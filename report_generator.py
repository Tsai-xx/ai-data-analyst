from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_report(summary):
    prompt = f"""
    You are a professional data analyst.

    Here is the dataset summary:
    {summary}

    Please generate:
    1. Key insights
    2. Potential issues
    3. Recommendations

    Keep it concise and professional.
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content