#========================================
#    author: Changlong.Zang
#      mail: zclongpop123@163.com
#      time: Thu Nov 29 18:33:42 2018
#========================================
import sys
sys.path.append('D:/work/rpc/gen-py')

from example import example
from thrift.server import TServer
from thrift.protocol import TBinaryProtocol
from thrift.transport import TSocket, TTransport
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+

class ExampleServer(object):
    def __init__(self):
        self.log = {}


    def ping(self):
        '''
        '''
        print 'got connect...'
        return 'Pong'


    def hello(self, name):
        '''
        '''
        print 'got user {0}'.format(name)
        return 'Hello {0}, how are you?'.format(name)


    def add(self, numberA, numberB):
        '''
        '''
        print 'got number {0} and {1}'.format(numberA, numberB)
        return numberA + numberB



if __name__ == '__main__':
    handler = ExampleServer()
    processor = example.Processor(handler)
    transport = TSocket.TServerSocket(host='127.0.0.1', port=9090)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)
    print('Starting the server...')
    server.serve()
    print('done.')


if __name__ == '__main__':
    main()
