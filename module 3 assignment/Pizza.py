"""assignment: Pizza
    created on 8 nov. 2019
    author: Gaia Liistro"""


def factorial(x):
    a = int(x)
    while (int(x)) > 1 :
        a = a * int(x-1)
        x -= 1
    return a


def number_of_pizzas(n,k):
    return factorial(n) / (factorial(k) * factorial(n - k))


luigi = number_of_pizzas(9, 4)
mario = number_of_pizzas(10, 3)

print "Luigi can make %d pizzas" % luigi
print "Mario can make %d pizzas" % mario

if luigi < mario:
    print "Mario has won the bet."
else:
    print "Luigi has won the bet."
