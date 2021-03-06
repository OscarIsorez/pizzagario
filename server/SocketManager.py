import socket
import threading

class SocketManager(threading.Thread):
    def __init__(self, socketListener, stop, socket):
        threading.Thread.__init__(self)
        self._working = True
        self._socketListener = socketListener
        self._stop = stop

        self._socket = socket

        self.start()

    def run(self):
        while self._working:
            try:
                encodedData = self._socket.recv(1024)
            except:
                if self._working:
                    print("problème lors de la reception d'un message !")
                    self.closeConnection()
            if self._working:
                data = encodedData.decode("utf8")
                if "/" in data:
                    index = data.index("/")
                    event = data[:index]
                    donnee = data[index+1:]
                    self._socketListener.message(self._socket, event, donnee)
                else:
                    self.closeConnection()

    def isConnected(self):
        return self._working

    def closeConnection(self):
        if self._working:
            self._stop(self._socket)
            self._working = False
            self._socket.close()
            self._socketListener.disconnect(self._socket)

    def send(self, event, msg):
        if self._working:
            data = event + "/" + msg
            data = data.encode("utf8")
            try:
                self._socket.sendall(data)
            except:
                print("problème lors de l'envoie d'un message !")
                self.closeConnection()