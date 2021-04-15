import os
import random
import cherrypy
from walls import *
from utility import *
from snake import *
from food import *
from directions import *



class Battlesnake(object):
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def index(self):
        # This function is called when you register your Battlesnake on play.battlesnake.com
        # It controls your Battlesnake appearance and author permissions.
        # TIP: If you open your Battlesnake URL in browser you should see this data
        return {
            "apiversion": "1",
            "author": "Krunal",
            "color": "#37FFFF",
            "head": "silly",
            "tail": "bolt",
        }

    @cherrypy.expose
    @cherrypy.tools.json_in()
    def start(self):
        # This function is called everytime your snake is entered into a game.
        # cherrypy.request.json contains information about the game that's about to be played.
        data = cherrypy.request.json

        print("START")
        print(data)
        return "ok"

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def move(self):
        # This function is called on every turn of a game. It's how your snake decides where to move.
        # Valid moves are "up", "down", "left", or "right".
        # TODO: Use the information in cherrypy.request.json to decide your next move.
        data = cherrypy.request.json
        
        snakes = []
        for snake in data["board"]["snakes"]:
          snakes.append(Snake(snake))
        #print(snakes)

        mySnake = data['you']
        directions = Directions()
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("Direction in Starting= " , directions.toString())
        foods = Foods(data['board']['food'])
        #print("=================================")
        #print(foods)
        board = createBoardObject(data, snakes)
        #print("==================================")
        #print(board)
        directions = foods.goTowards(foods.amClosest(snakes, mySnake), directions, mySnake)
        print ("Direction After goTowards= " , directions.toString())
        # Check for collision
        walls = Walls()
        directions = walls.wallCollision(data, directions, mySnake)
        print ("Direction After wallCollision= " , directions.toString())
        directions = walls.snakeCollision(data, board, directions, mySnake)
        print ("Direction After snakeCollision= " , directions.toString())
        #Check for dead ends
        directions = walls.deadEndDetection(board, mySnake, directions)
        print ("Direction After deadEndDetection= " , directions.toString())
        ## Check for attack opportunities
        #Create temporary mySnake's Snake class object
        mySnakeClassObject = Snake(mySnake)
        directions = mySnakeClassObject.attack(directions, snakes)
        print ("Direction after Attack= " , directions.toString())
        #print ("Direction = " , directions.toString())
        move = directions.bestDirection()
        print(f"MOVE: {move}")
        return {"move": move}

    @cherrypy.expose
    @cherrypy.tools.json_in()
    def end(self):
        # This function is called when a game your snake was in ends.
        # It's purely for informational purposes, you don't have to make any decisions here.
        data = cherrypy.request.json

        print("END")
        return "ok"


if __name__ == "__main__":
    server = Battlesnake()
    cherrypy.config.update({"server.socket_host": "0.0.0.0"})
    cherrypy.config.update(
        {"server.socket_port": int(os.environ.get("PORT", "8080")), }
    )
    print("Starting Battlesnake Server...")
    cherrypy.quickstart(server)