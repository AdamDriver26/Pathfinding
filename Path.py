from MapLogic import *

pathMap = Map([8,8],20)
obstacleList = [4,5,7,10,13,18,19,23,26,29,36,37,39,42,45,47,50,51,55,61]
for obs in obstacleList:
  pathMap.regionList[obs].traverse = False


def floodFill(grid, initRef, termRef):
  """

  """
  queue = [ [initRef, 0] ]
  checked = [initRef]
  step = 1
  nCount = 0
  a = 0
  b = 1
  maxIterations = 50

  # Cycles until either the terminal point (with regionList reference termRef) is found, or the maximum number of iterations is reached.
  while ([termRef, step - 1] not in queue) and (step <= maxIterations):

    # The values [a,b) reflect the elements of queue that have not had their neighbours considered.
    for i in range(a,b):

      # Uses the neighbours method of MapLogic to find the neighbouring regions of the current element in the queue. 
      neighbours = grid.neighbours(queue[i][0])

      # Iterates through these neighbours and checks that they: a) are not an obstacle; and b) have not been checked previously.
      # Adds the successful neighbours to the queue with a note of the step and iterates the nCount.
      for neighbour in neighbours:

        if (grid.regionList[neighbour].traverse == True) and (neighbour not in checked):
          print(neighbour, " added")
          queue.append([neighbour,step])
          checked.append(neighbour)
          nCount += 1

    # After all elements of queue added in the last cycle have had their neighbours considered, updates the new values of a & b;
    # resets the nCount; and iterates the current step.
    a = b
    b += nCount
    nCount -= nCount
    step += 1

  # The path is then initiated with the terminal point, from which the next steps will work backwards from.
  orderedPath = [termRef]

  
  return queue


print(floodFill(pathMap,17,59))
