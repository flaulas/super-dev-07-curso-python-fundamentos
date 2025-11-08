from openai import OpenAI
client = OpenAI(
    api_key="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"
)

response = client.responses.create(
    model="gpt-5",
    input="Write a short bedtime story about a unicorn."
)

print(response.output_text)
