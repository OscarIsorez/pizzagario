
class SocketListener():
    def __init__(self):
        pass

    def message(event, msg):
        print(event + " : " + msg)

    def stop():
        print("stop")

if __name__ == "__main__":
    from SocketManager import SocketManager
    socketManager = SocketManager(self)