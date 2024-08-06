import random

def ask():
    while True:
        try:
            user = int(input("Choose:\n0 for 'snake'\n1 for 'water'\n2 for 'gun': "))
            if user not in [0, 1, 2]:
                print("Please enter a valid number (0, 1, or 2).")
            else:
                break  # Exit loop if input is valid
        except ValueError:
            print("Invalid input. Please enter a number.")

    comp = random.randint(0, 2)
    if comp == 0:
        print("Computer chose 'snake'")
    elif comp == 1:
        print("Computer chose 'water'")
    elif comp == 2:
        print("Computer chose 'gun'")

    return user, comp

def check(user, comp):
    if user == comp:
        return 0
    elif (user == 0 and comp == 2) or (user == 2 and comp == 1) or (user == 1 and comp == 0):
        return -1
    else:
        return 1

while True:
    user, comp = ask()
    final = check(user, comp)

    if final == 0:
        print("Draw")
    elif final == 1:
        print("You win")
    elif final == -1:
        print("You lose")

    review = input("Do you want to play again? (yes/no): ").strip().lower()
    if review != "yes":
        print("\nTHANKS FOR PLAYING")
        break
