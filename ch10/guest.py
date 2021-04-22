prompt = "Please input your name: "
name = input(prompt)
filename = 'guest.txt'
with open(filename, 'w') as file_object:
    file_object.write(name)
    