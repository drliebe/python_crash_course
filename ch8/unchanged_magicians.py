def show_magicians(magician_list):
    for magician in magician_list:
        print(magician)

def make_great(magician_list):
    updated_magician_list = []
    for magician in magician_list:
        updated_magician = 'The Great ' + magician
        updated_magician_list.append(updated_magician)
    return updated_magician_list


favorite_magicians = ['Copperfield', 'Siegfrid', 'Roy']


great_magicians = make_great(favorite_magicians[:])
show_magicians(great_magicians)
show_magicians(favorite_magicians)