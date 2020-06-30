"""assignment: weave1
    created on 24 nov. 2019
    author: Gaia Liistro"""


input = open('weave1input.txt').readlines()
list1 = input[0].split()
list2 = input[1].split()

numbers = []
def add(list, number):
    list.append(number)
    return numbers

x = 0
while x < 10:
    final_serie = add(numbers, list1[x])
    final_serie = add(numbers, list2[x])
    x+=1

print " ".join(final_serie)

