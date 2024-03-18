heroes = {
    "Kob":
        {"Name": "Kobe Bryant",
         "Power": "Helicopter crashing",
         "Strength": "Monkey",
         "Speed": 0
         },

    "Leb": {"Name": "Lebron James",
            "Power": "Banana eater",
            "Strength": 6.9,
            "Speed": 9.6
            }
}
for hero_id, hero_info in heroes.items():
    print(f"\nHero ID: {hero_id}")

    for key in hero_info:
        print(f"{key}: {hero_info[key]}")
