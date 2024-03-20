logins = {"Rafael": "Cars1", "Kavin": "Cars2", "Alex": "Cars3",
          "Nation": "Cars0.5"}

while True:
    info = input("Enter username: ").title()
    if info in logins:
        while True:
            password = input("Please enter your password: ")
            if password in logins[info]:
                print(f"Welcome {info}")
                break
            else:
                print("Please enter a valid password")
                continue
        break
    else:
        print("Please enter a valid username")
        continue
