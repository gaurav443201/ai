
# Simple Banking Chatbot

print("Welcome to ABC Bank Chatbot!")
print("You can ask about balance, deposit, withdraw, or loan.")
print("Type 'bye' to exit.")

balance = 5000

while True:
    user = input("\nYou: ").lower()

    if "hello" in user or "hi" in user:
        print("Bot: Hello! Welcome to ABC Bank.")

    elif "balance" in user:
        print("Bot: Your account balance is Rs.", balance)

    elif "deposit" in user:
        amount = int(input("Enter deposit amount: "))
        balance = balance + amount
        print("Bot: Amount deposited successfully.")
        print("Bot: Current balance is Rs.", balance)

    elif "withdraw" in user:
        amount = int(input("Enter withdrawal amount: "))

        if amount <= balance:
            balance = balance - amount
            print("Bot: Withdrawal successful.")
            print("Bot: Current balance is Rs.", balance)
        else:
            print("Bot: Insufficient balance.")

    elif "loan" in user:
        print("Bot: We provide personal, home and education loans.")

    elif "bye" in user:
        print("Bot: Thank you for using ABC Bank. Goodbye!")
        break

    else:
        print("Bot: Sorry, I don't understand your query.")

