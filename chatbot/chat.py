# CONSOLE CHATBOT

def chatbot():
    print("******** WELCOME TO PYTHON CHATBOT ********")
    print("Type 'bye' to end the conversation.")

    responses = {
        "hello": "Hello! How are you?",
        "hi": "Hi there! Nice to meet you.",
        "how are you": "I'm doing great! Thanks for asking.",
        "name": "I'm a Python console chatbot.",
        "python": "Python is a popular programming language.",
        "help": "Sure! How can I help you?",
        "bye": "Goodbye! Have a nice day!"
    }

    conversation = []

    while True:
        user_input = input("You: ").lower()

        conversation.append({
            "role": "user",
            "content": user_input
        })

        if user_input == "bye":
            reply = responses["bye"]
            print("Bot:", reply)

            conversation.append({
                "role": "assistant",
                "content": reply
            })
            break

        reply = "Sorry, I don't understand that."

        for keyword in responses:
            if keyword in user_input:
                reply = responses[keyword]
                break

        print("Bot:", reply)

        conversation.append({
            "role": "assistant",
            "content": reply
        })

    print("\n******** CONVERSATION HISTORY ********")
    for message in conversation:
        print(message)


# STUDENT MARKS ANALYZER

def analyze_marks(marks):
    average = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)

    return average, highest, lowest


def main():
    chatbot()

    print("\n******** STUDENT MARKS ANALYZER ********")

    marks = []

    n = int(input("Enter the number of students: "))

    for i in range(n):
        mark = float(input(f"Enter mark of student {i+1}: "))
        marks.append(mark)

    average, highest, lowest = analyze_marks(marks)

    print("\n******** MARKS REPORT ********")
    print("Average Marks:", average)
    print("Highest Marks:", highest)
    print("Lowest Marks:", lowest)


main()