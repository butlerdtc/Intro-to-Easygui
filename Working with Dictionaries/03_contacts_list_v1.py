contacts = {}

for i in range(1):

    error = "\nSorry, you must enter an integer\n"
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

    error = "\nSorry, you must enter an integer\n"
    mobile = ""
    while not mobile:
        try:
            mobile = int(input("Enter mobile number: "))
        except ValueError:
            print(error)
    contacts[contact_ID]['Mobile number'] = mobile

    email = input("Enter email: ")
    contacts[contact_ID]['Email'] = email

print(f"\n{contacts}")
