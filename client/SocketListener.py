from Enemy import Enemy
from CircleEnemies import Circle

class SocketListener():
    def __init__(self, setPlayerDirection, player, bots, screen, cam):
        self.bots = bots # liste de bots
        self.ids = {} # id:bot
        self.player = player
        self.screen = screen
        self.cam = cam
        self.setPlayerDirection = setPlayerDirection

    def message(self, event, msg):
        print(event + " : " + msg)
        index = msg.index(",")
        self.id = msg[:index]
        msg = msg[index+1:]
        players = {} # id:[{size: x: y:}]
        while "|" in msg:
            index = msg.index("|")
            player_msg = msg[:index]
            msg = msg[index+1:]

            index = player_msg.index(",")
            id_player = player_msg[:index]
            players[id_player] = []

            player_msg = player_msg[index+1:]

            while len(player_msg) > 0:
                dico_circle = {}
                players[id_player].append(dico_circle)

                index = player_msg.index(",")
                dico_circle["size"] = player_msg[:index]
                player_msg = player_msg[index+1:]

                index = player_msg.index(",")
                dico_circle["x"] = player_msg[:index]
                player_msg = player_msg[index+1:]

                index = player_msg.index(",")
                dico_circle["y"] = player_msg[:index]
                player_msg = player_msg[index+1:]

        # supprimation des bots qui n'existent plus
        for id in self.ids.keys():
            if not id in players.keys():
                self.bots.remove(self.ids[id])
                del self.ids[id]

        # mise à jour du joueur principal
        self.player.update_circle(players[self.id])
        del players[self.id]

        # mise à jour des bots existant et création des nouveaux bots
        for id in players.keys():
            if id in self.ids.keys():
                enemy = self.ids[id]
                enemy.circles = []
            else:
                enemy = Enemy(self.screen, self.cam)
                self.ids[id] = enemy
                self.bots.append(enemy)

            for circle in players[id]:
                enemy.circles.append(Circle(float(circle["x"]), float(circle["y"]), int(circle["size"]), 0, 0))

        # send direction x and y
        self.setPlayerDirection()

    def stop(self):
        print("stop")

if __name__ == "__main__":
    from SocketManager import SocketManager
    socketListener = SocketListener()
    socketManager = SocketManager(socketListener)
    message = ""
    while message != "stop":
        message = input("enter stop to stop : ")
        if message == "split":
            socketManager.send("split", message)
        else:
            socketManager.send("msg", message)
    socketManager.closeConnection()