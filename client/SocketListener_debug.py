
class SocketListener():
    def __init__(self):
        pass

    def message(self, event, msg):
        print(event + " : " + msg)

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