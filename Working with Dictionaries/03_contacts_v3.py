import easygui

contacts = {"1": {"First name": "Rafael", "Last name": "Aang",
                  "Mobile": "027 337 8089", "Email": "raf@gmail.com"},
            "2": {"First name": "Alex", "Last name": "Lau",
                  "Mobile": "021 457 7696", "Email": "alex@gmail.com"}
            }

while True:
    all_details = []
    answer = easygui.buttonbox("Would you like to search for a contact, "
                               "print the full list or add a contact",
                               "Choose", ["Search", "List", "Add",
                                          "Exit"])
    if answer == "Add":
        while True:
            new_ID = easygui.integerbox("Enter new contacts ID: ",
                                        "New ID")
            if new_ID in contacts:
                easygui.msgbox("This ID is already assigned to a contact\n"
                               "Please enter a new ID")
                continue
            else:
                contacts[new_ID] = {}
                break

        first_name = easygui.enterbox("Enter first name: ",
                                      "First Name")
        contacts[new_ID]['First name'] = first_name

        last_name = easygui.enterbox("Enter last name: ",
                                     "Last Name")
        contacts[new_ID]['Last name'] = last_name

        while True:
            mobile = easygui.integerbox("Enter mobile number: ",
                                        "Mobile Number")
            if mobile in contacts:
                easygui.msgbox("Another contact already has this number")
                continue
            else:
                contacts[new_ID]['Mobile'] = mobile
                break

        while True:
            email = easygui.enterbox("Enter email address: ",
                                     "Email Address")
            if email in contacts:
                easygui.msgbox("Another contact already has this email")
                continue
            else:
                contacts[new_ID]['Email'] = email
                break

    elif answer == "List":
        for contacts_id, contact_info in contacts.items():
            all_details.append(f"\nContact ID: {contacts_id}\n")

            for key in contact_info:
                all_details.append("- " + f"{key}: {contact_info[key]}\n")
            if contacts_id != "1":
                all_details.append("\n")

        details = "".join(all_details)
        easygui.msgbox(f"{details}", "Full list")
    elif answer == "Search":
        while True:
            contact_details = []
            correct = 0
            search = easygui.enterbox("Enter name of contact: ",
                                      "Search").title()

            for contact_id, contact_info in contacts.items():
                if (contact_info['First name'] == search or
                        contact_info['Last name'] == search):
                    correct += 1
                    contact_details.append(f"\nContact ID: {contact_id}\n")

                    for key, value in contact_info.items():
                        contact_details.append("- " + f"{key}: {value}\n")
                    break

            if correct > 0:
                clean_details = "".join(contact_details)
                easygui.msgbox(f"{clean_details}", f"{search} details")
                break

            else:
                easygui.msgbox("This contact is not in the list",
                               "Contact Not found")
                continue

    else:
        easygui.msgbox("Thanks for using this program", "Thank you")
        break
