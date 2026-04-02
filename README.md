# Chatty Responder

Chatty Responder is a beginner-friendly Python chatbot that runs in the terminal, answers from a local JSON knowledge base, and learns new replies from the user when it does not know what to say.

It is a small project, but it touches several useful Python basics: file handling, JSON, loops, conditionals, and persistent local storage.

## What This Project Does

- Loads question-and-answer pairs from `data/knowledge.json`
- Starts a terminal chat loop and waits for user input
- Matches known inputs and prints saved responses
- Asks the user to teach a response for unknown inputs
- Saves newly learned replies back into the JSON file
- Appends each conversation to `logs/chatlog.txt`
- Exits when the user types `bye` or `exit`

## Why It Is Useful

This project is a good practice build if you want to learn how to:

- read and write JSON files
- store data between program runs
- work with dictionaries in Python
- build a simple interactive CLI app
- handle basic user input and fallback logic

## Project Structure

```text
CHATBOT/
|-- chatty.py
|-- README.md
|-- flowchart.txt
|-- structure.txt
|-- data/
|   `-- knowledge.json
`-- logs/
    `-- chatlog.txt
```

## Requirements

- Python 3

This project uses only Python's built-in modules, so no third-party installation is needed.

## Quick Start

1. Open a terminal in the project folder.
2. Run the chatbot:

```bash
python chatty.py
```

3. Start chatting.
4. If the bot does not know an answer, teach it one.

## How The Chatbot Works

1. The script reads saved responses from `data/knowledge.json`.
2. It asks for input with the prompt `YOU:`.
3. Your message is converted to lowercase before matching.
4. If the message exists in the knowledge base, the saved reply is shown.
5. If the message is unknown, the bot asks you to teach it a response.
6. That new response is saved so the bot can remember it later.
7. The exchange is written to `logs/chatlog.txt`.

## Example Session

```text
YOU: hello
YOUR DAD: Hello! How can I help you today?

YOU: what is your favorite game?
Teach me: What should I reply to that?
Minecraft is fun.
Thanks! I've learned that.

YOU: what is your favorite game?
YOUR DAD: Minecraft is fun.
```

## Data Files

### `data/knowledge.json`

This file stores the chatbot's learned responses as key-value pairs:

```json
{
  "hello": "Hello! How can I help you today?",
  "what is python": "Python is a popular, easy-to-learn programming language."
}
```

### `logs/chatlog.txt`

This file stores the conversation history. Each chat message is appended so you can review past interactions later.

## Current Behavior And Limitations

- Matching is based on exact text, not meaning
- Input is lowercased before checking the knowledge base
- Similar questions with different wording are treated as different inputs
- The chatbot does not use AI, APIs, or internet access
- Knowledge is stored locally, so learning stays on your machine

## Customization Ideas

- Change the bot name shown in `chatty.py`
- Add more starter responses to `data/knowledge.json`
- Split logic into functions for cleaner code
- Add timestamps to `logs/chatlog.txt`
- Improve validation for empty input and file errors
- Add support for fuzzy matching or multiple replies per question

## Learning Value

If you are practicing Python, this project is a nice step between very small exercises and larger applications. It shows how simple code can still feel interactive, useful, and stateful across runs.
