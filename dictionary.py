# Create a dictionary
my_dict = {'key1': 'value', 'key2': 'value2', 'key3': 'value3'}
print(my_dict)

print(my_dict['key1'])

my_dict['key4'] = 'value4'
print(my_dict)

my_dict['key1'] = 'new_value1'
print(my_dict)

# ITERATING THROUGH DICTIONARIES 
# 1. Using .items() method. It returns a list key-value pairs.
d = {'a': 1, 'b': 2, 'c':3}
for key, value in d.items():
    print(key, value)

# 2. Using .keys() method. The keys() method return a list of keys in the dictionary. 
d = {'a': 1, 'b':2, 'c':3}
for key in d.keys():
    print(key, d[key])
