# Control Flow
# If statements
# Syntax is if condition: then_do_this

age = 15  # assigns 15 to the age variable
if age >= 18:  # checking if the value stored in age is equal to or greater than 18
    # prints out whether they can buy an 18+ movie ticket
    print("You are old enough to watch movies with an age rating of 18!")
elif age >= 15:  # the second if statement runs if the first if condition is not met
    # prints out that they can't buy the ticket
    print("You are not old enough to watch an 18+ movie, but you can watch one with a rating of 15+.")
else:  # if none of the previous conditions are met, this code is run
    print("You can watch movies with an age rating U")

# create a program using control flow with if, elif, and else
# using operators == >=
# check age distrinctions before selling the ticket
# 18, 15, 12, PG, U
# else block should ensure to display message if other conditions are not met

# First we obtain the age rating of the movie they want to see
requested_movie = input("Please enter the age rating of the movie you would like to see:  ")
# And how old the user is
viewer_age = int(input("Please enter your age:  "))

# Then we see if they are old enough to watch that movie
if requested_movie == "18":
    if viewer_age >= 18:  # Checks if the user is 18 or over
        print("You are old enough to watch this movie!")
    else:
        print("Unfortunately you are not old enough to watch this movie")
elif requested_movie == "15":
    if viewer_age >= 15:  # Checks if the user is 15 or over
        print("You are old enough to watch this movie!")
    else:
        print("Unfortunately you are not old enough to watch this movie")
elif requested_movie == "12":  # Checks if the user is 12 or over
    if viewer_age >= 12:
        print("You are old enough to watch this movie!")
    else:
        print("Unfortunately you are not old enough to watch this movie")
elif requested_movie == "PG":
    if viewer_age >= 12:  # Checks if they are older than 12
        print("You are old enough to watch this movie!")
    elif viewer_age < 12:  # Checks if they are younger than 12
        print("You can watch this movie with your parent's permission!")
    else:
        print("Unfortunately you are not old enough to watch this movie")
else:
    print("You can watch this movie!")  # everyone can watch a Universal film
