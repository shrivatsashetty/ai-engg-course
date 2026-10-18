from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # reads variables from a .env file and sets them in os.environ

client = OpenAI()

# additional instruction that goes into the AI model before the user prompt.
SYSTEM_INSTRUCTIONS = \
    """
    Your name is Alex.
    You are an AI chatbot who answers to questions related to Computer Programming/Coding.
    Apart from that you do not answer to questions related to other topics.
    If a user aks a question related to some other topics, 
    then just reply with "Sorry, that's out of my scope."
    """

# the contents of the user prompt.
CONTENT = \
    """
    Explain what is a columb of electric charge ?
    """


# Usage in chat session
chat_response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": SYSTEM_INSTRUCTIONS},
        {"role": "user", "content": CONTENT},
    ]
)

print(f"User Request \n {CONTENT}")

print(f"Chat Response \n {chat_response.choices[0].message.content}")
