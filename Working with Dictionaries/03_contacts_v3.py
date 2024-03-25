"""Program that keeps a dictionary of contacts and the user can choose to read
the list, search for a specific entry or add a new entry
Updated version of version 2
Created by Robson Butler - 23/03/24"""

import easygui


# Formats the inputted phone number to a 000 000 0000 order
def phone_formatter(number):
    formatted_number = '{:010}'.format(number)
    return (f'{formatted_number[:3]} {formatted_number[3:6]} '
            f'{formatted_number[6:]}')


# Dictionary of existing contacts and for new contacts
contacts = {"1": {"First name": "Rafael", "Last name": "Aang",
                  "Mobile": "027 337 8089", "Email": "raf@gmail.com"},
            "2": {"First name": "Alex", "Last name": "Lau",
                  "Mobile": "021 457 7696", "Email": "alex@gmail.com"}
            }

# Loops the whole program until user decides to exit
while True:
    # List to add dictionary entries to, so they all can be printed at once
    all_details = []
    # Asks user what they want to choose
    answer = easygui.buttonbox("Would you like to search for a contact, "
                               "print the full list or add a contact",
                               "Choose", ["Search", "List", "Add",
                                          "Exit"])
    if answer == "Add":
        # Loops to check if contact ID is already in use
        while True:
            new_ID = easygui.integerbox("Enter new contacts ID: ",
                                        "New ID", upperbound=300)
            # Converts new_ID from an integer to a string
            string_new_id = f"{new_ID}"
            if string_new_id in contacts:
                easygui.msgbox("This ID is already assigned to a contact\n"
                               "Please enter a new ID")
                continue
            else:
                # Adds new ID number as a nested dictionary in contacts
                contacts[string_new_id] = {}
                break

        first_name = easygui.enterbox("Enter first name: ",
                                      "First Name")
        # Adds new contact first name to dictionary
        contacts[string_new_id]['First name'] = first_name.title()

        last_name = easygui.enterbox("Enter last name: ",
                                     "Last Name")
        # Adds new contact last name to dictionary
        contacts[string_new_id]['Last name'] = last_name.title()

        while True:
            # Variable to record if number checker is used so loop can be
            # continued if it is used
            count_1 = 0
            mobile = easygui.integerbox("Enter mobile number\nMust be 10 "
                                        "digits or less and with no spaces: ",
                                        "Mobile Number",
                                        upperbound=100000000000000)
            # Uses phone_formatter function to convert number to mobile number
            # format of '000 000 0000'
            string_mobile = phone_formatter(mobile)
            for contact in contacts.values():
                # Checks if number is already in dictionary
                if 'Mobile' in contact and string_mobile == contact['Mobile']:
                    easygui.msgbox("Another contact already has this number",
                                   "Mobile number in use")
                    count_1 += 1
                    break
            if count_1 > 0:
                continue
            else:
                # Adds new contact mobile number to dictionary
                contacts[string_new_id]['Mobile'] = string_mobile
                break

        while True:
            # Variable to record if number checker is used so loop can be
            # continued if it is used
            count_2 = 0
            email = easygui.enterbox("Enter email address: ",
                                     "Email Address")
            for contact in contacts.values():
                # Checks if email address is already in dictionary
                if 'Email' in contact and email == contact['Email']:
                    easygui.msgbox("Another contact already has this email",
                                   "Email in use")
                    count_2 += 1
                    break
            if count_2 > 0:
                continue
            else:
                # Adds new contact email address to dictionary
                contacts[string_new_id]['Email'] = email
                break

    elif answer == "List":
        # For loop to go through each entry in dictionary
        for contacts_id, contact_info in contacts.items():
            # Appends each contact ID to a list
            all_details.append(f"\nContact ID: {contacts_id}\n")

            for key in contact_info:
                # Appends each value in each nested dictionary with its key to
                # a list
                all_details.append("- " + f"{key}: {contact_info[key]}\n")
            if contacts_id != "1":
                # Appends an empty line between each contact
                all_details.append("\n")

        # Makes the list all_details more aesthetically pleasing
        details = "".join(all_details)
        easygui.msgbox(f"{details}", "Full list")
    elif answer == "Search":
        while True:
            # Empty list to store searched ID's values
            contact_details = []
            # Variable to store if name searched is in contacts
            correct = 0
            search = easygui.enterbox("Enter name of contact: ",
                                      "Search").title()

            # Checks through each ID in contacts
            for contact_id, contact_info in contacts.items():
                # If searched name is in any of the nested dictionaries
                if (contact_info['First name'] == search or
                        contact_info['Last name'] == search):
                    # Adds 1 to variable storing use of loop
                    correct += 1
                    # Appends searched contacts ID to list
                    contact_details.append(f"\nContact ID: {contact_id}\n")

                    # Appends dictionary values of searched contact to list
                    for key, value in contact_info.items():
                        contact_details.append("- " + f"{key}: {value}\n")
                    break

            # If name has been found in dictionary runs this statement
            if correct > 0:
                # Makes the contact details more aesthetically pleasing
                clean_details = "".join(contact_details)
                # Outputs searched contacts details
                easygui.msgbox(f"{clean_details}", f"{search} details")
                break

            else:
                # Outputs that contact is not in dictionary and loop continues
                easygui.msgbox("This contact is not in the list",
                               "Contact Not found")
                continue

    else:
        # Thank you message to the user and ends the program
        easygui.msgbox("Thanks for using this program", "Thank you")
        break
