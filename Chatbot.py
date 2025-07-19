import re
from datetime import datetime


def match_pattern(user_input, user_name):
    user_input = user_input.lower()

    if re.search(r"\bhi\b|\bhello\b", user_input):
        if user_name:
            return f"hello {user_name}! how can i assist you today?"
        else:
            return "hello there! may i know your name?"

    elif re.search(r"my name is (.+)", user_input):
        name = re.search(r"my name is (.+)", user_input).group(1).strip()
        return f"nice to meet you, {name}!", name

    elif re.search(r"what(?:'s| is) the time", user_input):
        current_time = datetime.now().strftime("%I:%M %p").lower()
        return f"it's currently {current_time}."

    elif re.search(r"what(?:'s| is) the date", user_input):
        current_date = datetime.now().strftime("%d %b %Y").lower()
        return f"today's date is {current_date}."

    elif "name" in user_input and not user_name:
        return "i don't know your name yet. please tell me by saying 'my name is ___'."

    elif re.search(r"do you know my name", user_input) and user_name:
        return f"your name is {user_name}, my current user."

    elif re.search(r"can you introduce yourself", user_input):
        return "i am cypher, your simple rule-based assistant."

    elif re.search(r"what can you do", user_input):
        return "i can chat with you, remember your name, tell time/date, and respond to basic queries."

    elif re.search(r"how are you", user_input):
        return "i am doing well! hope you're having a good time too."

    elif re.search(r"thank you|thanks", user_input):
        return "you're welcome!"

    elif re.search(r"bye for now|exit|quit", user_input):
        return "goodbye! have a great time."

    else:
        return "sorry, i didn't understand that."


# Export chatbot runner (optional CLI version)
def run_cli_chatbot():
    print("🤖 cypher: hello! type 'bye for now' to exit.")
    user_name = None

    while True:
        user_input = input("you: ").lower()

        if re.search(r"my name is (.+)", user_input):
            name = re.search(r"my name is (.+)", user_input).group(1).strip()
            user_name = name
            print(f"cypher: nice to meet you, {user_name}!")
            continue

        response = match_pattern(user_input, user_name)
        if isinstance(response, tuple):
            response, user_name = response

        print(f"cypher: {response}")

        if "bye for now" in user_input or "exit" in user_input:
            break


if __name__ == "__main__":
    run_cli_chatbot()
