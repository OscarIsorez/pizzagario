import socket
import threading
from SocketManager import SocketManager

class ServerManager(threading.Thread):
    def __init__(self, socketListener, port="56248"):
        threading.Thread.__init__(self)
        self._working = True
        self._socketListener = socketListener

        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.bind('', port)

        self._clients = {}

        self.start()

    def run(self):
        while self._working:
            self._socket.listen()
            socket, address = socket.accept()
            self._clients[socket] = SocketManager(self._socketListener, self._stop, socket)
            self._socketListener.newClient(socket)

    def isConnected(self):
        return self._working

    def closeConnection(self):
        if self._working:
            self._working = False
            for client in self._clients:
                client.closeConnection()
            self._socket.close()
            self._socketListener.stop()

    def send(self, socket, event, msg):
        '''l'event ne doit pas contenir de /'''
        self._clients[socket].send(event, msg)

    def _stop(self, socket):
        self._clients.pop(socket)