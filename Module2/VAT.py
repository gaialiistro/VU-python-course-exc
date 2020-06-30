""" assignemnt: Chapter2 VAT
    created on 1 nov. 2019
    author: Gaia Liistro """

VAT = 21 # %
price = float(raw_input("Enter the price of the article including VAT: ")) #
price_without_VAT = (price - VAT * price / 100)
print "the article will cost %.2f without VAT" %(price_without_VAT)
