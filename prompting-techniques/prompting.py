from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # reads variables from a .env file and sets them in os.environ

client = OpenAI()

# additional instruction that goes into the AI model before the user prompt.
system_instructions = \
    """
    Always keep your responses precise. Answer in a maximum of 2-3 scentences.
    """

# the contents of the user prompt.
content= \
    """
    Explain what is an LLM in
    """


# Usage in chat session
chat_response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": system_instructions},
        {"role": "user", "content": content},
    ]
)

print(f"Chat Response \n {chat_response.choices[0].message.content}")
