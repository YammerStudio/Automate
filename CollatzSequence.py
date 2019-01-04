
'''
Rules:
if number is even, divide it by two
if number is odd, triiple it and add one


'''
def collatz(num):
    if(num % 2 == 0):
        print(int(num/2))
        return int(num/2)
    else:
       print(int(num * 3 + 1))
       return int(num*3 + 1)


print('Please enter a number and the Collatz sequence will be printed!')
try:
    x = int(input())
except ValueError:
    print('Error: Invalid Value, only integer man')

while  x != 1:
    x = collatz(x)
