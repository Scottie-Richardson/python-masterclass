import tkinter

print(tkinter.TkVersion)
print(tkinter.TclVersion)

main_window = tkinter.Tk()

main_window.title("Hello World!")
main_window.geometry('640x480+10+10')
main_window.mainloop()