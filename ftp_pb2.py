# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ftp.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tftp.proto\x12\x03\x66tp\"\x1b\n\x0b\x44ownloadReq\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x0b\n\tUploadRes\"2\n\x04\x46ile\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06seq_no\x18\x02 \x01(\x05\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\x32W\n\x03\x46TP\x12%\n\x06Upload\x12\t.ftp.File\x1a\x0e.ftp.UploadRes(\x01\x12)\n\x08\x44ownload\x12\x10.ftp.DownloadReq\x1a\t.ftp.File0\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ftp_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_DOWNLOADREQ']._serialized_start=18
  _globals['_DOWNLOADREQ']._serialized_end=45
  _globals['_UPLOADRES']._serialized_start=47
  _globals['_UPLOADRES']._serialized_end=58
  _globals['_FILE']._serialized_start=60
  _globals['_FILE']._serialized_end=110
  _globals['_FTP']._serialized_start=112
  _globals['_FTP']._serialized_end=199
# @@protoc_insertion_point(module_scope)