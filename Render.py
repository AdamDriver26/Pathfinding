from tkinter import *
import time
from MapLogic import *
from Path import *

renderMap = Map([8,8],80)

obstacleList = [4,5,7,10,13,18,19,23,26,29,36,37,39,42,45,47,50,51,55,61]

for obs in obstacleList:
  renderMap.regionList[obs].traverse = False

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

colors = {} #values 0-10 with gradually darker colours

queue = floodFill(renderMap,17,59)

# print(queue)

for x in queue:
  reference = x[0]
  region = renderMap.regionList[reference]
  canvas.create_oval([i*h for i in region.corners[0] + region.corners[2]], fill="black")

gui.mainloop()