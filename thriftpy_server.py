#========================================
#    author: Changlong.Zang
#      mail: zclongpop123@163.com
#      time: Thu Nov 29 18:56:03 2018
#========================================
import thriftpy
from thriftpy.rpc import make_server
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
example_thrift = thriftpy.load("rpc_example.thrift", module_name="pp_thrift")


class ServerCore(object):
    '''
    '''
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



def main():
    server = make_server(example_thrift.example, ServerCore(),
                         '127.0.0.1', 6000)
    print("serving...")
    server.serve()


if __name__ == '__main__':
    main()
