from openai import OpenAI

client = OpenAI()

def detect_anomaly(message, retrieved_examples):
    prompt = f"""
You are a financial risk analyst.

Normal customer behavior:
{retrieved_examples}

Current customer message:
"{message}"

Decide whether the behavior is anomalous.

Respond in JSON:
{{
  "anomaly": true/false,
  "risk_level": "low | medium | high",
  "reason": "short explanation"
}}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    return response.choices[0].message.content
