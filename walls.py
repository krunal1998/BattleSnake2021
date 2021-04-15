import json
from utility import *


class Walls():
    def wallCollision(self, data, direction, mySnake):
        
        snake_head = mySnake['head']
#        if len(snake_head) < 2:
#            return direction

        width = data["board"]["width"]
        height = data["board"]["height"]

        north_result = 100
        east_result = 100
        west_result = 100
        south_result = 100

        if snake_head['x'] == 0:  # head on left side, don't go west
            west_result = 0
            direction.west = 0

        if snake_head['x'] == width - 1:  # head on right side, don't go east
            east_result = 0
            direction.east = 0

        if snake_head['y'] == height - 1:  # head on top side, don't go north
            north_result = 0
            direction.north = 0

        if snake_head['y'] == 0:  # head on bottom, dont go south
            south_result = 0
            direction.south = 0

        # result_json = {"north": north_result, "east": east_result, "west": west_result, "south": south_result}
        # print ("result_json: " , str(result_json))
        # return result_json
        return direction

    def snakeCollision(self, data, board, direction, mySnake):

        width = data["board"]["width"]
        height = data["board"]["height"]

        head = mySnake['head']

        north = ""
        south = ""
        east = ""
        west = ""

        if head['y'] > 0:
            south = board[head['x']][head['y'] - 1]
        if head['y'] < height - 1:
            north = board[head['x']][head['y'] + 1]
        if head['x'] > 0:
            west = board[head['x'] - 1][head['y']]
        if head['x'] < width - 1:
            east = board[head['x'] + 1][head['y']]

        boardTypes = {'Empty': 0, 'Wall': 1, 'Snake_Body': 2, 'Snake_Head': 3, 'Food': 4}

        if north == boardTypes["Snake_Body"] or north == boardTypes["Snake_Head"]:
            direction.north = 0
            print ("Snake north")

        if south == boardTypes["Snake_Body"] or south == boardTypes["Snake_Head"]:
            direction.south = 0
            print ("Snake south")

        if east == boardTypes["Snake_Body"] or east == boardTypes["Snake_Head"]:
            direction.east = 0
            print ("Snake east")

        if west == boardTypes["Snake_Body"] or west == boardTypes["Snake_Head"]:
            direction.west = 0
            print ("Snake west")

        return direction


    def deadEndDetection(self, board, mySnake, direction):

        boardTypes = {'Empty': 0, 'Wall': 1, 'Snake_Body': 2, 'Snake_Head': 3, 'Food': 4}

        boardHeight = len(board)
        boardWidth = len(board[0])

        head = mySnake['head']
        leftOfHead = head['x'] - 1
        rightOfHead = head['x'] + 1
        #aboveHead = head['y'] - 1
        aboveHead = head['y'] + 1
        #belowHead = head['y'] + 1
        belowHead = head['y'] - 1
        deadEndDetectedNorth = True
        deadEndDetectedSouth = True
        deadEndDetectedEast = True
        deadEndDetectedWest = True
        distanceToBlockNorth = 0
        distanceToBlockSouth = 0
        distanceToBlockEast = 0
        distanceToBlockWest = 0

        # Check North
        for i in range(aboveHead, boardHeight):
            if board[head['x']][i] == boardTypes['Snake_Head'] or board[head['x']][i] == boardTypes['Snake_Body']:
                break
            else:
                distanceToBlockNorth = distanceToBlockNorth + 1

        distanceToBlockNorth = head['y'] + distanceToBlockNorth
        for i in range(aboveHead, distanceToBlockNorth):

            if not deadEndDetectedNorth:
                break

            canGoLeft = True
            canGoRight = True

            if leftOfHead < 0:
                canGoLeft = False
                print ("We are against the left wall")
            else:
                if board[leftOfHead][i] == boardTypes['Snake_Body'] or board[leftOfHead][i] == boardTypes['Snake_Head']:
                    canGoLeft = False
            if rightOfHead == len(board):
                canGoRight = False
                print ("We are against the right wall")
            else:
                if board[rightOfHead][i] == boardTypes['Snake_Body'] or board[rightOfHead][i] == boardTypes['Snake_Head']:
                    canGoRight = False

            if not canGoLeft and not canGoRight:
                deadEndDetectedNorth = True
            else:
                deadEndDetectedNorth = False

        # Check South

        for i in range(belowHead, -1, -1):

            if board[head['x']][i] == boardTypes['Snake_Head'] or board[head['x']][i] == boardTypes['Snake_Body']:
                break
            else:
                distanceToBlockSouth = distanceToBlockSouth + 1

        distanceToBlockSouth = head['y'] -distanceToBlockSouth
        for i in range(belowHead, distanceToBlockSouth -1, -1):

            if not deadEndDetectedSouth:
                break

            canGoLeft = True
            canGoRight = True

            if leftOfHead < 0:
                canGoLeft = False
                print ("We are against the left wall")
            else:
                if board[leftOfHead][i] == boardTypes['Snake_Body'] or board[leftOfHead][i] == boardTypes['Snake_Head']:
                    canGoLeft = False
            if rightOfHead == boardWidth:
                canGoRight = False
                print ("We are against the right wall")
            else:
                if board[rightOfHead][i] == boardTypes['Snake_Body'] or board[rightOfHead][i] == boardTypes['Snake_Head']:
                    canGoRight = False

            if not canGoLeft and not canGoRight:
                deadEndDetectedSouth = True
            else:
                deadEndDetectedSouth = False

        # Check East
        for i in range(rightOfHead, len(board)):

            if board[i][head['y']] == boardTypes['Snake_Head'] or board[i][head['y']] == boardTypes['Snake_Body']:
                break
            else:
                distanceToBlockEast = distanceToBlockEast + 1

        for i in range(rightOfHead, rightOfHead + distanceToBlockEast):
            if not deadEndDetectedEast:
                break

            canGoUp = True
            canGoDown = True

            if aboveHead == boardHeight:
                canGoUp = False
                print ("We are against the top wall")
            else:
                if board[i][aboveHead] == boardTypes['Snake_Body'] or board[i][aboveHead] == boardTypes['Snake_Head']:
                    canGoUp = False
            if belowHead < 0:
                canGoDown = False
                print ("We are against the bottom wall")
            else:
                if board[i][belowHead] == boardTypes['Snake_Body'] or board[i][belowHead] == boardTypes['Snake_Head']:
                    canGoDown = False

            if not canGoUp and not canGoDown:
                deadEndDetectedEast = True
            else:
                deadEndDetectedEast = False

        # Check West
        for i in range(leftOfHead, -1, -1):
            if board[i][head['y']] == boardTypes['Snake_Head'] or board[i][head['y']] == boardTypes['Snake_Body']:
                break
            else:
                distanceToBlockWest = distanceToBlockWest + 1

        distanceToBlockWest = head['x'] - distanceToBlockWest
        for i in range(leftOfHead, distanceToBlockWest - 1, -1):
            if not deadEndDetectedWest:
                break

            canGoUp = True
            canGoDown = True

            if aboveHead == boardHeight:
                canGoUp = False
                print ("We are against the top wall")
            else:
                if board[i][aboveHead] == boardTypes['Snake_Body'] or board[i][aboveHead] == boardTypes['Snake_Head']:
                    canGoUp = False
            if belowHead < 0:
                canGoDown = False
                print ("We are against the bottom wall")
            else:
                if board[i][belowHead] == boardTypes['Snake_Body'] or board[i][belowHead] == boardTypes['Snake_Head']:
                    canGoDown = False

            if not canGoUp and not canGoDown:
                deadEndDetectedWest = True
            else:
                deadEndDetectedWest = False

        if deadEndDetectedNorth:
            print ("Dead end detect North!!")
            direction.north = 0

        if deadEndDetectedSouth:
            print ("Dead end detect South!!")
            direction.south = 0

        if deadEndDetectedEast:
            print ("Dead end detect East!!")
            direction.east = 0

        if deadEndDetectedWest:
            print ("Dead end detect West!!")
            direction.west = 0

        return direction
