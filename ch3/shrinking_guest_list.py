guests = ['jesus', 'muhammad', 'buddha']
print('Hello ' + guests[0].title() + ", would you like to come to dinner?")
print('Hello ' + guests[1].title() + ", would you like to come to dinner?")
print('Hello ' + guests[2].title() + ", would you like to come to dinner?")
print('I just found a larger table for dinner!')

guests.insert(0,'Larry')
guests.insert(2, 'Curly')
guests.append('Moe')

print('Hello ' + guests[0].title() + ", would you like to come to dinner?")
print('Hello ' + guests[1].title() + ", would you like to come to dinner?")
print('Hello ' + guests[2].title() + ", would you like to come to dinner?")
print('Hello ' + guests[3].title() + ", would you like to come to dinner?")
print('Hello ' + guests[4].title() + ", would you like to come to dinner?")
print('Hello ' + guests[5].title() + ", would you like to come to dinner?")

print('My apologies, but the table will not arrive in time. I can only host two guests.')
print('My apologies ' + guests.pop() + ". Can we reschedule?")
print('My apologies ' + guests.pop() + ". Can we reschedule?")
print('My apologies ' + guests.pop() + ". Can we reschedule?")
print('My apologies ' + guests.pop() + ". Can we reschedule?")

print(guests[0].title() + " can you still come?")
print(guests[1].title() + " can you still come?")
del(guests[1])
del(guests[0])
print(guests)