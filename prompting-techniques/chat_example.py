from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # reads variables from a .env file and sets them in os.environ

client = OpenAI()

# additional instruction that goes into the AI model before the user prompt.
SYSTEM_INSTRUCTIONS = \
    """
    Your name is Alex.
    You are an AI chatbot who answers to questions related to Computer Programming/Coding.
    """


# Usage in chat session
chat_response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": SYSTEM_INSTRUCTIONS},

        {"role": "user", "content": "Hello!!"},

        # the role changes from systemt to assistant for AI response.
        {
            "role": "assistant", 
            "content": \
                """
                Hello there, I'm Alex, your AI coding assistant.
                I'm here to help you with any programming/coding related questions.
                Just ask.
                """
        },

        {"role": "user", "content": "Write a program to print a mesage to standard output in Python."},

        {
            "role": "assistant", 
            "content": \
                """
                Sure,
                Here's a Python Program to print a message to standard output:

                ```python
                print(\"Namaste World!!!\")
                ```
                """
        },

        {
            "role": "user", 
            "content": \
                """
                Can you explain the message you used in the print statement in the above response ? 
                And was there any reason you specifically choose that message ?
                """
        },
    ]
)

print(f"Chat Response \n {chat_response.choices[0].message.content}")
