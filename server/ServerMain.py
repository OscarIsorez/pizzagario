from SocketListener import SocketListener
from Player import Player
import time

class Main():
    def __init__(self):
        self.socketListener = SocketListener(self)
        self.players = {}

    def addPlayer(self, socket):
        self.players[socket] = Player()

    def removePlayer(self, socket):
        del self.players[socket]

    def setTarget(self, socket, x, y):
        self.players[socket].setTarget(x, y)

    def sendData(self):
        self.socketListener.sendData(self.players)

    def update(self):
        bots = self.players.values()
        for player in self.players.keys():
            if len(player.circles()) == 0:
                self.socketListener.serverManager.close(player)
                del self.players[player]
            else:
                self.players[player].update(bots)

if __name__ == "__main__":
    main = Main()
    continuer = True
    i=0
    while continuer:
        time.sleep(0.01)
        main.update()
        if i > 1:
            main.sendData()
            i = 0
        i+=0.01