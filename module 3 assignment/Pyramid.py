""" assignment: Pyramid
    created on 8 nov. 2019
    author: Gaia Liistro """


def pyramid(blank_spaces, letter):
    s = blank_spaces * " "
    for i in range(ord(letter)-97):
        s = s + chr(i + ord("a"))
    s = s + letter
    for i in range(ord(letter)-97):
        s = s + chr(ord(letter)-1-i)
    print s


for i in range(15):
    pyramid(40-i, chr(i + ord("a")))






