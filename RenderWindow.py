from tkinter import *
import time

gui = Tk()
gui.geometry("800x600")
gui.title("Pathfinder")
canvas = Canvas(gui, width=800, height=600, bg='grey90')
canvas.pack()

h = 100 # Grid division width

# Creates vertical grid lines
for i in range(0,800,h):
  canvas.create_line(i,0,i,600, fill="grey80", width=2)

# Creates horizontal grid lines
for j in range(0,600,h):
  canvas.create_line(0,j,800,j, fill="grey80", width=2)

#rect1 = canvas.create_rectangle(10,10, 150,150, fill="grey30", outline="")
#poly1 = canvas.create_polygon([200,250, 220,260, 220,280, 300,255, 250,180], fill="grey30", outline="")

obstacle = canvas.create_polygon([2*h,2*h, 3*h,h, 5*h,h, 6*h,4*h, 4*h,5*h, 2*h,4*h], fill="grey30", outline="")

bodyR = 5*h/22 # Radius of the "creatures" body
bodyPos = [1.5*h, 2.5*h]

creatureBody = canvas.create_oval(bodyPos[0]-bodyR, bodyPos[1]-bodyR, bodyPos[0]+bodyR, bodyPos[1]+bodyR, fill="red", outline="")

gui.mainloop()