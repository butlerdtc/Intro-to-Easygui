hero_0 = {
    "Name": "Kobe Bryant",
    "Power": "Helicopter crashing",
    "Strength": "monkey",
    "Speed": 0
}

hero_1 = {
    "Name": "Lebron James",
    "Power": "banana eater",
    "Strength": 6.9,
    "Speed": 9.6
}
hero_list = [hero_0, hero_1]

for i in hero_list:
    print(f"{i['Name']}'s superpower is {i['Power']} and their strength value "
          f"is {i['Strength']} with a speed of {i['Speed']}")
