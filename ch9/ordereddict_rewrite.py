from collections import OrderedDict

glossary = OrderedDict()

glossary['dictionary'] = 'stores a set of key-value pairs'
glossary['variable'] = 'stores a value'
glossary['list'] = 'stores a series of ordered values'
glossary['set'] = 'stores a set of unique values'
glossary['for loop'] = 'iterates a fixed number of times'
glossary['if statement'] = 'a conditional test that only executes if true'
glossary['and statement'] = 'a way to combine two logical statements'
glossary['or statement'] = 'a second way to combine two logical statements'

for key, value in glossary.items():
    print(str(key) + ' means: ' + str(value))