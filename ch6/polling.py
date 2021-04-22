favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " 
          + language.title() + ".")

people_polled = ['edward', 'ted', 'bill', 'sarah']

for person in people_polled:
    if person in favorite_languages.keys():
        print('Thank you for taking the poll!')
    else:
        print('Please take the poll.')
        