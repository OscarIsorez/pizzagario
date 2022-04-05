
class SocketListener():
    def __init__(self, player, bots):
        self.bots = bots
        self.ids = {}
        self.player = player

    def message(self, event, msg):
        print(event + " : " + msg)
        index = msg.index(",")
        self.id = msg[:index]
        msg = msg[index+1:]
        players = []
        while "|" in msg:
            index = msg.index("|")
            player = msg[:index]
            msg = msg[index+1:]
            
            dico = {}
            players.append(dico)
            index = player_msg.index(",")
            dico["id"] = player_msg[:index]
            player_msg = player_msg[index+1:]
            dico["circles"] = []
            while len(player_msg) > 0:
                dico_circle = {}
                dico["circles"].append(dico_circle)
                
                index = player_msg.index(",")
                dico_circle["size"] = player_msg[:index]
                player_msg = player_msg[index+1:]
                
                index = player_msg.index(",")
                dico_circle["x"] = player_msg[:index]
                player_msg = player_msg[index+1:]
                
                index = player_msg.index(",")
                dico_circle["y"] = player_msg[:index]
                player_msg = player_msg[index+1:]
        
        i = 0
        for identifiant in self.ids.keys():
            while identifiant != players[i]:
                self.bots.remove(self.ids[identifiant])
                del self.ids[identifiant]
            # actualiser le bot
            i += 1
        
        for j in range(i, len(players)):
            # créer des nouveaux bots
            pass

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