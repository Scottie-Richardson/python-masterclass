# Write a GUI program to create a simple calculator
# layout that looks like the screenshot.
#
# Try to be as Pythonic as possible - it's ok if you
# end up writing repeated Button and Grid statements,
# but consider using lists and a for loop.
#
# There is no need to store the buttons in variables.
#
# As an optional extra, refer to the documentation to
# work out how to use minsize() to prevent your window
# from being shrunk so that the widgets vanish from view.
#
# Hint: You may want to use the widgets .winfo_height() and
# winfo_width() methods, in which case you should know that
# they will not return the correct results unless the window
# has been forced to draw the widgets by calling its .update()
# method first.
#
# If you are using Windows you will probably find that the
# width is already constrained and can't be resized too small.
# The height will still need to be constrained, though.

try:
    import tkinter
except ImportError: # Python 2
    import Tkinter as tkinter

main_window = tkinter.Tk()
main_window_padding = 10

main_window.title('tkinter GUI Challange')
main_window.geometry('640x480-4-8')
# Add space between the edge of the main window and other widgets
main_window['padx'] = main_window_padding

# Create and configure frame for calculator keys
key_pad_frame = tkinter.Frame(main_window)
key_pad_frame.grid(row=1, column=0, sticky='nsew')
key_pad_frame.columnconfigure(0, weight=100)
key_pad_frame.columnconfigure(1, weight=1)
key_pad_frame.columnconfigure(2, weight=1)
key_pad_frame.columnconfigure(3, weight=1)
key_pad_frame.columnconfigure(4, weight=1)
key_pad_frame.columnconfigure(5, weight=100)

# Create result widget
result = tkinter.Entry(key_pad_frame)
result.grid(row=0, column=1, sticky='nsew', columnspan=4)

# Create the calculator keys
calc_c_button = tkinter.Button(key_pad_frame, text='C')
calc_ce_button = tkinter.Button(key_pad_frame, text='CE')
calc_7_button = tkinter.Button(key_pad_frame, text='7')
calc_8_button = tkinter.Button(key_pad_frame, text='8')
calc_9_button = tkinter.Button(key_pad_frame, text='9')
calc_plus_button = tkinter.Button(key_pad_frame, text='+')
calc_4_button = tkinter.Button(key_pad_frame, text='4')
calc_5_button = tkinter.Button(key_pad_frame, text='5')
calc_6_button = tkinter.Button(key_pad_frame, text='6')
calc_minus_button = tkinter.Button(key_pad_frame, text='-')
calc_1_button = tkinter.Button(key_pad_frame, text='1')
calc_2_button = tkinter.Button(key_pad_frame, text='2')
calc_3_button = tkinter.Button(key_pad_frame, text='3')
calc_times_button = tkinter.Button(key_pad_frame, text='*')
calc_0_button = tkinter.Button(key_pad_frame, text='0')
calc_equal_button = tkinter.Button(key_pad_frame, text='=')
calc_divide_button = tkinter.Button(key_pad_frame, text='/')

# Align the calculator keys
calc_c_button.grid(row=1, column=1, sticky='ew')
calc_ce_button.grid(row=1, column=2, sticky='ew')
calc_7_button.grid(row=2, column=1, sticky='ew')
calc_8_button.grid(row=2, column=2, sticky='ew')
calc_9_button.grid(row=2, column=3, sticky='ew')
calc_plus_button.grid(row=2, column=4, sticky='ew')
calc_4_button.grid(row=3, column=1, sticky='ew')
calc_5_button.grid(row=3, column=2, sticky='ew')
calc_6_button.grid(row=3, column=3, sticky='ew')
calc_minus_button.grid(row=3, column=4, sticky='ew')
calc_1_button.grid(row=4, column=1, sticky='ew')
calc_2_button.grid(row=4, column=2, sticky='ew')
calc_3_button.grid(row=4, column=3, sticky='ew')
calc_times_button.grid(row=4, column=4, sticky='ew')
calc_0_button.grid(row=5, column=1, sticky='ew')
calc_equal_button.grid(row=5, column=2, sticky='ew', columnspan=2)
calc_divide_button.grid(row=5, column=4, sticky='ew')

# Set the minimum and maximum window sizes
main_window.update()
main_window.minsize(key_pad_frame.winfo_width() + (main_window_padding*2), result.winfo_height() + key_pad_frame.winfo_height())
main_window.maxsize(key_pad_frame.winfo_width() + (main_window_padding*2) + 150, result.winfo_height() + key_pad_frame.winfo_height() + 40)

main_window.mainloop()

######################################################################################################################################################
#####                                  The code below is the provided solution for the above challange exercise                                  #####
######################################################################################################################################################
#####   try:                                                                                                                                     #####
#####       import tkinter                                                                                                                       #####
#####   except ImportError: # python 2                                                                                                           #####
#####       import Tkinter as tkinter                                                                                                            #####
#####                                                                                                                                            #####
#####   keys = [[('C', 1), ('CE', 1)],                                                                                                           #####
#####           [('7', 1), ('8', 1), ('9', 1), ('+', 1)],                                                                                        #####
#####           [('4', 1), ('5', 1), ('6', 1), ('-', 1)],                                                                                        #####
#####           [('1', 1), ('2', 1), ('3', 1), ('*', 1)],                                                                                        #####
#####           [('0', 1), ('=', 1), ('/', 1)],                                                                                                  #####
#####           ]                                                                                                                                #####
#####                                                                                                                                            #####
#####   mainWindowPadding = 8                                                                                                                    #####
#####                                                                                                                                            #####
#####   mainWindow = tkinter.Tk()                                                                                                                #####
#####   mainWindow.title("Calculator")                                                                                                           #####
#####   mainWindow.geometry('640x480-8-200')                                                                                                     #####
#####   mainWindow['padx'] = mainWindowPadding                                                                                                   #####
#####                                                                                                                                            #####
#####   result = tkinter.Entry(mainWindow)                                                                                                       #####
#####   result.grid(row=0, column=0, sticky='nsew')                                                                                              #####
#####                                                                                                                                            #####
#####   keyPad = tkinter.Frame(mainWindow)                                                                                                       #####
#####   keyPad.grid(row=1, column=0, sticky='nsew')                                                                                              #####
#####                                                                                                                                            #####
#####   row = 0                                                                                                                                  #####
#####   for keyRow in keys:                                                                                                                      #####
#####       col = 0                                                                                                                              #####
#####       for key in keyRow:                                                                                                                   #####
#####           tkinter.Button(keyPad, text=key[0]).grid(row=row, column=col, columnspan=key[1], sticky=tkinter.E + tkinter.W)                   #####
#####           col += key[1]                                                                                                                    #####
#####       row += 1                                                                                                                             #####
#####                                                                                                                                            #####
#####   mainWindow.update()                                                                                                                      #####
#####   mainWindow.minsize(keyPad.winfo_width() + mainWindowPadding, result.winfo_height() + keyPad.winfo_height())                              #####
#####   mainWindow.maxsize(keyPad.winfo_width() + mainWindowPadding, result.winfo_height() + keyPad.winfo_height())                              #####
#####                                                                                                                                            #####
#####   mainWindow.mainloop()                                                                                                                    #####
######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################
