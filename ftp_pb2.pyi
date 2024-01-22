from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DownloadReq(_message.Message):
    __slots__ = ["name"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class UploadRes(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class File(_message.Message):
    __slots__ = ["name", "seq_no", "data"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SEQ_NO_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    name: str
    seq_no: int
    data: bytes
    def __init__(self, name: _Optional[str] = ..., seq_no: _Optional[int] = ..., data: _Optional[bytes] = ...) -> None: ...
