from utility import *

class Snake():
  def __init__(self, snake):
    #print("~~~~~~Snake Object Created~~~~~~~")
    self.id = snake['id'] 
    #print(self.id)
    self.name = snake['name']
    #print(self.name)
    self.health = snake['health']
    #print(self.health)
    self.coordinates = snake['body']
    #print(self.coordinates)
    self.head = snake['head']
    #print(self.head)
    self.length = snake['length']
    #print(self.length)
  
  
  # only attack when our snake is longer than enemySnake and distance between two snakes is less than 3
  def shouldAttack(self, enemySnake):
    if self.length <= enemySnake.length:
      return False
    
    if distanceBetweenTwoPoints(self.head, enemySnake.head) < 3:
      return True
  
  
  def attackDirection(self, enemySnake):
    #print("EnemySnake ID: ", enemySnake.id, "=",enemySnake.head)
    head = enemySnake.head
    vertDiff = head['y'] - self.head['y']
    horDiff = head['x'] - self.head['x']
    
    if vertDiff > 0: return 'north'
    elif vertDiff < 0: return 'south'
    
    if horDiff > 0: return 'east'
    elif horDiff < 0: return 'west'
  
  
  def attack(self, directions, snakes):
    for snake in snakes:
      if snake.id == self.id: continue
      
      direction = self.attackDirection(snake)
      if self.shouldAttack(snake):  
        if (direction == 'north'): directions.north *= 2
        elif (direction == 'south'): directions.south *= 2
        elif (direction == 'east'): directions.east *= 2
        elif (direction == 'west'): directions.west *= 2
      
      else:
        if self.length <= snake.length and distanceBetweenTwoPoints(self.head, snake.head) < 3:
          if (direction == 'north'): directions.north *= .1
          elif (direction == 'south'): directions.south *= .1
          elif (direction == 'east'): directions.east *= .1
          elif (direction == 'west'): directions.west *= .1 
    
    return directions
        