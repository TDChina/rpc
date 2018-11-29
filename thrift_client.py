#========================================
#    author: Changlong.Zang
#      mail: zclongpop123@163.com
#      time: Tue Nov 13 15:03:20 2018
#========================================
import sys, time
sys.path.append('D:/work/rpc/gen-py')

from example import example
from thrift import Thrift
from thrift.protocol import TBinaryProtocol
from thrift.transport import TSocket, TTransport
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
def main():
    transport = TSocket.TSocket('127.0.0.1', 9090)
    transport = TTransport.TBufferedTransport(transport)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    client = example.Client(protocol)

    # Connect!
    transport.open()
    print client.ping()
    transport.close()


if __name__ == '__main__':
    main()
