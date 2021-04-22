current_users = ['admin', 'user_a', 'user_b', 'user_c', 
                 'user_d', 'user_e']
new_users = ['user_f', 'user_g', 'user_b', 'user_i', 'user_e']

for new_user in new_users:
    if new_user.lower() in current_users:
        print('Apologies, but the username: ' + new_user 
            + ' is already in use.')
    else:
        print('Congratulations, that username is available.')
