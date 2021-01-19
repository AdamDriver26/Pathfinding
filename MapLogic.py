import math

class Region:
  def __init__(self, ref, centre, corners, traverse):
    """
    Represents a division of the map which can traversable by the "creature" or an obstacle.
    Args:
      ref (int): a *unique* reference for a single region.
      centre (List[int]): the relative coordinates of the regions centre.
      corners (List[int]): the relative coordinates of the regions four vertices, counted clockwise starting from the top left.
      traverse (Boolean): whether the region is an obstacle (False) or traversable (True).
    """
    self.ref = ref
    self.centre = centre
    self.corners = corners
    self.traverse = traverse

  @staticmethod
  def disVector(a, b):
    return [b.centre[0] - a.centre[0], b.centre[1] - a.centre[1]]

  @staticmethod
  def disMetric(a, b):
    return math.sqrt((b.centre[0] - a.centre[0])**2 + (b.centre[1] - a.centre[1])**2)


class Map:
  def __init__(self, dim, div):
    """
    The Map class represents a union of all the Region objects.
    Args:
      dim (List[int]): the maximum count of regions on the map.
      div (int): the objective (as opposed to relative, which =1) width of each region on the map.
      regionList (List[int]): a list of all regions.
    """
    self.dim = dim
    self.div = div
    self.regionList = {}
    self.generateRegions()

  def generateRegions(self):
    currentRef = 1
    for relY in range(self.dim[1]):
      for relX in range(self.dim[0]):
        self.regionList[currentRef] = Region(currentRef,[relX+0.5,relY+0.5],[[relX,relY],[relX+1,relY],[relX+1,relY+1],[relX,relY+1]],True)
        currentRef += 1

  def objCoordinateToRef(self,pos):
    return self.dim[0]*(pos[1]//self.div) + (pos[0]//self.div) + 1

  def neighbours(self, ref):
    neighboursList = []
    if ref % self.dim[0] == 0:                  # Checks that the region is in the Eastern column

      if ref != self.dim[0]:                       # Checks that the province is not the North Eastern corner
        neighboursList.append(ref - self.dim[0])   # Adds the Northern region reference

      if ref != self.dim[0]*self.dim[1]:           # Checks that the province is not the South Eastern corner
        neighboursList.append(ref + self.dim[0])   # Adds the Southern region reference 

      neighboursList.append(ref - 1)               # Adds the Western region reference    

    elif ref % self.dim[0] == 1:                # Checks that the region is in the Western column
      
      if ref != 1:                                 # Checks that the province is not the North Western corner
        neighboursList.append(ref - self.dim[0])   # Adds the Northern region reference

      if ref != self.dim[0]*(self.dim[1] - 1) + 1: # Checks that the province is not the South Western corner
        neighboursList.append(ref + self.dim[0])   # Adds the Southern region reference 

      neighboursList.append(ref + 1)               # Adds the Eastern region reference  

    else:                                           # The remaining regions are in the center columns

      if ref > self.dim[0]:                          # Checks that the region is not in the Northern row
        neighboursList.append(ref - self.dim[0])     # Adds the Northern region reference 

      if ref < self.dim[0]*(self.dim[1] - 1):        # Checks that the region is not in the Southern row
        neighboursList.append(ref + self.dim[0])     # Adds the Southern region reference 

      neighboursList.append(ref + 1)              # Adds the Eastern region reference 
      neighboursList.append(ref - 1)              # Adds the Western region reference

    return sorted(neighboursList)

testMap = Map([8,8],50)
print(len(testMap.regionList))
#print( testMap.neighbours(testMap.regionList(5)) )

print( testMap.neighbours(  17  ) )


