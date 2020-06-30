""" assignemnt: Chapter2 VAT
    created on 3 nov. 2019
    author: Gaia Liistro """


n = int(raw_input("Enter a number: "))
s = ""
while n != 1:
    if (n%2) == 0:
        n = n/2
    else:
        n = 3*n + 1
    print n,
