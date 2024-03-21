contacts = {"1": {"First name": "Rafael", "Last name": "Aang",
                  "Mobile": "027 337 8089", "Email": "raf@gmail.com"},
            "2": {"First name": "Alex", "Last name": "Lau",
                  "Mobile": "021 457 7696", "Email": "alex@gmail.com"}
            }

while True:
    answer = input("\nWould you like to search for a contact or print the "
                   "full list.\n'Yes' to search or 'No' for the full list or"
                   " 'X' to exit the program: ").lower()
    if answer == "no":
        for contacts_id, contact_info in contacts.items():
            print(f"\nContact ID: {contacts_id}")

            for key in contact_info:
                print(f"{key}: {contact_info[key]}")

    elif answer == "yes":
        while True:
            search = input("Enter name of contact to search for: ").title()
            correct = 0
            for contact_id, contact_info in contacts.items():
                if (contact_info['First name'] == search or
                        contact_info['Last name'] == search):
                    correct += 1
                    print(f"\nContact ID: {contact_id}")

                    for key, value in contact_info.items():
                        print(f"{key}: {value}")
                    break
            if correct > 0:
                break
            else:
                print("This contact is not in the list")
                continue

    elif answer == "x":
        print("Thanks for using this program")
        break

    else:
        print("\nPlease enter 'Yes', 'No' or 'X'")
