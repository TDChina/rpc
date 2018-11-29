#========================================
#    author: Changlong.Zang
#      mail: zclongpop123@163.com
#      time: Thu Nov 29 18:58:56 2018
#========================================
import thriftpy
from thriftpy.rpc import client_context
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
def main():
    '''
    '''
    example_thrift = thriftpy.load("rpc_example.thrift", module_name="pp_thrift")

    with client_context(example_thrift.example, '127.0.0.1', 6000) as c:
        print c.ping()


if __name__ == '__main__':
    main()