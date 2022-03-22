import socket

class socketManager(threading.Thread):
    def __init__(self, main, conn):
        threading.Thread.__init__(self)
        self._main = main
        self._socket = conn
        self._receivedMsg = {"ok":None}
        self._working = True
        self.start()
        
    def run(self):
        while self._working:
            encodedData = self._socket.recv(1024)
            data = encodedData.decode("utf8")
            prefix = data[:2]
            donnee = data[2:]
            self._receivedMsg[prefix] = donnee
            if prefix == "an":
                rep = self._main.recvData(donnee)
                if rep != None:
                    rep = "ok" + rep
                else:
                    rep = "ok"
                rep = rep.encode("utf8")
                self._socket.sendall(rep)
                
            if not encodedData or prefix == "st":
                self.closeConnection()
    
    def isConnected(self):
        return self._working

    def closeConnection(self):
        if self._working:
            data = "st"
            data = data.encode("utf8")
            self._socket.sendall(data)
            self._socket.close()
            self._working = False
    
    def send(self, msg):
        if self._working:
            data = "an" + msg
            data = data.encode("utf8")
            self._socket.sendall(data)
            
            while self._receivedMsg["ok"] == None:
                pass
            rep = self._receivedMsg["ok"]
            self._receivedMsg["ok"] = None
            
            return rep
        else:
            return None