from ServerManager import ServerManager

class SocketListener():
    def __init__(self, main):
        self.main = main
        self.id = 0
        self.socket_ids = {}
        self.clients = []
        self.serverManager = ServerManager(self)

    def newClient(self, socket):
        print("new client")
        self.clients.append(socket)
        self.socket_ids[socket] = self.id
        self.id += 1
        self.main.addPlayer(socket)

    def message(self, socket, event, msg):
        print(event + " : " + msg)
        if msg == "stopserver":
            self.serverManager.closeConnection()
        elif "," in msg:
            index = msg.index(",")
            self.main.setTarget(socket, int(msg[:index]), int(msg[index+1:]))

    def sendData(self, data):
        strdata = ""
        for socket in data:
            strdata += str(self.socket_ids[socket]) + ","

            circles = data[socket].circles
            for circle in circles:
                strdata += str(circle.size) + ","
                strdata += str(circle.x) + ","
                strdata += str(circle.y) + ","
            strdata += "|"
        for socket in self.clients:
            self.serverManager.send(socket, "msg", str(self.socket_ids[socket]) + "," + strdata)

    def disconnect(self, socket):
        self.main.removePlayer(socket)
        self.clients.remove(socket)
        del self.socket_ids[socket]
        print("client disconnect")

    def stop(self):
        print("the server has stoped")

if __name__ == "__main__":

    socketListener = SocketListener()
    serverManager = ServerManager(socketListener)
    continuer = True
    while continuer:
        pass
    serverManager.closeConnection()