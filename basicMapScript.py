#! python3

# mapIt.py - launches a map in the browser using an address from the command line or clipboard

import webbrowser, sys, pyperclip
'''
if len(sys.argv) > 1 :
    #get address from command line:

    address = ' '.join(sys.argv[1:])

else:
    #get address from clipboard
    address = pyperclip.paste()
'''#
fromAddress = str(input('Enter in from address: '))
toAddress = str(input('Enter in to address: '))


#now open
'''
default new = 0, opens in same page
new = 2, opens in new tab

'''
#webbrowser.open('https://www.google.com/maps/dir/' +  fromAddress + '/' + toAddress, new = 2)

url = 'https://docs.python.org/3/library/'

#open url in a new tab, if browser already open
#webbrowser.open_new_tab(url)

#open url in new window, raising the window if possible
webbrowser.open_new(url)

webbrowser.get()
