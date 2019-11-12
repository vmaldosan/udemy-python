try:
	import tkinter
except ImportError:  # python 2
	import TKinter as tkinter


def parabola(x):
	return x * x / 100


def draw_axes(p_canvas):
	p_canvas.update()
	x_origin = p_canvas.winfo_width() / 2
	y_origin = p_canvas.winfo_height() / 2
	p_canvas.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
	p_canvas.create_line(-x_origin, 0, x_origin, 0, fill='white')
	p_canvas.create_line(0, y_origin, 0, -y_origin, fill='white')


def plot(p_canvas, x, y):
	p_canvas.create_line(x, y, x + 1, y + 1, fill='blue')


mainWindow = tkinter.Tk()
mainWindow.title('Parabola')
mainWindow.geometry('900x600')

canvas = tkinter.Canvas(mainWindow, width=450, height=600)
canvas.grid(row=0, column=0)

canvas2 = tkinter.Canvas(mainWindow, width=450, height=600, background='#cccccc')
canvas2.grid(row=0, column=1)

print(repr(canvas), repr(canvas2))
draw_axes(canvas)
draw_axes(canvas2)

for x in range(-100, 100):
	y = parabola(x)
	# print(y)
	plot(canvas, x, -y)

mainWindow.mainloop()
