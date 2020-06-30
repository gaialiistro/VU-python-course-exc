""" assignment: Palindrome 1
    created on 8 nov. 2019
    author: Gaia Liistro """

s = " "
for i in range(25):
    s = s + chr(i + ord("a"))
s = s + "z"
for i in range(25):
    s = s + chr(ord("y")-i)
print s
