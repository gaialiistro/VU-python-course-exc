""" assignemnt: Chapter2 VAT
    created on 1 nov. 2019
    author: Gaia Liistro """

TOTAL_SQUARES = 64
white_pieces = float(int(raw_input("Enter the number of white pieces on the board: ")))
black_pieces = float(int(raw_input("Enter the number of black pieces on the board: ")))

percentage_black_pieces = ( black_pieces / TOTAL_SQUARES * 100 )
relative_percentage_black_pieces = (black_pieces / (white_pieces + black_pieces) * 100)

print "the percentage of black pieces is: %.2f%% " %(percentage_black_pieces)
print "the percentage of black pieces of all the pieces in the board is: %.2f%% " %(relative_percentage_black_pieces)