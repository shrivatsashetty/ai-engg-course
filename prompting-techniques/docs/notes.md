# Prompting

## Zero Shot Prompting

Zero Shot Prompting is a technique to prompt AI models where you ask an the model to perform a task using only a direct instruction, without providing any prior examples, sample outputs, or extra training data.

## Few Shot Prompting

Few-shot prompting is a prompt engineering technique where you provide a Large Language Model (LLM) with a small number of input-output examples (usually 2 to 5) directly inside the prompt to guide its behavior

A "shot" means a single example.

- Zero-shot: No examples provided (instructions only).
- One-shot: A single example provided.
- Few-shot: Two or more examples provided (typically 2–5)


## Structured Outputs


Few-shot prompting enforces structured LLM outputs (like JSON or XML) by showing the model concrete examples of valid input-to-output pairs directly inside the prompt. Instead of relying on vague adjectives ("return clean JSON"), examples teach the model exact syntax, key names, and data types.

**Example:**

```md
You are a data-extraction assistant.
Given a user feedback string (“Input”), extract these fields:
- type
- severity
- description
Return output strictly in valid JSON with exactly the above listed attributes as JSON keys:

```
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
```

**Best Practices:**

- Choose 3 to 5 diverse examples: Include a standard case, an ambiguous case, and an edge case to prevent the model from overfitting to a single pattern.
- Match production reality: Base your few-shot examples on real logs or real user inputs rather than overly simple synthetic strings.
- Lock the temperature low: Set temperature = 0.0 (or near zero) in your API client to maximize deterministic output formatting.

## Chain of Thought (CoT) Prompting

an AI prompt engineering technique that guides a large language model to solve complex problems through a series of intermediate logical steps before giving a final answer.

**How CoT Works:**
- Decomposition: It breaks a difficult task down into smaller, sequential parts rather than jumping straight to a final guess.
- Zero-Shot CoT: You trigger this simply by adding phrases like "Let's think step by step" to your prompt.
- Few-Shot CoT: You provide the model with a few example questions that explicitly show the question, the step-by-step rationale, and the final answer.


**Core Benefits:**

- Higher Accuracy: It dramatically improves performance on math word problems, logical puzzles, and coding tasks.
- Transparency: You can read the model's logic and spot where a mistake happens.

**Common Use Cases:**

- Multi-step arithmetic: Solving word problems that require adding, subtracting, or multiplying in order.
- Software debugging: Tracing code or logic backward from an error.
- Commonsense reasoning: Explaining the real-world rules behind why a scenario makes sense.

**Examples:**
```md
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

`{"step": "START" | "PLAN" | "OUTPUT", "content": "string"}`


## Example:

START: If you have 7 bananas and give 4 bananas to your friend, then you receive 5 more bananas, and afterward, throw out 3 rotten bananas; how many bananas do you have left?”

PLAN: {"step": "PLAN", "content": "Looks like the user has provided a Mathematics Word problem. Let me break it down step by step"}
PLAN: {"step": "PLAN", "content": "You start with 7 bananas."}
PLAN: {"step": "PLAN", "You give 4 bananas to your friend, so you have: 7 - 4 = 3 bananas left"}
PLAN: {"step": "PLAN", "You buy 5 more bananas, so you now have: 3 + 5 = 8 bananas"}
PLAN: {"step": "PLAN", "You throw out 3 bananas, so you have: 8 - 3 = 5 bananas left"}

OUTPUT: {"step": "OUTPUT", "content": "You have 5 bananas left."}
```

