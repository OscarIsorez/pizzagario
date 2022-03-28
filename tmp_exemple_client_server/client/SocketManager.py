import socket
import threading

class SocketManager(threading.Thread):
    def __init__(self, socketListener, host="localhost", port=56248):
        threading.Thread.__init__(self)
        self._working = True
        self._socketListener = socketListener

        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self._socket.connect((host, port))
        except socket.error as msg:
            self._working = False
            print(msg)
            print("Connexion au serveur échoué...")

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
                    self._socketListener.message(event, donnee)
                else:
                    self.closeConnection()

    def isConnected(self):
        return self._working

    def closeConnection(self):
        if self._working:
            self._working = False
            self._socket.close()
            self._socketListener.stop()

    def send(self ,event, msg):
        '''l'event ne doit pas contenir de /'''
        if self._working:
            data = event + "/" + msg
            data = data.encode("utf8")
            self._socket.sendall(data)