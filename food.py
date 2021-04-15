import json

class Foods():
  def __init__(self, foods):
    #print ("~~~~~~~~~Food Object Created~~~~~~~")
    self.foods = foods
    #print (self.foods)
  
  
  def distanceToFood(self, snake):
    foods = []
    # IF mySnake is passed to this method then data type of snake will be dictionary otherwise it'll be Snake class' object
    if (type(snake) is dict):
      head = snake['head']
    else:
      head = snake.head

    for food in self.foods:
      x =  head['x'] - food['x']
      y =  head['y'] - food['y']
      foods.append(abs(x) + abs(y))
    
    return foods
  
  
  def amClosest(self, snakes, mySnake):
    # calculate each food's distance from our snake head
    myDistance = self.distanceToFood(mySnake)
    
    for snake in snakes:
      # Check for current snake is not mySnake
      if( snake.id != mySnake['id']):
        #Calculate each food's distance from snake head 
        snakeDistance = self.distanceToFood(snake)
        
        #now check our snake's food distance with others  
        for i in range(0,len(snakeDistance)):
          # If our distance is greater than no need to go there, so set highest value in distance
          if myDistance[i] > snakeDistance[i]:
            myDistance[i] = 100
          # If our distance is same but our snake small, then no need to go there, so set highest value in distance
          if myDistance[i] == snakeDistance[i]:
            if len(snake.coordinates) > mySnake['length']:
              myDistance[i] = 100
    
    closest = []
    for distance in myDistance:
      if distance < 100:
        closest.append(distance)
      else:
        closest.append(-1)
    
    return closest
  
  
  def goTowards(self, closest, direction, mySnake):
    foodWeight = 10
    head = mySnake['head']
    for i in range(0, len(self.foods)):
      if closest[i] >= 0:
        #print ("i am closest to " , str(closest[i]))
        food = self.foods[i]
        
        # Calculate Vertical Distance
        vertDist = food['y'] - head['y']
        # Calculate Horizontal Distance
        horDist = food['x'] - head['x']
        
        #If vertical distance is +ve, it means food is located on the North side of the head 
        if vertDist > 0:
          direction.north *= (1 + foodWeight/closest[i])
        
        #If vertical distance is -ve, it means food is located on the South side of the head
        elif vertDist < 0:
          direction.south *= (1 + foodWeight/closest[i])
        
        #If Horizontal distance is +ve, it means food is located on the East side of the head
        if horDist > 0:
          direction.east *= (1 + foodWeight/closest[i])
        #If Horizontal distance is -ve, it means food is located on the West side of the head
        elif horDist < 0:
          direction.west *= (1 + foodWeight/closest[i])
    return direction
