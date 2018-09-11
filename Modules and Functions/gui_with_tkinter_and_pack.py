try:
    import tkinter
except ImportError: # Python 2
    import Tkinter as tkinter

# print(tkinter.TkVersion)
# print(tkinter.TclVersion)

main_window = tkinter.Tk()

main_window.title("Hello World!")
main_window.geometry('640x480+10+10')

label = tkinter.Label(main_window, text="Hello World!")
label.pack(side='top')

left_frame = tkinter.Frame(main_window)
left_frame.pack(side="left", anchor="n", fill=tkinter.Y, expand=False)

canvas = tkinter.Canvas(left_frame, relief="raised", borderwidth=1)
canvas.pack(side="top")
#   You need the expand=True if the side is set to either left or right and you are "filling" the X,
#   However, if you are not filling the X and only the Y when side is set to left or right the "expand"
#   argument is not nessicary.
# canvas.pack(side="left", fill=tkinter.X, expand=True)
#   You need the expand=True if the side is set to either top or bottom and you are "filling" the Y,
#   However, if you are not filling the Y and only the X when side is set to top or bottom the "expand"
#   argument is not nessicary.
# canvas.pack(side="top", fill=tkinter.Y, expand=True)
#   You can also set both X and Y to fill using the following:
# canvas.pack(side="left", fill=tkinter.BOTH, expand=True)
#   Note that you do need the expand argument in this particular case above.

right_frame = tkinter.Frame(main_window)
right_frame.pack(side="right", anchor="n", expand=True)

left_button = tkinter.Button(right_frame, text="Left")
right_button = tkinter.Button(right_frame, text="Right")
exit_button = tkinter.Button(right_frame, text="Exit")
left_button.pack(side="top")
right_button.pack(side="top")
exit_button.pack(side="top")

main_window.mainloop()