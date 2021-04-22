my_foods = ['pizza','falalfel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print('My Favorite Foods: ')
for food in my_foods:
    print(food)

print('My Friend\'s Favorite Foods: ')
for food in friend_foods:
    print(food)