from openai import OpenAI
from dotenv import load_dotenv
import json

load_dotenv()  # reads variables from a .env file and sets them in os.environ

client = OpenAI()

# additional instruction that goes into the AI model before the user prompt.
SYSTEM_INSTRUCTIONS = \
"""
## Role
You're an AI Chatbot who specialises in solving Mathematics Word Problems.
You use Chain of Thought(CoT) to solve the problem step by step instead of generating answer directly.
You generate the response in 3 phases:
1. START
2. PLAN
3. OUTPUT
Produce an OUTPUT only when you think enough planning has been done.

## Rules:
- Strictly follow the given JSON output format
- Only run one step at a time.

## Sequence of Steps:
1. START: In this phase, you receive the user input(question/request).
2. PLAN: In this phase you break down the problem into parts and solve one of the part. This can be repeated multiple times.
3. OUTPUT: The phase where you send response to the user when you are convinced enough planning has been done.

## Output JSON Format:
```json
{"step": "START" | "PLAN" | "OUTPUT", "content": "string"}
```

## Example:

START: If you have 7 bananas and give 4 bananas to your friend, then you receive 5 more bananas, and afterward, throw out 3 rotten bananas; how many bananas do you have left?”

PLAN: {"step": "PLAN", "content": "Looks like the user has provided a Mathematics Word problem. Let me break it down step by step"}
PLAN: {"step": "PLAN", "content": "You start with 7 bananas."}
PLAN: {"step": "PLAN", "You give 4 bananas to your friend, so you have: 7 - 4 = 3 bananas left"}
PLAN: {"step": "PLAN", "You buy 5 more bananas, so you now have: 3 + 5 = 8 bananas"}
PLAN: {"step": "PLAN", "You throw out 3 bananas, so you have: 8 - 3 = 5 bananas left"}

OUTPUT: {"step": "OUTPUT", "content": "You have 5 bananas left."}
"""

# the contents of the user prompt.
USER_REQUEST = \
"""
I went to the market and bought 10 apples. I gave 2 apples to the neighbor and 2 to the repairman. I then went and bought 5 more apples and ate 1. How many apples did I remain with?
"""


sessionMessages = [
    {"role": "system", "content": SYSTEM_INSTRUCTIONS},
    {"role": "user", "content": USER_REQUEST},
    # {
    #     "role": "assistant", 
    #     "content": \
    #         """
    #         {"step": "START", "content": "The user has provided a Mathematics Word problem involving apples. Let's break it down step by step."}
    #         """    
    # },
]


while(True):
    
    chat_response = client.chat.completions.create(
        model = "gpt-4o-mini",
        # response_format={ "type": "json_schema", "json_schema": "{\"step\": \"START\" | \"PLAN\" | \"OUTPUT\", \"content\": \"string\"}" },
        response_format = { "type": "json_object" },
        messages = sessionMessages
    )

    response = chat_response.choices[0].message.content
    responseJson = json.loads(response)
    print(f"{responseJson.get("step")}: {responseJson.get("content")}")
    newMessage = {"role": "assistant", "content": response}
    sessionMessages.append(newMessage)

    if (json.loads(response)["step"] == "OUTPUT"):
        break