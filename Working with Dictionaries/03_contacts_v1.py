contacts = {"1": {"First name": "Rafael", "Last name": "Aang",
                  "Mobile": "027 337 8089", "Email": "raf@gmail.com"},
            "2": {"First name": "Alex", "Last name": "Lau",
                  "Mobile": "021 457 7696", "Email": "alex@gmail.com"}
            }

for contacts_id, contact_info in contacts.items():
    print(f"\nContact ID: {contacts_id}")

    for key in contact_info:
        print(f"{key}: {contact_info[key]}")
