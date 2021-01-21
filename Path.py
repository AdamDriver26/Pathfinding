from MapLogic import *

pathMap = Map([8,8],20)

# obstacleList = [56, 54, 30, 43, 42, 45, 44, 67, 55, 41, 53, 52, 40, 29, 51, 64, 66, 65, 77, 79, 78, 68] # for 12,10
obstacleList = [4,5,7,10,13,18,19,23,26,29,36,37,39,42,45,47,50,51,55,61]

for obs in obstacleList:
  pathMap.regionList[obs].traverse = False


def floodFill(grid, initRef, termRef):
  queue = [ [initRef, 0] ]
  checked = [initRef]
  step = 1
  nCount = 0
  a = 0
  b = 1
  maxIterations = 50

  # for reg in grid.regionList:
  #   if grid.regionList[reg].traverse == True:
  #     unchecked.append(grid.regionList[reg].ref)

  while ([termRef, step - 1] not in queue) and (step <= maxIterations):
    print("a:",a,"b:",b,"nCount:",nCount)
    for i in range(a,b):

      neighbours = grid.neighbours(queue[i][0])
      print("unchecked neighbours of ",queue[i][0]," at position ",i,": ",neighbours)

      for neighbour in neighbours:

        if (grid.regionList[neighbour].traverse == True) and (neighbour not in checked):
          print(neighbour, " added")
          queue.append([neighbour,step])
          checked.append(neighbour)
          nCount += 1

        print(nCount)

      print("step:",step,", queue:",queue)
    a = b
    b += nCount
    nCount -= nCount
    step += 1
  
  return queue


floodFill(pathMap,17,59)

#[[59, 0], [58, 1], [60, 1], [57, 2], [52, 2], [49, 2], [44, 3], [53, 3], [41, 3], [43, 3], [54, 4], [33, 4], [35, 4], [46, 4], [62, 4], [25, 5], [34, 5], [27, 5], [38, 5], [63, 5], [17, 5]]