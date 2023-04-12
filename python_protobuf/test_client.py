import grpc
import start_pb2
import start_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50052', options=(('grpc.enable_http_proxy', 0),)) as channel:
        stub = start_pb2_grpc.SquareRootServiceStub(channel)
        response = stub.squareRoot(start_pb2.Number(input=3))
        print(response.resulta)

if __name__=='__main__':
    run()