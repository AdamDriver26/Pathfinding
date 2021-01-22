from tkinter import *
import time
from MapLogic import *
from Path import *
import random

renderMap = Map([20,16],50)

X = renderMap.dim[0]*renderMap.div
Y = renderMap.dim[1]*renderMap.div
h = renderMap.div # Grid division width

initReg = random.randrange(0,renderMap.dim[0]*renderMap.dim[1]+1)
termReg = random.choice([random.randrange(0,initReg), random.randrange(initReg + 1, renderMap.dim[0]*renderMap.dim[1]+1)])


drawnObstacles = {}

def toggleObstacle(event):
  reg = renderMap.regionList[renderMap.objCoordinateToRef([event.x,event.y])]
  if reg.ref in drawnObstacles:
    canvas.delete("obstacle" + str(reg.ref))
    drawnObstacles.pop(reg.ref)
    renderMap.regionList[reg.ref].traverse = True

  else:
    renderMap.regionList[reg.ref].traverse = False
    drawnObstacles[reg.ref] = canvas.create_rectangle([i*h for i in reg.corners[0] + reg.corners[2]], fill="grey20", outline="", tags="obstacle" + str(reg.ref))

def printObstacles(event):
  print(drawnObstacles.keys())

def genPath(event):
  path, queue = floodFill(renderMap,initReg,termReg)
  colours = colourGradient(len(path))
  print(path)
  print(queue)
  for x in queue:
    reference = x[0]
    region = renderMap.regionList[reference]
    canvas.create_rectangle([i*h for i in region.corners[0] + region.corners[2]], fill=colours[x[1]], outline="")
  
  for j in range(0,len(path)-1):
    canvas.create_line([k*h for k in renderMap.regionList[path[j]].centre + renderMap.regionList[path[j+1]].centre], fill="#094481", width=4)
    #canvas.create_oval([renderMap.regionList[path[j+1]].corners[0]*h-2, renderMap.regionList[path[j+1]].corners[1]*h-2, renderMap.regionList[path[j+1]].corners[0]*h+2, renderMap.regionList[path[j+1]].corners[1]*h+2], fill="#094481", width=4)





def colourGradient(maxSteps):
  startGreenRGB = [250,250,110]
  endRedRGB = [159,21,21]
  output = ['#%02x%02x%02x' % (startGreenRGB[0], startGreenRGB[1], startGreenRGB[2])]

  for i in range(1,maxSteps):
    output.append('#%02x%02x%02x' % (startGreenRGB[0]+i*(endRedRGB[0]-startGreenRGB[0])//maxSteps, startGreenRGB[1]+i*(endRedRGB[1]-startGreenRGB[1])//maxSteps, startGreenRGB[2]+i*(endRedRGB[2]-startGreenRGB[2])//maxSteps))
    
  output.append('#%02x%02x%02x' % (endRedRGB[0], endRedRGB[1], endRedRGB[2]))

  return output

gui = Tk()
gui.geometry(str(X) + "x" + str(Y))
gui.title("Pathfinder")

canvas = Canvas(gui, width=X, height=Y, bg='grey90')
canvas.bind("<Button-1>", toggleObstacle)
canvas.bind("<Button-3>", printObstacles)
gui.bind("<Return>", genPath)
canvas.pack()

# Creates vertical grid lines
for i in range(0,X,h):
  canvas.create_line(i,0,i,Y, fill="grey80", width=2)

# Creates horizontal grid lines
for j in range(0,Y,h):
  canvas.create_line(0,j,X,j, fill="grey80", width=2)

# Create the start and end point rectangles.
canvas.create_rectangle([i*h for i in renderMap.regionList[initReg].corners[0] + renderMap.regionList[initReg].corners[2]], fill="#af3448")
canvas.create_rectangle([i*h for i in renderMap.regionList[termReg].corners[0] + renderMap.regionList[termReg].corners[2]], fill="#360981")

gui.mainloop()

