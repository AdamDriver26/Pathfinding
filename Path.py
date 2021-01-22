from MapLogic import *
import random

pathMap = Map([16,16],20)
obstacleList = [219, 218, 217, 215, 214, 213, 216, 182, 166, 200, 184, 239, 238, 240, 204, 205, 206, 236, 252, 220, 208, 192, 176, 160, 155, 171, 187, 203]
for obs in obstacleList:
  pathMap.regionList[obs].traverse = False


def floodFill(grid, initRef, termRef):
  """

  """
  queue = [ [initRef, 0] ]
  checked = [initRef]
  fStep = 1
  nCount = 0
  a = 0
  b = 1
  maxIterations = 1000

  # Cycles until either the terminal point (with regionList reference termRef) is found, or the maximum number of iterations is reached.
  while ([termRef, fStep - 1] not in queue) and (fStep <= maxIterations):

    # The values [a,b) reflect the elements of queue that have not had their neighbours considered.
    for i in range(a,b):

      # Uses the neighbours method of MapLogic to find the neighbouring regions of the current element in the queue. 
      neighbours = grid.neighbours(queue[i][0])

      # Iterates through these neighbours and checks that they: a) are not an obstacle; and b) have not been checked previously.
      # Adds the successful neighbours to the queue with a note of the step and iterates the nCount.
      for neighbour in neighbours:

        if (grid.regionList[neighbour].traverse == True) and (neighbour not in checked):
          print(neighbour, " added")
          queue.append([neighbour,fStep])
          checked.append(neighbour)
          nCount += 1

    # After all elements of queue added in the last cycle have had their neighbours considered, updates the new values of a & b;
    # resets the nCount; and iterates the current step.
    a = b
    b += nCount
    nCount -= nCount
    fStep += 1

  # The path is then initiated with the terminal point, from which the next steps will work backwards from.
  orderedPath = [termRef]
  # The step at which the termRef was found.
  maxStep = queue[-1][1]

  # Iterates backwards in range (-1,maxStep] = [0,maxStep], as the path is found backwards from the terminal point, given by termRef.
  for bStep in range(maxStep - 1,-1,-1):
    neighbours = grid.neighbours(orderedPath[0])
    options = []

    for neighbour in neighbours:
      if [neighbour, bStep] in queue:
        options.append(neighbour)
    
    orderedPath.insert(0, random.choice(options))
    print("path:",orderedPath,"at step:",bStep)
  
  return [orderedPath, queue]


print(floodFill(pathMap,247,256))
