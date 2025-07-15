while True:
    print("\n--- Marriage Eligibility Checker ---")
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    gender = input("Enter your gender (male/female): ").lower()
    if gender == "male":
        if age >= 21:
            print(f"{name}, you are eligible for marriage! 🎉")
        else:
            print(f"{name}, you need to wait {21 - age} more year(s) to get married.")
    elif gender == "female":
        if age >= 18:
            print(f"{name}, you are eligible for marriage! 🎉")
        else:
            print(f"{name}, you need to wait {18 - age} more year(s) to get married.")
    else:
        print("Invalid gender input. Please enter 'male' or 'female'.")
    choice = input("\nDo you want to check again? (yes/no): ").lower()
    if choice != "yes":
        print("Thank you for using the Marriage Calculator!")
        break