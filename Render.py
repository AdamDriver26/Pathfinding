from tkinter import *
import time
from MapLogic import *

renderMap = Map([12,10],80)

X = renderMap.dim[0]*renderMap.div
Y = renderMap.dim[1]*renderMap.div
h = renderMap.div # Grid division width

drawnObstacles = {}

def toggleObstacle(event):
  reg = renderMap.regionList[renderMap.objCoordinateToRef([event.x,event.y])]
  if reg.ref in drawnObstacles:
    canvas.delete("obstacle" + str(reg.ref))
    drawnObstacles.pop(reg.ref)

  else:
    reg.traverse = False
    drawnObstacles[reg.ref] = canvas.create_rectangle([i*h for i in reg.corners[0] + reg.corners[2]], fill="grey20", outline="", tags="obstacle" + str(reg.ref))

def printObstacles(event):
  print(drawnObstacles)

gui = Tk()
gui.geometry(str(X) + "x" + str(Y))
gui.title("Pathfinder")

canvas = Canvas(gui, width=X, height=Y, bg='grey90')
canvas.bind("<Button-1>", toggleObstacle)
canvas.bind("<Button-3>", printObstacles)
canvas.pack()

# Creates vertical grid lines
for i in range(0,X,h):
  canvas.create_line(i,0,i,Y, fill="grey80", width=2)

# Creates horizontal grid lines
for j in range(0,Y,h):
  canvas.create_line(0,j,X,j, fill="grey80", width=2)

gui.mainloop()