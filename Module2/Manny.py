""" assignemnt: Chapter2 VAT
    created on 1 nov. 2019
    author: Gaia Liistro """

donation = int(raw_input("Enter the amount you want to donate: ")) #euros

while donation < 50:
    donation = int(raw_input("Enter the amount you want to donate: "))
    if donation > 50:
        print("Thank you for your donation of %.2f euros") %(donation)
