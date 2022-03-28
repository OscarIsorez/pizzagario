
class SocketListener():
    def __init__(self):
        self.clients = []

    def newClient(self, socket):
        print("new client")
        self.clients.append(socket)

    def message(self, socket, event, msg):
        print(event + " : " + msg)
        if msg == "stopserver":
            global continuer
            continuer = False
        else:
            global serverManager
            for client in self.clients:
                serverManager.send(client, "msg", msg)

    def disconnect(self, socket):
        self.clients.remove(socket)
        print("client disconnect")

    def stop(self):
        print("the server has stoped")

if __name__ == "__main__":
    from ServerManager import ServerManager
    socketListener = SocketListener()
    serverManager = ServerManager(socketListener)
    continuer = True
    while continuer:
        pass
    serverManager.closeConnection()