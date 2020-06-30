""" assignemnt: Chapter2 VAT
    created on 1 nov. 2019
    author: Gaia Liistro """

black_player = float(int(raw_input("Enter the time the black player thought: "))) #millisecond
white_player = float(int(raw_input("Enter the time the white player thought: "))) #millisecond

if black_player > white_player:
    human_time = black_player
else:
    human_time = white_player

seconds = human_time / 1000
minutes = 0
hours = 0
if seconds >= 60:
    minutes = seconds / 60
    seconds = seconds % 60
if minutes >= 60:
    hours = minutes / 60
    minutes = minutes % 60


print "The time the human player has spent thinking is %02d:%02d:%02d" %(hours, minutes, seconds)