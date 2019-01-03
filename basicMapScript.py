import webbrowser 

fromAddress = str(input('Enter in from address: '))
toAddress = str(input('Enter in to address: '))

webbrowser.open('https://www.google.com/maps/dir/' + fromAddress + '/' + toAddress, new = 2)

'''

'''
