# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='api.proto',
  package='api',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\tapi.proto\x12\x03\x61pi\"\x1c\n\x0bTestRequest\x12\r\n\x05value\x18\x01 \x01(\t\"\x1c\n\tTestReply\x12\x0f\n\x07message\x18\x01 \x01(\t24\n\x06Tester\x12*\n\x04Test\x12\x10.api.TestRequest\x1a\x0e.api.TestReply\"\x00\x62\x06proto3'
)




_TESTREQUEST = _descriptor.Descriptor(
  name='TestRequest',
  full_name='api.TestRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='api.TestRequest.value', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=46,
)


_TESTREPLY = _descriptor.Descriptor(
  name='TestReply',
  full_name='api.TestReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='api.TestReply.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=48,
  serialized_end=76,
)

DESCRIPTOR.message_types_by_name['TestRequest'] = _TESTREQUEST
DESCRIPTOR.message_types_by_name['TestReply'] = _TESTREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TestRequest = _reflection.GeneratedProtocolMessageType('TestRequest', (_message.Message,), {
  'DESCRIPTOR' : _TESTREQUEST,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:api.TestRequest)
  })
_sym_db.RegisterMessage(TestRequest)

TestReply = _reflection.GeneratedProtocolMessageType('TestReply', (_message.Message,), {
  'DESCRIPTOR' : _TESTREPLY,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:api.TestReply)
  })
_sym_db.RegisterMessage(TestReply)



_TESTER = _descriptor.ServiceDescriptor(
  name='Tester',
  full_name='api.Tester',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=78,
  serialized_end=130,
  methods=[
  _descriptor.MethodDescriptor(
    name='Test',
    full_name='api.Tester.Test',
    index=0,
    containing_service=None,
    input_type=_TESTREQUEST,
    output_type=_TESTREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_TESTER)

DESCRIPTOR.services_by_name['Tester'] = _TESTER

# @@protoc_insertion_point(module_scope)
