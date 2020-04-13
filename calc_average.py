#based off calculate sum code found here
#https://medium.com/programminginpython-com/python-program-to-calculate-the-sum-of-elements-in-a-list-ed2b80db8268

lst = []
num = int(input('How many numbers: '))
for n in range(num):
    numbers = int(input('Enter number '))
    lst.append(numbers)
#print("Sum of elements in given list is :", sum(lst))
print("The average of the numbers is:", sum(lst) / num)
