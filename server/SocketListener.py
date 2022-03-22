
class SocketListener():
    def __init__(self):
        pass

    def newClient(socket):
        print("new client")

    def message(event, msg):
        print(event + " : " + msg)

    def disconnect(socket):
        print("client disconnect")

    def stop():
        print("the server has stoped")

if __name__ == "__main__":
    from SocketManager import SocketManager
    socketManager = SocketManager(self)