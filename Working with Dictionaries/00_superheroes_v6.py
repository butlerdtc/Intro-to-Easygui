heroes = {}

for i in range(2):
    hero_ID = input("\nEnter ID: ")
    heroes[hero_ID] = {}

    name = input("Enter name: ")
    heroes[hero_ID]['Name'] = name

    power = input("Enter power: ")
    heroes[hero_ID]['Power'] = power

    strength = input("Enter strength value: ")
    heroes[hero_ID]['Strength'] = strength

    speed = input("Enter speed: ")
    heroes[hero_ID]['Speed'] = speed

print(f"\n{heroes}")
