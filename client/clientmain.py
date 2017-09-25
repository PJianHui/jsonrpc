from . import rpcclient

#mixin 的c，含有Client 和RPACStub 的属性和方法
c = rpcclient.RPCClient()
c.connect('127.0.0.1', 5000)
#在rpcstib中利用__getattr__实现send数据，从而在server端实现bar(1, 2, c=3)的调用
c.bar(1, 2, c=3)