print("Welcome to Banking Chatbot!")

balance = 5000

while True:
    print("\n1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Loan Information")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Your balance is:", balance)

    elif choice == "2":
        amount = int(input("Enter deposit amount: "))
        balance = balance + amount
        print("Money deposited successfully!")
        print("Updated balance:", balance)

    elif choice == "3":
        amount = int(input("Enter withdrawal amount: "))

        if amount <= balance:
            balance = balance - amount
            print("Money withdrawn successfully!")
            print("Updated balance:", balance)
        else:
            print("Insufficient balance!")

    elif choice == "4":
        print("We provide personal, home and education loans.")

    elif choice == "5":
        print("Thank you for using our chatbot!")
        break

    else:
        print("Invalid choice! Please try again.")