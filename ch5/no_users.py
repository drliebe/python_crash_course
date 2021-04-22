#usernames = ['admin', 'user_a', 'user_b', 'user_c', 'user_d', 'user_e']
usernames = []
if usernames:
    for user in usernames:
        if user == 'admin':
            print('Hello ' + user + ', would you like to see a status' + 
                  ' report?')
        else:
            print('Hello ' + user + ', thank you for logging in again.')
else:
    print('We need to find some users!')
