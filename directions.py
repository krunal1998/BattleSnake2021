class Directions:
  def __init__(self):
    self.north = 100
    self.south = 100
    self.east = 100
    self.west = 100

  
  def toString(self):
    return 'N:'+str(self.north) + 'S:'+str(self.south) + 'E:'+str(self.east) + 'W:'+str(self.west)
    
  
  def bestDirection(self):
    bestDir = "up"
    bestVal = 0
    
    if self.north > bestVal:
      bestVal = self.north
      bestDir = "up"
    
    if self.south > bestVal:
      bestVal = self.south
      bestDir = "down"
    
    if self.east > bestVal:
      bestVal = self.east
      bestDir = "right"
    
    if self.west > bestVal:
      bestVal = self.west
      bestDir = "left"

    return bestDir