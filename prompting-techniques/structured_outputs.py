from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # reads variables from a .env file and sets them in os.environ

client = OpenAI()

# additional instruction with examples that goes into the AI model before the user prompt.
# the more examples we provide, the better will be the results
SYSTEM_INSTRUCTIONS = \
"""
You are a data-extraction assistant.
Given a user feedback string (“Input”), extract these fields:
- type
- severity
- description
Return output strictly in valid JSON with exactly the above listed attributes as JSON keys:

```json
{
    "type": "bug" | "feature_request" | "feedback", 
    "serverity": "high" | "medium" | "low", 
    "summary": "Summary of the user feedback in 1 scentence"
}
```

Example 1: 
Input: "App crashes on Save button click." 
Output: {"type": "bug", "serverity": "high", "summary": "Crash on Save"}

Example 2: 
Input: "I love the new UI update, super smooth!" 
Output: {"type": "feedback", "serverity": "low", "summary": "Positive user feedback on UI"}

Example 3 
Input: "I wish there was a dark mode option.." 
Output: {"type": "feature_request", "serverity": "medium", "summary": "New feature request to have Dark mode in UI."}
"""

# the contents of the user prompt.
CONTENT_1 = \
"""
The submit button freezes on mobile devices sometimes.
"""

CONTENT_2 = \
"""
There's a minor UI issue,
The Search button overlaps a bit with my profile icon.
A fix would be great. 
Thanks in advance.
"""

CONTENT_3 = \
"""
I would like to get watsapp notification message at the morning of my orders arrival date.
Very dissappointing that the app lacks such a basic feature.
Most of the competetors do have it.
"""

# set the prompt here
USER_PROMPT = CONTENT_3

# Usage in chat session
chat_response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": SYSTEM_INSTRUCTIONS},
        {"role": "user", "content": USER_PROMPT},
    ]
)

print(f"User Request:\n {USER_PROMPT}")

print(f"Chat Response:\n {chat_response.choices[0].message.content}")
