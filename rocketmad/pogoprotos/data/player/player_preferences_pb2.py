# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/player/player_preferences.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/player/player_preferences.proto',
  package='pogoprotos.data.player',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n/pogoprotos/data/player/player_preferences.proto\x12\x16pogoprotos.data.player\"7\n\x11PlayerPreferences\x12\"\n\x1aopt_out_of_sponsored_gifts\x18\x01 \x01(\x08\x62\x06proto3')
)




_PLAYERPREFERENCES = _descriptor.Descriptor(
  name='PlayerPreferences',
  full_name='pogoprotos.data.player.PlayerPreferences',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='opt_out_of_sponsored_gifts', full_name='pogoprotos.data.player.PlayerPreferences.opt_out_of_sponsored_gifts', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=75,
  serialized_end=130,
)

DESCRIPTOR.message_types_by_name['PlayerPreferences'] = _PLAYERPREFERENCES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PlayerPreferences = _reflection.GeneratedProtocolMessageType('PlayerPreferences', (_message.Message,), dict(
  DESCRIPTOR = _PLAYERPREFERENCES,
  __module__ = 'pogoprotos.data.player.player_preferences_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.player.PlayerPreferences)
  ))
_sym_db.RegisterMessage(PlayerPreferences)


# @@protoc_insertion_point(module_scope)