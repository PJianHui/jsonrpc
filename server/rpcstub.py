#业务逻辑
class RPCStub(object):
    def __init__(self):
        pass

    def foo(self, a, b, c):
        print('foo:', a, b, c)

    def bar(self, a, b, c=10):
        print('bar:', a, b, c)