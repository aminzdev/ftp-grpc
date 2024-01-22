#!/bin/python

import sys
from lib import FTPClient


def help_cmd(cmd: str):
    if cmd == "upload":
        print("upload file_path [options]")
        print("available options:")
        print("\t--server server_address")
        print("\t--port server_port")

    if cmd == "download":
        print("download file_path [options]")
        print("available options:")
        print("\t--server server_address")
        print("\t--port server_port")

    if cmd == "help":
        print("shows the usage message")


def upload_cmd(file_path: str, server: str, port: int):
    api = FTPClient().connect(server, port)
    api.upload(file_path)


def download_cmd(file_name: str, server: str, port: int):
    api = FTPClient().connect(server, port)
    api.download(file_name)


def main():
    if len(sys.argv) <= 2:
        print(f"usage: {sys.argv[0]} command")
        print(f"available commands:\n\tupload\n\tdownload\n\thelp")
    else:
        for i in sys.argv:
            match i:
                case "help":
                    command = sys.argv[sys.argv.index(i) + 1]
                    help_cmd(command)
                    return

                case "download":
                    file_name = sys.argv[sys.argv.index(i) + 1]
                    server = ""
                    port = 50051

                    for arg in sys.argv:
                        match arg:
                            case "--server":
                                server = sys.argv[sys.argv.index(arg) + 1]
                            case "--port":
                                port = int(sys.argv[sys.argv.index(arg) + 1])

                    print(f'downloading file "{file_name}" from {server}:{port}')
                    download_cmd(file_name, server, port)
                    return

                case "upload":
                    file_path = sys.argv[sys.argv.index(i) + 1]
                    server = ""
                    port = 50051

                    for arg in sys.argv:
                        match arg:
                            case "--server":
                                server = sys.argv[sys.argv.index(arg) + 1]
                            case "--port":
                                port = int(sys.argv[sys.argv.index(arg) + 1])

                    print(f'uploading file "{file_path}" to {server}:{port}')
                    upload_cmd(file_path, server, port)
                    return


if __name__ == '__main__':
    main()
