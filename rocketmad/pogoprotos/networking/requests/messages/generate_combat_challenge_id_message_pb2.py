# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/messages/generate_combat_challenge_id_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/requests/messages/generate_combat_challenge_id_message.proto',
  package='pogoprotos.networking.requests.messages',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nRpogoprotos/networking/requests/messages/generate_combat_challenge_id_message.proto\x12\'pogoprotos.networking.requests.messages\"\"\n GenerateCombatChallengeIdMessageb\x06proto3')
)




_GENERATECOMBATCHALLENGEIDMESSAGE = _descriptor.Descriptor(
  name='GenerateCombatChallengeIdMessage',
  full_name='pogoprotos.networking.requests.messages.GenerateCombatChallengeIdMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=127,
  serialized_end=161,
)

DESCRIPTOR.message_types_by_name['GenerateCombatChallengeIdMessage'] = _GENERATECOMBATCHALLENGEIDMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GenerateCombatChallengeIdMessage = _reflection.GeneratedProtocolMessageType('GenerateCombatChallengeIdMessage', (_message.Message,), dict(
  DESCRIPTOR = _GENERATECOMBATCHALLENGEIDMESSAGE,
  __module__ = 'pogoprotos.networking.requests.messages.generate_combat_challenge_id_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.messages.GenerateCombatChallengeIdMessage)
  ))
_sym_db.RegisterMessage(GenerateCombatChallengeIdMessage)


# @@protoc_insertion_point(module_scope)