# Defining functions

# The standard convention for Python functions is to have at least two
#   blank lines between function definitions.

# A simple function that centers the text "Spam and eggs" on an 200
#   character wide screen.
def python_food():
    width = 200
    text = "Spam and eggs"
    # Remember that // is integer division
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)


# A simple function that centers a given input on an 200 character wide screen.
def center_text(text_in):
    text_in = str(text_in)
    left_margin = (200 - len(text_in)) // 2
    print(" " * left_margin, text_in)
########################################################################################################################################################################################################
#####                                                                A few lines from the beginning of Monty Python and the Holy Grail                                                             #####
########################################################################################################################################################################################################
mphg_line_1 = "You're using coconuts!"
mphg_line_2 = "What?"
mphg_line_3 = "You've got two empty halves of coconut and you're bangin' 'em together."
mphg_line_4 = "So? We have ridden since the snows of winter covered this land, through the kingdom of Mercia, through..."
mphg_line_5 = "Where'd you get the coconuts?"
mphg_line_6 = "We found them."
mphg_line_7 = "Found them? In Mercia?! The coconut's tropical!"
mphg_line_8 = "What do you mean?"
mphg_line_9 = "Well, this is a temperate zone."
mphg_line_10 = "The swallow may fly south with the sun or the house martin or the plover may seek warmer climes in winter, yet these are not strangers to our land?"
mphg_line_11 = "Are you suggesting that coconuts migrate?"
########################################################################################################################################################################################################
########################################################################################################################################################################################################


# Calling Functions
python_food()
center_text("#" * 200)
center_text(mphg_line_1)
center_text(mphg_line_2)
center_text(mphg_line_3)
center_text(mphg_line_4)
center_text(mphg_line_5)
center_text(mphg_line_6)
center_text(mphg_line_7)
center_text(mphg_line_8)
center_text(mphg_line_9)
center_text(mphg_line_10)
center_text(mphg_line_11)
center_text("#" * 200)

# You can also allow a function to take a variable number of arguments using *variable_name
def center_text_2(*text_in):
    text_out = ""
    for arg in text_in:
        text_out += str(arg) + " "
    left_margin = (200 - len(text_in)) // 2
    print(" " * left_margin, text_out)


center_text_2("Spam", "+", "eggs", "=", 42)
center_text_2(5,10,15,20,25,30)

# Creating a function that returns a value.
def center_text_3(*text_in):
    text_out = ""
    for arg in text_in:
        text_out += str(arg) + " "
    left_margin = (200 - len(text_in)) // 2
    return " " * left_margin + text_out

new_var = center_text_3("Spam", "+", "eggs", "=", 42)
print(new_var)
