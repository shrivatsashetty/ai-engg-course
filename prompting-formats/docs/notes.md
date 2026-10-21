# Prompting Formats

## Alpaca Style Prompting
The Alpaca prompt format is a standardized template created by Stanford researchers in 2023 for training and prompting instruction-following language models like LLaMA. It breaks a task down into clear, labeled sections so the model understands the distinction between the request, any extra data, and the expected answer.

Here's how it looks like:

```md
Below is an instruction that describes a task, paired with an input 
that provides further context. Write a response that appropriately 
completes the request.

### Instruction:
{}

### Input:
{}

### Response:
{}
```

**The Three Parts:**

Here's a breakdown of what the 3 parts of an Aplaca Prompt Template are

1. Instructions
    The main task or question — The What

    ```md
    ### Instruction:
    Explain what photosynthesis is
    ```

2. Input
    Additional context (optional, can be empty)- The Context

    ```md
    ### Input:
    For a 10-year-old student
    ```

3. Response
    The answer the model should generate — The How

    ```md
    ### Response:
    Photosynthesis is how plants make food using sunlight...
    ```

**Example:**

```md
Below is an instruction that describes a task, paired with an input 
that provides further context. Write a response that appropriately 
completes the request.

### Instruction:
Write a short poem about time.

### Input:
The poem should consist of 4 lines 

### Response:

```


## Chat ML (Chat Markup Language)

ChatML (Chat Markup Language) structures multi-turn conversations for language models using explicit control tokens (`<|im_start|>` and `<|im_end|>`) to mark where each dialogue turn begins and ends.

A ChatML turn follows this pattern:

```md
<|im_start|>{role}
{content}
<|im_end|>
```

**Example:**

```md
<|im_start|>system
You are a helpful assistant.<|im_end|>
<|im_start|>user
Hello!<|im_end|>
<|im_start|>assistant
Hi! How can I help you today?<|im_end|>
<|im_start|>user
What's the weather?<|im_end|>
<|im_start|>assistant
```

Leaving the final `<|im_start|>assistant` open signals the model to generate its response.

**Prompt Schema:**

This JSON-style message schema

```json
{ "role": "system", "content": "<instructions>" }
{ "role": "user", "content": "<your input>" }
{ "role": "assistant", "content": "<model reply>" }
```

**Example (OpenAI SDK ):**

```py
from openai import OpenAI
client = OpenAI()

system_prompt = "You are a helpful assistant who explains technical concepts clearly."
user_city = "Bangalore"

res = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"What is the weather in {user_city} right now?"}
    ]
)

print(res.choices[0].message.content)
```

## INST 

A lighter, faster, and easier to parse version of the Chat ML format. It was developed by the Open Source community to save tokens.

**Advantages:**
- Keeps the role-awareness from ChatML
- Drops the heavy markup
- Minimizes token overhead for faster inference


**Structure:**

```md
[INST] <<SYS>>
<system message>
<</SYS>>
<user message>
[/INST]
```

**Example:**

```md
[INST] <<SYS>>
You are a concise assistant.
<</SYS>>
Explain what an LRU Cache is.
[/INST]
```

**Usage:**

```py
import ollama

prompt = """[INST] <<SYS>>
You are a concise assistant.
<</SYS>>
Explain what an LRU Cache is.
[/INST]
"""

res = ollama.chat(model="mistral", messages=[
    {"role": "user", "content": prompt}
])

print(res['message']['content'])
```
