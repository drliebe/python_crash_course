import matplotlib.pyplot as plt

input = range(1,5001)
first_five = [x**3 for x in input[:5]]
remaining = [x**3 for x in input[5:]]

plt.scatter(input[:5], first_five, c=first_five, cmap=plt.cm.Blues, s=20)
plt.scatter(input[5:], remaining, c=remaining, cmap=plt.cm.inferno, s=20)
plt.title('Cubes')
plt.xlabel('Input Value')
plt.ylabel('Cube of Input Value')

plt.show()