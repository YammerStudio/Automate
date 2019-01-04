
'''
Rules:
if number is even, divide it by two
if number is odd, triiple it and add one

'''

num = int(input('Enter in a num: '))
while num != 1:
    if(num % 2 == 0):
        num = num / 2
        print(str(num))
    else:
        num = (num * 3) + 1
        print(str(num))
