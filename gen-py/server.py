#!/usr/bin/env python2.6
# encoding: utf-8
# Author: guodongdong <dd.guo@foxmail.com>
# Created Time: 2014年01月17日 星期五 10时11分51秒
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

from ServiceHandler import ParserServiceHandler 
from parser.ParseService import Processor


class Server(object):
    """main server module"""

    def start(self):
        port = 9999
        pfactory = TBinaryProtocol.TBinaryProtocolFactory()
        tfactory = TTransport.TBufferedTransportFactory()
        transport = TSocket.TServerSocket(port=port)
        handler = ParserServiceHandler()
        processor = Processor(handler)
        server = TServer.TThreadPoolServer(processor, transport, tfactory,
                pfactory, daemon=True)
        server.setNumThreads(2000)
        #server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)
        server.serve()

def main():
    server = Server()
    server.start()

if __name__ == "__main__":
    main()
