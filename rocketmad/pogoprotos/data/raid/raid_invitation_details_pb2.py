# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/raid/raid_invitation_details.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import raid_level_pb2 as pogoprotos_dot_enums_dot_raid__level__pb2
from pogoprotos.enums import pokemon_id_pb2 as pogoprotos_dot_enums_dot_pokemon__id__pb2
from pogoprotos.enums import form_pb2 as pogoprotos_dot_enums_dot_form__pb2
from pogoprotos.enums import team_color_pb2 as pogoprotos_dot_enums_dot_team__color__pb2
from pogoprotos.data.player import player_avatar_pb2 as pogoprotos_dot_data_dot_player_dot_player__avatar__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/raid/raid_invitation_details.proto',
  package='pogoprotos.data.raid',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n2pogoprotos/data/raid/raid_invitation_details.proto\x12\x14pogoprotos.data.raid\x1a!pogoprotos/enums/raid_level.proto\x1a!pogoprotos/enums/pokemon_id.proto\x1a\x1bpogoprotos/enums/form.proto\x1a!pogoprotos/enums/team_color.proto\x1a*pogoprotos/data/player/player_avatar.proto\"\xf2\x03\n\x15RaidInvitationDetails\x12\x0e\n\x06gym_id\x18\x01 \x01(\t\x12\x10\n\x08lobby_id\x18\x02 \x03(\x05\x12\x11\n\traid_seed\x18\x03 \x01(\x03\x12!\n\x19raid_invitation_expire_ms\x18\x04 \x01(\x03\x12/\n\nraid_level\x18\x05 \x01(\x0e\x32\x1b.pogoprotos.enums.RaidLevel\x12\x10\n\x08gym_name\x18\x06 \x01(\t\x12\x11\n\timage_url\x18\x07 \x01(\t\x12\x10\n\x08latitude\x18\x08 \x01(\x01\x12\x11\n\tlongitude\x18\t \x01(\x01\x12\x34\n\x0fraid_pokemon_id\x18\n \x01(\x0e\x32\x1b.pogoprotos.enums.PokemonId\x12\x31\n\x11raid_pokemon_form\x18\x0b \x01(\x0e\x32\x16.pogoprotos.enums.Form\x12\x12\n\ninviter_id\x18\x0c \x01(\t\x12\x18\n\x10inviter_nickname\x18\r \x01(\t\x12<\n\x0einviter_avatar\x18\x0e \x01(\x0b\x32$.pogoprotos.data.player.PlayerAvatar\x12\x31\n\x0cinviter_team\x18\x0f \x01(\x0e\x32\x1b.pogoprotos.enums.TeamColorb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_enums_dot_raid__level__pb2.DESCRIPTOR,pogoprotos_dot_enums_dot_pokemon__id__pb2.DESCRIPTOR,pogoprotos_dot_enums_dot_form__pb2.DESCRIPTOR,pogoprotos_dot_enums_dot_team__color__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_player_dot_player__avatar__pb2.DESCRIPTOR,])




_RAIDINVITATIONDETAILS = _descriptor.Descriptor(
  name='RaidInvitationDetails',
  full_name='pogoprotos.data.raid.RaidInvitationDetails',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gym_id', full_name='pogoprotos.data.raid.RaidInvitationDetails.gym_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lobby_id', full_name='pogoprotos.data.raid.RaidInvitationDetails.lobby_id', index=1,
      number=2, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='raid_seed', full_name='pogoprotos.data.raid.RaidInvitationDetails.raid_seed', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='raid_invitation_expire_ms', full_name='pogoprotos.data.raid.RaidInvitationDetails.raid_invitation_expire_ms', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='raid_level', full_name='pogoprotos.data.raid.RaidInvitationDetails.raid_level', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gym_name', full_name='pogoprotos.data.raid.RaidInvitationDetails.gym_name', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='image_url', full_name='pogoprotos.data.raid.RaidInvitationDetails.image_url', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='latitude', full_name='pogoprotos.data.raid.RaidInvitationDetails.latitude', index=7,
      number=8, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='pogoprotos.data.raid.RaidInvitationDetails.longitude', index=8,
      number=9, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='raid_pokemon_id', full_name='pogoprotos.data.raid.RaidInvitationDetails.raid_pokemon_id', index=9,
      number=10, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='raid_pokemon_form', full_name='pogoprotos.data.raid.RaidInvitationDetails.raid_pokemon_form', index=10,
      number=11, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='inviter_id', full_name='pogoprotos.data.raid.RaidInvitationDetails.inviter_id', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='inviter_nickname', full_name='pogoprotos.data.raid.RaidInvitationDetails.inviter_nickname', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='inviter_avatar', full_name='pogoprotos.data.raid.RaidInvitationDetails.inviter_avatar', index=13,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='inviter_team', full_name='pogoprotos.data.raid.RaidInvitationDetails.inviter_team', index=14,
      number=15, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=255,
  serialized_end=753,
)

_RAIDINVITATIONDETAILS.fields_by_name['raid_level'].enum_type = pogoprotos_dot_enums_dot_raid__level__pb2._RAIDLEVEL
_RAIDINVITATIONDETAILS.fields_by_name['raid_pokemon_id'].enum_type = pogoprotos_dot_enums_dot_pokemon__id__pb2._POKEMONID
_RAIDINVITATIONDETAILS.fields_by_name['raid_pokemon_form'].enum_type = pogoprotos_dot_enums_dot_form__pb2._FORM
_RAIDINVITATIONDETAILS.fields_by_name['inviter_avatar'].message_type = pogoprotos_dot_data_dot_player_dot_player__avatar__pb2._PLAYERAVATAR
_RAIDINVITATIONDETAILS.fields_by_name['inviter_team'].enum_type = pogoprotos_dot_enums_dot_team__color__pb2._TEAMCOLOR
DESCRIPTOR.message_types_by_name['RaidInvitationDetails'] = _RAIDINVITATIONDETAILS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RaidInvitationDetails = _reflection.GeneratedProtocolMessageType('RaidInvitationDetails', (_message.Message,), dict(
  DESCRIPTOR = _RAIDINVITATIONDETAILS,
  __module__ = 'pogoprotos.data.raid.raid_invitation_details_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.raid.RaidInvitationDetails)
  ))
_sym_db.RegisterMessage(RaidInvitationDetails)


# @@protoc_insertion_point(module_scope)