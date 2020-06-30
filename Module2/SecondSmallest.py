""" assignemnt: Chapter2 VAT
    created on 6 nov. 2019
    author: Gaia Liistro """

integers = (raw_input("Enter numbers: "))
list_integers = map(int, integers.split())

#delete the smallest integer
y = 0
smallest_integer = list_integers[0]
length = len(list_integers)
while y < length:
    if smallest_integer > list_integers[y]:
        smallest_integer = list_integers[y]
    y += 1
list_integers.remove(smallest_integer)

#print the second smallest integer
second_smaller = list_integers[0]
length = len(list_integers)
x=0
while x < length:
    if second_smaller > list_integers[x]:
        second_smaller = list_integers[x]
    x += 1
print "The second smallest number is: " + str(second_smaller)



