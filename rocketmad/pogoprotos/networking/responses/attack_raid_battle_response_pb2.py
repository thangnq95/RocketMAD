# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/attack_raid_battle_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.battle import battle_update_pb2 as pogoprotos_dot_data_dot_battle_dot_battle__update__pb2
from pogoprotos.data.vasa import ad_details_pb2 as pogoprotos_dot_data_dot_vasa_dot_ad__details__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/attack_raid_battle_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nApogoprotos/networking/responses/attack_raid_battle_response.proto\x12\x1fpogoprotos.networking.responses\x1a*pogoprotos/data/battle/battle_update.proto\x1a%pogoprotos/data/vasa/ad_details.proto\"\x98\x03\n\x18\x41ttackRaidBattleResponse\x12P\n\x06result\x18\x01 \x01(\x0e\x32@.pogoprotos.networking.responses.AttackRaidBattleResponse.Result\x12;\n\rbattle_update\x18\x02 \x01(\x0b\x32$.pogoprotos.data.battle.BattleUpdate\x12\x37\n\x0esponsored_gift\x18\x03 \x01(\x0b\x32\x1f.pogoprotos.data.vasa.AdDetails\"\xb3\x01\n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x17\n\x13\x45RROR_GYM_NOT_FOUND\x10\x02\x12\x1a\n\x16\x45RROR_BATTLE_NOT_FOUND\x10\x03\x12 \n\x1c\x45RROR_INVALID_ATTACK_ACTIONS\x10\x04\x12\x1c\n\x18\x45RROR_NOT_PART_OF_BATTLE\x10\x05\x12\x1c\n\x18\x45RROR_BATTLE_ID_NOT_RAID\x10\x06\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_battle_dot_battle__update__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_vasa_dot_ad__details__pb2.DESCRIPTOR,])



_ATTACKRAIDBATTLERESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.networking.responses.AttackRaidBattleResponse.Result',
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
      name='ERROR_GYM_NOT_FOUND', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_BATTLE_NOT_FOUND', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_INVALID_ATTACK_ACTIONS', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_NOT_PART_OF_BATTLE', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_BATTLE_ID_NOT_RAID', index=6, number=6,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=415,
  serialized_end=594,
)
_sym_db.RegisterEnumDescriptor(_ATTACKRAIDBATTLERESPONSE_RESULT)


_ATTACKRAIDBATTLERESPONSE = _descriptor.Descriptor(
  name='AttackRaidBattleResponse',
  full_name='pogoprotos.networking.responses.AttackRaidBattleResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.networking.responses.AttackRaidBattleResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='battle_update', full_name='pogoprotos.networking.responses.AttackRaidBattleResponse.battle_update', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sponsored_gift', full_name='pogoprotos.networking.responses.AttackRaidBattleResponse.sponsored_gift', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ATTACKRAIDBATTLERESPONSE_RESULT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=186,
  serialized_end=594,
)

_ATTACKRAIDBATTLERESPONSE.fields_by_name['result'].enum_type = _ATTACKRAIDBATTLERESPONSE_RESULT
_ATTACKRAIDBATTLERESPONSE.fields_by_name['battle_update'].message_type = pogoprotos_dot_data_dot_battle_dot_battle__update__pb2._BATTLEUPDATE
_ATTACKRAIDBATTLERESPONSE.fields_by_name['sponsored_gift'].message_type = pogoprotos_dot_data_dot_vasa_dot_ad__details__pb2._ADDETAILS
_ATTACKRAIDBATTLERESPONSE_RESULT.containing_type = _ATTACKRAIDBATTLERESPONSE
DESCRIPTOR.message_types_by_name['AttackRaidBattleResponse'] = _ATTACKRAIDBATTLERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AttackRaidBattleResponse = _reflection.GeneratedProtocolMessageType('AttackRaidBattleResponse', (_message.Message,), dict(
  DESCRIPTOR = _ATTACKRAIDBATTLERESPONSE,
  __module__ = 'pogoprotos.networking.responses.attack_raid_battle_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.AttackRaidBattleResponse)
  ))
_sym_db.RegisterMessage(AttackRaidBattleResponse)


# @@protoc_insertion_point(module_scope)