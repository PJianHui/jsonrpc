from . import rpcstub
import client

# mixin,多重继承
class RPCClient(client.Client, rpcstub.RPCStub):
    pass