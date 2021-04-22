person = {'first_name': 'Josh', 'last_name': 'Love', 'age': 37, 
          'city': 'Union City'}
for key, value in person.items():
    print(key + ': ' + str(value))

print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])