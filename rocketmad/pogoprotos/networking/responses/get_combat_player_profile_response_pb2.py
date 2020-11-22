# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/get_combat_player_profile_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.combat import combat_player_profile_pb2 as pogoprotos_dot_data_dot_combat_dot_combat__player__profile__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/get_combat_player_profile_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nHpogoprotos/networking/responses/get_combat_player_profile_response.proto\x12\x1fpogoprotos.networking.responses\x1a\x32pogoprotos/data/combat/combat_player_profile.proto\"\x8d\x02\n\x1eGetCombatPlayerProfileResponse\x12V\n\x06result\x18\x01 \x01(\x0e\x32\x46.pogoprotos.networking.responses.GetCombatPlayerProfileResponse.Result\x12<\n\x07profile\x18\x02 \x01(\x0b\x32+.pogoprotos.data.combat.CombatPlayerProfile\"U\n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x1a\n\x16\x45RROR_PLAYER_NOT_FOUND\x10\x02\x12\x17\n\x13\x45RROR_ACCESS_DENIED\x10\x03\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_combat_dot_combat__player__profile__pb2.DESCRIPTOR,])



_GETCOMBATPLAYERPROFILERESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.networking.responses.GetCombatPlayerProfileResponse.Result',
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
      name='ERROR_PLAYER_NOT_FOUND', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_ACCESS_DENIED', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=346,
  serialized_end=431,
)
_sym_db.RegisterEnumDescriptor(_GETCOMBATPLAYERPROFILERESPONSE_RESULT)


_GETCOMBATPLAYERPROFILERESPONSE = _descriptor.Descriptor(
  name='GetCombatPlayerProfileResponse',
  full_name='pogoprotos.networking.responses.GetCombatPlayerProfileResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.networking.responses.GetCombatPlayerProfileResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='profile', full_name='pogoprotos.networking.responses.GetCombatPlayerProfileResponse.profile', index=1,
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
    _GETCOMBATPLAYERPROFILERESPONSE_RESULT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=162,
  serialized_end=431,
)

_GETCOMBATPLAYERPROFILERESPONSE.fields_by_name['result'].enum_type = _GETCOMBATPLAYERPROFILERESPONSE_RESULT
_GETCOMBATPLAYERPROFILERESPONSE.fields_by_name['profile'].message_type = pogoprotos_dot_data_dot_combat_dot_combat__player__profile__pb2._COMBATPLAYERPROFILE
_GETCOMBATPLAYERPROFILERESPONSE_RESULT.containing_type = _GETCOMBATPLAYERPROFILERESPONSE
DESCRIPTOR.message_types_by_name['GetCombatPlayerProfileResponse'] = _GETCOMBATPLAYERPROFILERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetCombatPlayerProfileResponse = _reflection.GeneratedProtocolMessageType('GetCombatPlayerProfileResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETCOMBATPLAYERPROFILERESPONSE,
  __module__ = 'pogoprotos.networking.responses.get_combat_player_profile_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.GetCombatPlayerProfileResponse)
  ))
_sym_db.RegisterMessage(GetCombatPlayerProfileResponse)


# @@protoc_insertion_point(module_scope)