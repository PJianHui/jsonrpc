from . import (tcpserver, jsondecode, rpcstub)

#mixin
class RPCServer(tcpserver.Server, jsondecode.JSONRPC, rpcstub.RPCStup):
    def __init__(self):
        super(RPCServer, self).__init__()

    def loop(self):
        self.bind_listen(5000)
        while True:
            self.accept_receive_close()

    def on_message(self, data):
        self.from_data(data)
        self.call_method()