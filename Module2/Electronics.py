""" assignemnt: Chapter2 VAT
    created on 1 nov. 2019
    author: Gaia Liistro """

a = float(raw_input("Enter the price of the first article: "))  #first article price
b = float(raw_input("Enter the price of the second article: ")) #second article price
c = float(raw_input("Enter the price of the third article: "))  #third article price

if (a >= b >= c) or (a >= c >= b):
    most_expensive_article = a
elif (b >= a >= c) or (b >= c >= a):
    most_expensive_article = b
else:
    most_expensive_article = c

discount = most_expensive_article / 100 * 15
total = a + b + c - discount
print "Discount: %.2f" %(discount)
print "Total: %.2f" %(total)
