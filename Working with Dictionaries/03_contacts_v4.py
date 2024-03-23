import easygui


# Formats the inputted phone number to a 000 000 0000 order
def phone_formatter(number):
    formatted_number = '{:010}'.format(number)
    return (f'{formatted_number[:3]} {formatted_number[3:6]} '
            f'{formatted_number[6:]}')


def add_contact():
    while True:
        new_id = easygui.integerbox("Enter new contacts ID: ",
                                    "New ID", upperbound=300)
        string_new_id = f"{new_id}"
        if string_new_id in contacts:
            easygui.msgbox("This ID is already assigned to a contact\n"
                           "Please enter a new ID")
            continue
        else:
            contacts[string_new_id] = {}
            break

    first_name = easygui.enterbox("Enter first name: ",
                                  "First Name")
    contacts[string_new_id]['First name'] = first_name.title()

    last_name = easygui.enterbox("Enter last name: ",
                                 "Last Name")
    contacts[string_new_id]['Last name'] = last_name.title()

    while True:
        count_1 = 0
        mobile = easygui.integerbox("Enter mobile number\nMust be 10 "
                                    "digits or less and with no spaces: ",
                                    "Mobile Number",
                                    upperbound=100000000000000)
        string_mobile = phone_formatter(mobile)
        for contact in contacts.values():
            if 'Mobile' in contact and string_mobile == contact['Mobile']:
                easygui.msgbox("Another contact already has this number",
                               "Mobile number in use")
                count_1 += 1
                break
        if count_1 > 0:
            continue
        else:
            contacts[string_new_id]['Mobile'] = string_mobile
            break

    while True:
        count_2 = 0
        email = easygui.enterbox("Enter email address: ",
                                 "Email Address")
        for contact in contacts.values():
            if 'Email' in contact and email == contact['Email']:
                easygui.msgbox("Another contact already has this email",
                               "Email in use")
                count_2 += 1
                break
        if count_2 > 0:
            continue
        else:
            contacts[string_new_id]['Email'] = email
            break


def print_list():
    for contacts_id, contacts_info in contacts.items():
        all_details.append(f"\nContact ID: {contacts_id}\n")

        for key_1 in contacts_info:
            all_details.append("- " + f"{key_1}: {contacts_info[key_1]}\n")
        if contacts_id != "1":
            all_details.append("\n")

    details = "".join(all_details)
    easygui.msgbox(f"{details}", "Full list")


def search_list():
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


def main_program():
    while True:
        all_details = []
        answer = easygui.buttonbox("Would you like to search for a contact, "
                                   "print the full list or add a contact",
                                   "Choose", ["Search", "List", "Add",
                                              "Exit"])
        if answer == "Add":
            add_contact()

        elif answer == "List":
            print_list()

        elif answer == "Search":
            search_list()

        else:
            easygui.msgbox("Thanks for using this program", "Thank you")
            break


# Main routine
contacts = {"1": {"First name": "Rafael", "Last name": "Aang",
                  "Mobile": "027 337 8089", "Email": "raf@gmail.com"},
            "2": {"First name": "Alex", "Last name": "Lau",
                  "Mobile": "021 457 7696", "Email": "alex@gmail.com"}
            }

main_program()
