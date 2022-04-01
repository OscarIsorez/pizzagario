from SocketListener import SocketListener
from Player import Player

class Main():
    def __init__(self):
        self.socketListener = SocketListener()
        self.players = {}

    def addPlayer(self, socket):
        self.players[socket] = Player()

    def removePlayer(self, socket):
        del self.players[socket]

    def setTarget(self, socket, x, y):
        self.players[socket].setTarget(x, y)

    def getData(self):
        return self.players

if __name__ == "__main__":
    main = Main()
    continuer = True
    while continuer:
        sleep(1)