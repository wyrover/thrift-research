#!/usr/bin/env python2.6
# encoding: utf-8
# Author: guodongdong <dd.guo@foxmail.com>
# Created Time: 2014年01月17日 星期五 10时36分05秒
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from parser.ParseService import Client

import gevent
from gevent.threadpool import ThreadPool

#TODO: reconnect 
class ParserClient(object):
    def __init__(self, host='localhost', port=9999):
        self.extract_service_obj = None
        self.host = host
        self.port = port
        self.transport = TSocket.TSocket(self.host, self.port)
        protocol = TBinaryProtocol.TBinaryProtocol(self.transport)
        self.client = Client(protocol)
        self.transport.open()

    def Parse(self, url, document, cg):
        return self.client.Parse(url, document, cg)

    def Parse2(self, url, document, cg):
        return self.client.Parse2(url, document, cg)
   
def run():
    client = ParserClient()
    client.Parse("url", "document", "url")
    client.Parse2("url", "document", "url")
    client.transport.close()

if __name__ == "__main__":
    url = "url"
    document = "document"
    cg = "cg"

    import time
    start = time.time()
    thread_num = 1000
    total_num = 10000
    pool = ThreadPool(thread_num) 
    for i in xrange(total_num):
        print "spawn %s thread" % i
        pool.spawn(run)
    gevent.wait()
    end = time.time()
    print end-start
