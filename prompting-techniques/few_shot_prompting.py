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

    Examples:
    Q. What does (a + b)^2 evaluate to ?
    A. "Sorry, that's out of my scope."

    Q. Write a Python Code for adding two numbers.
    A: Here's a Pyton Code that returns the sum of two numbers:
        ```py
        def sum(a, b):
            return a + b
        ```
    """

# the contents of the user prompt.
CONTENT_1 = \
    """
    Explain what is a columb of electric charge ?
    """

CONTENT_2 = \
    """
    Write a Python Program to print "Hello World!!!"
    """

USER_REQUEST = CONTENT_2

# Usage in chat session
chat_response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": SYSTEM_INSTRUCTIONS},
        {"role": "user", "content": USER_REQUEST},
    ]
)

print(f"User Request \n {USER_REQUEST}")

print(f"Chat Response \n {chat_response.choices[0].message.content}")
