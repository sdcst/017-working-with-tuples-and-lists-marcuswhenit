#!python3

"""
Create a variable that contains an empty list.
Ask a user to enter 5 words.  Add the words into the list.
Print the list
inputs:
string 
string
string
string
string

outputs:
string

example:
Enter a word: apple
Enter a word: worm
Enter a word: dollar
Enter a word: shingle
Enter a word: virus

['apple', 'worm', 'dollar', 'shingle', 'virus']
"""
mylist = []

for i in range(5):
    x = input("Enter a word > ")
    mylist.append(x)

print(mylist)

        