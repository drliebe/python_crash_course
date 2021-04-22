prompt = "Please input your name: "
filename = 'guest_book.txt'

print("Enter 'q' to quit.")
with open(filename, 'w') as file_object:
    while True:
        name = input(prompt)
        if name == 'q':
            break
        else:
            print('Hello ' + name + '!')
            file_object.write(name+'\n')
        
    