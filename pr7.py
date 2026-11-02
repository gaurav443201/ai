# Intelligent Number Guessing Agent
low = 1
high = 100

while True:
    # Agent guesses the middle number
    guess = (low + high) // 2

    print("Agent's Guess:", guess)

    # Get feedback from user
    feedback = input("Enter feedback (higher/lower/correct): ").lower()

    if feedback == "correct":
        print("Agent guessed the number successfully!")
        break

    elif feedback == "higher":
        low = guess + 1

    elif feedback == "lower":
        high = guess - 1

    else:
        print("Invalid feedback! Try again.")