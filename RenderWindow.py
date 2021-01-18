from tkinter import *
import time
from MapLogic import *

renderMap = Map([12,10],80)

obstacleList = []

def toggleObstacles(event):
  ref = renderMap.objCoordinateToRef([event.x,event.y])
  if ref in obstacleList:
    obstacleList.remove(ref)
  else:
    obstacleList.append(ref)
  print("Position = ({0},{1})".format(event.x, event.y))

def drawBox(event):
  cor = renderMap.regionList[9].corners
  #cor = renderMap.regionList[obstacleList[0]].corners
  canvas.create_rectangle(cor[0] + cor[2], fill="black")

def drawObstacles(event):
  for obID in obstacleList:
    renderMap.regionList[obID].traverse = False
    canvas.create_rectangle([i * h for i in renderMap.regionList[obID].corners[0] + renderMap.regionList[obID].corners[2]], fill="grey20", outline="")
    gui.update()
    time.sleep(.05)


for obID in obstacleList:
  renderMap.regionList[obID].traverse = False

X = renderMap.dim[0]*renderMap.div
Y = renderMap.dim[1]*renderMap.div
h = renderMap.div # Grid division width

gui = Tk()
gui.geometry(str(X) + "x" + str(Y))
gui.title("Pathfinder")
gui.bind("<Escape>", lambda x: gui.destroy())

canvas = Canvas(gui, width=X, height=Y, bg='grey90')
canvas.bind('<Button-1>', toggleObstacles)
gui.bind("<Button-3>", drawBox)

canvas.pack()



# Creates vertical grid lines
for i in range(0,X,h):
  canvas.create_line(i,0,i,Y, fill="grey80", width=2)

# Creates horizontal grid lines
for j in range(0,Y,h):
  canvas.create_line(0,j,X,j, fill="grey80", width=2)



# Draws obstacles
for reg in renderMap.regionList:
  if not renderMap.regionList[reg].traverse:
    canvas.create_rectangle([i * h for i in renderMap.regionList[reg].corners[0] + renderMap.regionList[reg].corners[2]], fill="grey20", outline="")



#rect1 = canvas.create_rectangle(10,10, 150,150, fill="grey30", outline="")
#poly1 = canvas.create_polygon([200,250, 220,260, 220,280, 300,255, 250,180], fill="grey30", outline="")

#obstacle = canvas.create_polygon([2*h,2*h, 3*h,h, 5*h,h, 6*h,4*h, 4*h,5*h, 2*h,4*h], fill="grey30", outline="")

bodyR = 5*h/18 # Radius of the "creatures" body

initReg = renderMap.regionList[ 2 ]
termReg = renderMap.regionList[ 30 ]

start = canvas.create_rectangle([i * h for i in initReg.corners[0] + initReg.corners[2]], fill="pale green", outline="green")
end = canvas.create_rectangle([i * h for i in termReg.corners[0] + termReg.corners[2]], fill="IndianRed1", outline="red")

bodyPos = [initReg.centre[0]*h, initReg.centre[1]*h]

creatureBodyOuter = canvas.create_oval(bodyPos[0]-bodyR, bodyPos[1]-bodyR, bodyPos[0]+bodyR, bodyPos[1]+bodyR, fill="orange red", outline="")
creatureBodyInner = canvas.create_oval(bodyPos[0]-4*bodyR/5, bodyPos[1]-4*bodyR/5, bodyPos[0]+4*bodyR/5, bodyPos[1]+4*bodyR/5, fill="LightSalmon", outline="")

vec = Region.disVector(initReg,termReg)
print(Region.disMetric(initReg,termReg))
steps = math.floor(100/Region.disMetric(initReg,termReg))

for n in range(steps):
  canvas.move(creatureBodyOuter, h*vec[0]/steps, h*vec[1]/steps)
  canvas.move(creatureBodyInner, h*vec[0]/steps, h*vec[1]/steps)
  gui.update()
  time.sleep(.05)

print(obstacleList)

gui.update()
time.sleep(.05)

gui.mainloop()