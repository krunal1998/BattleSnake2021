import json
import math
import random

boardTypes = {'Empty': 0, 'Wall': 1, 'Snake_Body': 2, 'Snake_Head': 3, 'Food': 4}

def distanceBetweenTwoPoints(point1, point2):
  return  (abs((point2['x'] - point1['x'])) + abs((point2['y'] - point1['y'])))


def createBoardObject(data, snakes):
  global boardTypes
  boardHeight = data["board"]["height"]
  boardWidth = data["board"]["width"]
  
  # Create empty board 
  Board = [[0 for x in range(boardHeight)] for x in range(boardWidth)]
  
  # Start off as empty
  for i in range(boardHeight - 1):
    for j in range(boardWidth - 1):
      Board[i][j] = boardTypes['Empty']
  
  # Find Snakes
  #print("~~~~~~~~Adding Snake in Board~~~~~~~")
  for snake in snakes:
    for index, point in enumerate(snake.coordinates, start=0):
      #print(snake.coordinates)
      if index == 0:
        Board[point['x']][point['y']] = boardTypes['Snake_Head']
      else:
        # Unnecessary Condition
        if Board[point['x']][point['y']] != boardTypes['Snake_Head']:
          Board[point['x']][point['y']] = boardTypes['Snake_Body']
  
  # Find Food
  #print("~~~~~~~Adding Food in Board~~~~~~~~")
  for leaf in data['board']['food']:
    #print (leaf)
    Board[leaf['x']][leaf['y']] = boardTypes['Food']
  
  return Board