def count(data, target):
    n = 0
    for item in data:
        if item == target:
            n = data.index(item)
    return n


print(count([1, 2, 3, 4, 5, 6, 7, 8], 4))

# Simple Input and  Output
print('maroon', 5)
year = int(input('Enter a year: '))
print('The input year is: ' + str(year))

xNy = input('Enter x and y, separated by a comma RESPECTIVELY: ')
pieces = xNy.split(',')
print('x = ', float(pieces[0]))
print('y = ', float(pieces[1]))

# Sample Input and Output Program
age = int(input('Enter your age in years: '))
# as per Med Sci Sports Exerc. 2007;39(8):1423-32
max_heart_rate = 206.9 - (0.67 * age)
target = 0.65 * max_heart_rate
print('Your target heart rate is: ' + str(target))

# FILES
with open('sample.txt', 'r') as file:  # 'r' is for read mode
    content = file.read()
    print(content)

with open('sample.txt', 'w') as file:  # 'w' is for write mode
    # This will overwrite the existing content
    file.write('This is a sample text file')


names = ['John', 'Mary', 'Bob', 'Mosh', 'Sarah', 'Marry']
with open('sample.txt', 'a') as file:  # 'a' is for append mode
    # This will append the content to the existing content
    for i in names:
        file.write(i + '\n')

# EXCEPTION HANDLING
def sqrt(x):
    if not isinstance(x, (int, float)): # isinstance() is a built-in function that checks if an object is an instance of a class
        raise TypeError('x must be numeric')
    elif x < 0:
        raise ValueError('x cannot be negative')

sqrt('a') # This will raise a TypeError
sqrt(-1) # This will raise a ValueError

try:
    fp = open('sawmple.txt')
except IOError as e:
    print('Unable to open the file. Check if it exists.')
else:
    print('File found')
    fp.close()

age = -1 
while age <= 0:
    try:
        age = int(input('Enter your age: '))
        if age <= 0:
            print('Age must be positive')
    except ValueError:
        print('That is an invalid age specification. Try again...')
    except EOFError:
        print('Why did you do an EOF on me?')
        raise # This will raise the exception again

def factors(n):
    results = []
    for k in range(1, n+1):
        if n % k == 0:
            results.append(k)
    return results

print(factors(131))

def factors(n): # generator version
    for k in range(1, n+1): 
        if n % k == 0: # divides evenly, thus k is a factor
            yield k # yield k to the caller

factors = factors(131)
print(factors)