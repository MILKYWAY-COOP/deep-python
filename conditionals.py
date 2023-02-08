isWednesday = True

if isWednesday == True:
    print('Today is Wednesday')
elif isWednesday == False:
    print('Today is not Wednesday')

data = [1,2,3,4,15,6,7,8,9]
j = 0
while j < len(data):
    j = j + 1
    print('The value of j is', j)

for i in data:
    if i % 2 == 0:
        print('Even numbers', i)

for i in data:
    if i % 2 == 1:
        print('Odd numbers', i)

biggest = data[0]
for val in data: 
    if val > biggest:
        biggest = val

print(biggest)

# Break and Continue Statements
myArray = [1, 2, 3, 4, 5, False, 10]
found = 10
for item in myArray:
    if item == found:
        print(myArray.index(item))
        break

for num in range(0, 10):
    if num % 2 == 0:
        print(f"{num} is an even number.")
        continue
    elif num == 7: 
        print(f"{num} is my break number.")
        break
    print(f'{num} is an odd number')