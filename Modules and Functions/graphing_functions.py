import math

try:
    import tkinter
except ImportError:  # Pyhton 2
    import Tkinter as tkinter

def draw_axes(canvas):
    canvas.update()
    x_origin = canvas.winfo_width() / 2
    y_origin = canvas.winfo_height() / 2
    canvas.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin,))
    # Notice that the create_line method for the X and Y axes are implemented differently
    canvas.create_line(-x_origin, 0, x_origin, 0, fill='black')
    canvas.create_line(0, -y_origin, 0, y_origin, fill='black')


def parabola(canvas, size):
    for x in range(size):
        y = x * x / size
        plot(canvas, x, y)
        plot(canvas, -x, y)


def plot(canvas, x, y):
    canvas.create_line(x, -y, x + 1, -y + 1, fill='red')


def circle(canvas, radius, g, h, line_color='red', line_width=1):  # Remember that default values are set like this
    # g is the x cooridinate and h is the y coordinate for the center point of the circle
    # The code below works, but is significantly slower than jus using the create_oval method
    # for x in range(g * 100, (g + radius) * 100):
    #     x /= 100
    #     y = h + (math.sqrt(radius ** 2 - ((x - g) ** 2)))
    #     plot(canvas, x, y)
    #     plot(canvas, x, 2 * h - y)
    #     plot(canvas, 2 * g - x, y)
    #     plot(canvas, 2 * g - x, 2 * h - y)
    top_x = g + radius
    top_y = h + radius
    bottom_x = g - radius
    bottom_y = h - radius
    canvas.create_oval(top_x, top_y, bottom_x, bottom_y, outline=line_color, width=line_width)


main_window = tkinter.Tk()

main_window.title('Graph')
main_window.geometry('1000x1000')

graph_1 = tkinter.Canvas(main_window, width=1000, height=1000)
graph_1.grid(row=0, column=0)

draw_axes(graph_1)

parabola(graph_1, 100)
parabola(graph_1, 200)
parabola(graph_1, 300)
circle(graph_1, 100, 100, 100, 'blue')
circle(graph_1, 100, 100, -100, 'blue')
circle(graph_1, 100, -100, 100, 'blue')
circle(graph_1, 100, -100, -100, 'blue')
circle(graph_1, 10, 30, 30, 'green')
circle(graph_1, 10, 30, -30, 'green')
circle(graph_1, 10, -30, 30, 'green')
circle(graph_1, 10, -30, -30, 'green')
circle(graph_1, 30, 0, 0)
circle(graph_1, 300, 0, 0)


main_window.mainloop()