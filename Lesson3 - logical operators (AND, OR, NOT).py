while True:
    try:
        # Input for age
        age = int(input("Tell me your age! We will see if you can enter this party.\nYour age buddy: "))

        # Checking if the user is under 12 years old
        if age <= 12:
            print("You cannot enter. We are going to call your parents!")
            print("Police, 122. How can I serve you?")

        else:
            # Input for cash if age is 12 or older
            cash = int(input("Tell me how rich you are (in euros): "))

            # Checking conditions based on age and cash
            if age >= 18 and cash >= 20:
                print("You can enter! You need to pay 20 euros.")
                cash -= 20
                print(f"Your remaining balance is {cash} euros.")

            elif 13 <= age <= 17 and cash >= 25:
                print("You can enter! You need to pay only 15 euros.")
                cash -= 15
                print(f"Your remaining balance is {cash} euros.")

            else:
                print("You cannot enter. Maybe this party is not for you...")

    except ValueError as e:
        print(f"You have entered invalid data! Please try again. Error: {ValueError}{e}")
