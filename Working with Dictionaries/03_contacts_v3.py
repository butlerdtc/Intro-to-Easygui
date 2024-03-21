import easygui

contacts = {"1": {"First name": "Rafael", "Last name": "Aang",
                  "Mobile": "027 337 8089", "Email": "raf@gmail.com"},
            "2": {"First name": "Alex", "Last name": "Lau",
                  "Mobile": "021 457 7696", "Email": "alex@gmail.com"}
            }

while True:
    all_details = []
    answer = easygui.buttonbox("Would you like to search for a contact or "
                               "print the full list", "Choose",
                               ["Search", "List", "Exit"])

    if answer == "List":
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
            search = easygui.enterbox("Enter name of contact: ",
                                      "Search").title()
            correct = 0
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
