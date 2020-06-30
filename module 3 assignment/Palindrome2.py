""" assignment: Palindrome 2
    created on 8 nov. 2019
    author: Gaia Liistro """


letter = raw_input("Enter a letter: ")

s = " "
for i in range(ord(letter)-97):
    s = s + chr(i + ord("a"))
s = s + letter
for i in range(ord(letter)-97):
    s = s+chr(ord(letter)-1-i)
print s
