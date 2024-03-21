contacts = {}

for i in range(2):
    error = "Sorry, you must enter an integer"

    contact_ID = ""
    while not contact_ID:
        try:
            contact_ID = int(input("Enter ID: "))
        except ValueError:
            print(error)
    contacts[contact_ID] = {}

    first_name = input("Enter first name: ")
    contacts[contact_ID]['First name'] = first_name

    last_name = input("Enter last name: ")
    contacts[contact_ID]['Last name'] = last_name

    mobile = ""
    while not mobile:
        try:
            mobile = int(input("Enter mobile number: "))
        except ValueError:
            print(error)
    contacts[contact_ID]['Mobile number'] = mobile

    email = input("Enter email: ")
    contacts[contact_ID]['Email'] = email
    print("\n")

for contacts_id, contact_info in contacts.items():
    print(f"\nContact ID: {contacts_id}")

    for key in contact_info:
        print(f"{key}: {contact_info[key]}")
