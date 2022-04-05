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

    def split(self, socket):
        self.players[socket].split()

    def sendData(self):
        self.socketListener.sendData(self.players)

    def update(self):
        bots = self.players.values()
        tmp_sockets = list(self.players.keys())
        for player in tmp_sockets:
            if len(self.players[player].circles) == 0:
                self.socketListener.serverManager.close(player)
            else:
                self.players[player].update(bots)

    def stop():
        global continuer
        continuer = False

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