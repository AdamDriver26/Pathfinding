from tkinter import *
import time
from MapLogic import *

renderMap = Map([16,12],50)
renderMap.generateRegions()

gui = Tk()
gui.geometry("800x600")
gui.title("Pathfinder")
canvas = Canvas(gui, width=800, height=600, bg='grey90')
canvas.pack()

h = renderMap.div # Grid division width

print(renderMap.regionList[5].corners)

# Creates vertical grid lines
for i in range(0,800,h):
  canvas.create_line(i,0,i,600, fill="grey80", width=2)

# Creates horizontal grid lines
for j in range(0,600,h):
  canvas.create_line(0,j,800,j, fill="grey80", width=2)

#rect1 = canvas.create_rectangle(10,10, 150,150, fill="grey30", outline="")
#poly1 = canvas.create_polygon([200,250, 220,260, 220,280, 300,255, 250,180], fill="grey30", outline="")

#obstacle = canvas.create_polygon([2*h,2*h, 3*h,h, 5*h,h, 6*h,4*h, 4*h,5*h, 2*h,4*h], fill="grey30", outline="")

bodyR = 5*h/18 # Radius of the "creatures" body
bodyPos = [1.5*h, 2.5*h]

creatureBodyOuter = canvas.create_oval(bodyPos[0]-bodyR, bodyPos[1]-bodyR, bodyPos[0]+bodyR, bodyPos[1]+bodyR, fill="red", outline="")
creatureBodyInner = canvas.create_oval(bodyPos[0]-4*bodyR/5, bodyPos[1]-4*bodyR/5, bodyPos[0]+4*bodyR/5, bodyPos[1]+4*bodyR/5, fill="LightSalmon", outline="")

test1 = canvas.create_line(renderMap.regionList[4].centre[0]*h,renderMap.regionList[4].centre[1]*h,renderMap.regionList[5].centre[0]*h,renderMap.regionList[5].centre[1]*h, width=5)

test2 = canvas.create_line(renderMap.regionList[2].centre[0]*h,renderMap.regionList[2].centre[1]*h,renderMap.regionList[100].centre[0]*h,renderMap.regionList[100].centre[1]*h, width=5)

print(renderMap.regionList[4].centre)
print(renderMap.regionList[5].centre)

gui.mainloop()