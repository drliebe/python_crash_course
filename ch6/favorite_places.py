favorite_places = {
    'Josh': ['LA', 'Grand Canyon', 'Florida'],
    'Jerry': ["Grandpa's farm", 'Chicago'],
    'Joe': ['Colorado', 'Alaska'],
}

for name, places in favorite_places.items():
    print(name + "'s favorite places are:")
    for place in places:
        print("  " + place)