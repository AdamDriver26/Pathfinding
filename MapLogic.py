class Region:
  def __init__(self, ref, centre, corners, traverse):
    """
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

class Map:
  def __init__(self, dim, div):
    """
    Args:
      dim (List[int]): the maximum count of regions on the map.
      div (int): the objective (as opposed to relative, which =1) width of each region on the map.
      regionList (List[int]): a list of all regions.
    """
    self.dim = dim
    self.div = div
    self.regionList = {}

  def generateRegions(self):
    currentRef = 1
    for relY in range(0,self.dim[1]):
      for relX in range(0,self.dim[0]):
        self.regionList[currentRef] = Region(currentRef,[relX+0.5,relY+0.5],[[relX,relY],[relX+1,relY],[relX+1,relY+1],[relX,relY+1]],False)
        currentRef += 1
