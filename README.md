# Cypher – A Simple Rule-Based Chatbot 🤖

Cypher is a lightweight rule-based chatbot built in Python using basic pattern matching. It's designed for beginners to understand how simple text interactions work without the need for AI or NLP libraries.

## 💬 Features

- Responds to greetings like "hi", "hello"
- Learns and remembers your name during a session
- Can tell you what it can do
- Introduces itself
- Simple farewell response
- Entire conversation in lowercase (stylistic choice)

## 🧠 How It Works

The chatbot uses Python's `re` (regular expression) module to identify patterns in user input and generate fixed responses based on predefined rules.

Example interaction:
cypher: hello! type 'bye for now' to exit.
you: hi
cypher: hello there! may i know your name?
you: my name is akash
cypher: nice to meet you, akash!
you: do you know my name ?
cypher: your name is akash, my current user.
you: bye for now
cypher: goodbye! have a great time.



## 🚀 Getting Started

### Requirements
- Python 3.x

### Running the Bot
Clone the repository and run the script:

```bash
git clone https://github.com/your-username/cypher-chatbot.git
cd cypher-chatbot
python chatbot.py


cypher-chatbot/
├── chatbot.py       # Main Python script
└── README.md        # Project documentation
