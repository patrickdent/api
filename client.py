from __future__ import print_function
import logging

import grpc

import api_pb2
import api_pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = api_pb2_grpc.TesterStub(channel)
        response = stub.Test(api_pb2.TestRequest(value='marp'))
    print("Tester client received: " + response.message)


if __name__ == '__main__':
    logging.basicConfig()
    run()