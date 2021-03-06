# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/get_buddy_stats_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.buddy import buddy_observed_data_pb2 as pogoprotos_dot_data_dot_buddy_dot_buddy__observed__data__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/get_buddy_stats_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n>pogoprotos/networking/responses/get_buddy_stats_response.proto\x12\x1fpogoprotos.networking.responses\x1a/pogoprotos/data/buddy/buddy_observed_data.proto\"\xe4\x01\n\x15GetBuddyStatsResponse\x12M\n\x06result\x18\x01 \x01(\x0e\x32=.pogoprotos.networking.responses.GetBuddyStatsResponse.Result\x12?\n\robserved_data\x18\x02 \x01(\x0b\x32(.pogoprotos.data.buddy.BuddyObservedData\";\n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x19\n\x15\x45RROR_BUDDY_NOT_VALID\x10\x02\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_buddy_dot_buddy__observed__data__pb2.DESCRIPTOR,])



_GETBUDDYSTATSRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.networking.responses.GetBuddyStatsResponse.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_BUDDY_NOT_VALID', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=318,
  serialized_end=377,
)
_sym_db.RegisterEnumDescriptor(_GETBUDDYSTATSRESPONSE_RESULT)


_GETBUDDYSTATSRESPONSE = _descriptor.Descriptor(
  name='GetBuddyStatsResponse',
  full_name='pogoprotos.networking.responses.GetBuddyStatsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.networking.responses.GetBuddyStatsResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='observed_data', full_name='pogoprotos.networking.responses.GetBuddyStatsResponse.observed_data', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _GETBUDDYSTATSRESPONSE_RESULT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=149,
  serialized_end=377,
)

_GETBUDDYSTATSRESPONSE.fields_by_name['result'].enum_type = _GETBUDDYSTATSRESPONSE_RESULT
_GETBUDDYSTATSRESPONSE.fields_by_name['observed_data'].message_type = pogoprotos_dot_data_dot_buddy_dot_buddy__observed__data__pb2._BUDDYOBSERVEDDATA
_GETBUDDYSTATSRESPONSE_RESULT.containing_type = _GETBUDDYSTATSRESPONSE
DESCRIPTOR.message_types_by_name['GetBuddyStatsResponse'] = _GETBUDDYSTATSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetBuddyStatsResponse = _reflection.GeneratedProtocolMessageType('GetBuddyStatsResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETBUDDYSTATSRESPONSE,
  __module__ = 'pogoprotos.networking.responses.get_buddy_stats_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.GetBuddyStatsResponse)
  ))
_sym_db.RegisterMessage(GetBuddyStatsResponse)


# @@protoc_insertion_point(module_scope)
