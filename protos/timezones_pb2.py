# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/timezones.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16protos/timezones.proto\"(\n\x08TimeZone\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x0e\n\x06offset\x18\x02 \x02(\x01\"\x14\n\x04Time\x12\x0c\n\x04time\x18\x01 \x02(\t\"\x07\n\x05\x45mpty2Q\n\tTimeZones\x12\x1d\n\x07getTime\x12\t.TimeZone\x1a\x05.Time\"\x00\x12%\n\x0cgetTimezones\x12\x06.Empty\x1a\t.TimeZone\"\x00\x30\x01')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.timezones_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _TIMEZONE._serialized_start=26
  _TIMEZONE._serialized_end=66
  _TIME._serialized_start=68
  _TIME._serialized_end=88
  _EMPTY._serialized_start=90
  _EMPTY._serialized_end=97
  _TIMEZONES._serialized_start=99
  _TIMEZONES._serialized_end=180
# @@protoc_insertion_point(module_scope)
