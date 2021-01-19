from MapLogic import *

pathMap = Map([8,8],20)

# obstacleList = [56, 54, 30, 43, 42, 45, 44, 67, 55, 41, 53, 52, 40, 29, 51, 64, 66, 65, 77, 79, 78, 68] # for 12,10
obstacleList = [4,5,7,10,13,18,19,23,26,29,36,37,39,42,45,47,50,51,55,61] 

for obs in obstacleList:
  pathMap.regionList[obs].traverse = False

def sampleAlg(map, initRef, termRef):
  queue = [ [initRef, 0] ]
  step = 1
  maxIterations = 10

  
  # Loop until either the terminal point is included in the queue for any step
  # or the number of steps exceeds maxIterations
  while (not any(x in list([termRef,s] for s in range(step) ) for x in queue) ) and ( step <= maxIterations ): 
    if step == 6:
      queue.append([termRef,step])
    print(step,":",queue)
    print([termRef,step])
    #print([termRef,any(s for s in range(step))])


    
    step += 1

  """
  while ([termRef,step] not in queue) and (step <= maxIterations):
    step += 1
    for checked in queue:
      currentNeighbours = pathMap.neighbours(checked[0])
      print("checked pos:",checked)
      print("neighbours list: ",currentNeighbours)

      for neighbourRef in currentNeighbours:
        print("neighbour ref: ",neighbourRef)
        if (pathMap.regionList[neighbourRef].traverse == False) or ( [neighbourRef, (i for i in range(step))] in queue):
          currentNeighbours.remove(neighbourRef)

      queue.append([neighbourRef, step])
    
      print("queue: ",queue)
  """


sampleAlg(pathMap,17,59)
queue = [[17,0], [59,4]]
step = 5

print( not any(x in list([59,s] for s in range(step) ) for x in queue) )
