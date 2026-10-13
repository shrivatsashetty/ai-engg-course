
## What is an LLM ?

An LLM stands for a Large Language Model, which is a type of artificial intelligence (AI) program designed to understand, process, and generate human-like text.

### Key Characteristics

- Large: They are trained on massive datasets containing billions of words, books, articles, and web pages.

- Language: They focus on natural human communication, grammar, and context rather than just numerical data.

- Model: They rely on deep learning architectures—specifically transformer neural networks—to predict the most probable next word or token in a sequence.

### Common Uses

• Chatbots and Assistants: Powering conversational AI tools like ChatGPT, Claude, and Gemini.
• Content Generation: Writing essays, emails, stories, and computer code.
• Summarization and Translation: Condensing long documents or translating text between different languages.

## Token
A token is the fundamental unit of text—such as a whole word, part of a word, single character, or punctuation mark—that a large language model (LLM) reads, processes, and generates.

### How tokens work

- Tokenization: Before an LLM can analyze text, a software tool called a tokenizer breaks raw input text down into smaller segments known as tokens.
- 
- Rule of Thumb: In English text, 1 token is roughly 4 characters or about ¾ of a word (meaning 100 tokens equal roughly 75 words). Common words become a single token (e.g., "the"), while long or rare words split into subwords (e.g., "unbelievable" might split into "un", "believe", and "able").

- Numerical IDs: Because LLMs process numbers rather than raw text, each token is mapped to a unique number or vector from the model's fixed vocabulary (which typically contains 30,000 to 100,000+ unique tokens).

- Context Windows: A model's context window (such as 8,000 tokens or 200,000+ tokens) measures the maximum number of tokens it can hold and analyze at one time.

- Play around with Tokenization in the following website: [Tiktokenizer](https://tiktokenizer.vercel.app/)