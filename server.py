from concurrent import futures

import grpc

import ftp_pb2_grpc as ftp_grpc
from lib import FTPService

ftp_server = grpc.server(futures.ThreadPoolExecutor(max_workers=16))
ftp_grpc.add_FTPServicer_to_server(FTPService(), ftp_server)
ftp_server.add_insecure_port('0.0.0.0:8080')
ftp_server.start()
ftp_server.wait_for_termination()
