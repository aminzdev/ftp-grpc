from pathlib import Path

import grpc

import ftp_pb2 as ftp_pb2
import ftp_pb2_grpc as ftp_grpc


def read_in_chunks(file_object, chunk_size=1024):
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data


class FTPService(ftp_grpc.FTP):

    def Upload(self, request, context, **kwargs):
        req: ftp_pb2.File
        file_name = ""
        data = bytes()

        for req in request:
            file_name = req.name
            data += req.data

        with open(f'server_data/uploaded_data/{file_name}', "wb") as f:
            f.write(data)
        f.close()

        return ftp_pb2.UploadRes()

    def Download(self, request: ftp_pb2.DownloadReq, context, **kwargs):
        file_name = request.name
        file_path = f'server_data/download_src/{file_name}'

        if not Path(file_path).exists():
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(f'file "{file_name}" not found.')
            return

        seq_no = 0
        with open(file_path, "rb") as f:
            for data in read_in_chunks(f):
                seq_no += 1
                yield ftp_pb2.File(
                    name=file_name,
                    seq_no=seq_no,
                    data=data,
                )


class FTPClient(object):
    def __init__(self):
        self.stub: ftp_grpc.FTPStub | None = None
        self.channel = None
        self.host = None
        self.server_port = None

    def connect(self, host, port):
        self.host = host
        self.server_port = port
        # instantiate a channel
        self.channel = grpc.insecure_channel(f'{self.host}:{self.server_port}')

        # bind the client and the server
        self.stub = ftp_grpc.FTPStub(self.channel)

        return self

    def upload(self, file_path: str):
        data_chunks = []
        seq_no = 0
        with open(file_path, "rb") as f:
            for data in read_in_chunks(f):
                seq_no += 1
                data_chunks.append(
                    ftp_pb2.File(
                        name=f"{file_path.split('/')[-1]}",
                        seq_no=seq_no,
                        data=data,
                    )
                )

        self.stub.Upload(data_chunks.__iter__())

    def download(self, file_name: str):
        res = self.stub.Download(ftp_pb2.DownloadReq(name=file_name))

        file: ftp_pb2.File
        file_name = ""
        data = bytes()

        for file in res:
            file_name = file.name
            data += file.data

        with open(f"client_data/downloaded_data/{file_name}", "wb") as f:
            f.write(data)
        f.close()
