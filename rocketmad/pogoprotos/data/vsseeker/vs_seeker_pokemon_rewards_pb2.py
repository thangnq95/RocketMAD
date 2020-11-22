# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/vsseeker/vs_seeker_pokemon_rewards.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.vsseeker import vs_seeker_reward_track_pb2 as pogoprotos_dot_data_dot_vsseeker_dot_vs__seeker__reward__track__pb2
from pogoprotos.data.quests import quest_reward_pb2 as pogoprotos_dot_data_dot_quests_dot_quest__reward__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/vsseeker/vs_seeker_pokemon_rewards.proto',
  package='pogoprotos.data.vsseeker',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n8pogoprotos/data/vsseeker/vs_seeker_pokemon_rewards.proto\x12\x18pogoprotos.data.vsseeker\x1a\x35pogoprotos/data/vsseeker/vs_seeker_reward_track.proto\x1a)pogoprotos/data/quests/quest_reward.proto\"\x9c\n\n\x16VsSeekerPokemonRewards\x12Y\n\x11\x61vailable_pokemon\x18\x01 \x03(\x0b\x32>.pogoprotos.data.vsseeker.VsSeekerPokemonRewards.PokemonUnlock\x12\x43\n\x0creward_track\x18\x02 \x01(\x0e\x32-.pogoprotos.data.vsseeker.VsSeekerRewardTrack\x1a\xad\x01\n\x0fOverrideIvRange\x12W\n\x05range\x18\x01 \x01(\x0b\x32\x46.pogoprotos.data.vsseeker.VsSeekerPokemonRewards.OverrideIvRange.RangeH\x00\x12\x0e\n\x04zero\x18\x02 \x01(\x08H\x00\x1a!\n\x05Range\x12\x0b\n\x03min\x18\x01 \x01(\x03\x12\x0b\n\x03max\x18\x02 \x01(\x03\x42\x0e\n\x0cOverrideType\x1a\xb1\x07\n\rPokemonUnlock\x12M\n\x07pokemon\x18\x01 \x01(\x0b\x32:.pogoprotos.data.quests.QuestReward.PokemonEncounterRewardH\x00\x12\x85\x01\n\x16limited_pokemon_reward\x18\x02 \x01(\x0b\x32\x63.pogoprotos.data.vsseeker.VsSeekerPokemonRewards.PokemonUnlock.LimitedEditionPokemonEncounterRewardH\x00\x12\x90\x01\n!guaranteed_limited_pokemon_reward\x18\x03 \x01(\x0b\x32\x63.pogoprotos.data.vsseeker.VsSeekerPokemonRewards.PokemonUnlock.LimitedEditionPokemonEncounterRewardH\x00\x12\x18\n\x10unlocked_at_rank\x18\x04 \x01(\x05\x12\x0e\n\x06weight\x18\x05 \x01(\x02\x12\\\n\x12\x61ttack_iv_override\x18\x06 \x01(\x0b\x32@.pogoprotos.data.vsseeker.VsSeekerPokemonRewards.OverrideIvRange\x12]\n\x13\x64\x65\x66\x65nse_iv_override\x18\x07 \x01(\x0b\x32@.pogoprotos.data.vsseeker.VsSeekerPokemonRewards.OverrideIvRange\x12]\n\x13stamina_iv_override\x18\x08 \x01(\x0b\x32@.pogoprotos.data.vsseeker.VsSeekerPokemonRewards.OverrideIvRange\x1a\xe1\x01\n$LimitedEditionPokemonEncounterReward\x12K\n\x07pokemon\x18\x01 \x01(\x0b\x32:.pogoprotos.data.quests.QuestReward.PokemonEncounterReward\x12\x12\n\nidentifier\x18\x02 \x01(\t\x12\x1c\n\x12lifetime_max_count\x18\x03 \x01(\x05H\x00\x12\x31\n\'per_competitive_combat_season_max_count\x18\x04 \x01(\x05H\x00\x42\x07\n\x05LimitB\x0c\n\nRewardTypeb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_vsseeker_dot_vs__seeker__reward__track__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_quests_dot_quest__reward__pb2.DESCRIPTOR,])




_VSSEEKERPOKEMONREWARDS_OVERRIDEIVRANGE_RANGE = _descriptor.Descriptor(
  name='Range',
  full_name='pogoprotos.data.vsseeker.VsSeekerPokemonRewards.OverrideIvRange.Range',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='min', full_name='pogoprotos.data.vsseeker.VsSeekerPokemonRewards.OverrideIvRange.Range.min', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max', full_name='pogoprotos.data.vsseeker.VsSeekerPokemonRewards.OverrideIvRange.Range.max', index=1,
      number=2, type=3, cpp_type=2, label=1,
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
  serialized_start=496,
  serialized_end=529,
)

_VSSEEKERPOKEMONREWARDS_OVERRIDEIVRANGE = _descriptor.Descriptor(
  name='OverrideIvRange',
  full_name='pogoprotos.data.vsseeker.VsSeekerPokemonRewards.OverrideIvRange',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='range', full_name='pogoprotos.data.vsseeker.VsSeekerPokemonRewards.OverrideIvRange.range', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='zero', full_name='pogoprotos.data.vsseeker.VsSeekerPokemonRewards.OverrideIvRange.zero', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_VSSEEKERPOKEMONREWARDS_OVERRIDEIVRANGE_RANGE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='OverrideType', full_name='pogoprotos.data.vsseeker.VsSeekerPokemonRewards.OverrideIvRange.OverrideType',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=372,
  serialized_end=545,
)

_VSSEEKERPOKEMONREWARDS_POKEMONUNLOCK_LIMITEDEDITIONPOKEMONENCOUNTERREWARD = _descriptor.Descriptor(
  name='LimitedEditionPokemonEncounterReward',
  full_name='pogoprotos.data.vsseeker.VsSeekerPokemonRewards.PokemonUnlock.LimitedEditionPokemonEncounterReward',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pokemon', full_name='pogoprotos.data.vsseeker.VsSeekerPokemonRewards.PokemonUnlock.LimitedEditionPokemonEncounterReward.pokemon', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='identifier', full_name='pogoprotos.data.vsseeker.VsSeekerPokemonRewards.PokemonUnlock.LimitedEditionPokemonEncounterReward.identifier', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lifetime_max_count', full_name='pogoprotos.data.vsseeker.VsSeekerPokemonRewards.PokemonUnlock.LimitedEditionPokemonEncounterReward.lifetime_max_count', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='per_competitive_combat_season_max_count', full_name='pogoprotos.data.vsseeker.VsSeekerPokemonRewards.PokemonUnlock.LimitedEditionPokemonEncounterReward.per_competitive_combat_season_max_count', index=3,
      number=4, type=5, cpp_type=1, label=1,
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
    _descriptor.OneofDescriptor(
      name='Limit', full_name='pogoprotos.data.vsseeker.VsSeekerPokemonRewards.PokemonUnlock.LimitedEditionPokemonEncounterReward.Limit',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1254,
  serialized_end=1479,
)

_VSSEEKERPOKEMONREWARDS_POKEMONUNLOCK = _descriptor.Descriptor(
  name='PokemonUnlock',
  full_name='pogoprotos.data.vsseeker.VsSeekerPokemonRewards.PokemonUnlock',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pokemon', full_name='pogoprotos.data.vsseeker.VsSeekerPokemonRewards.PokemonUnlock.pokemon', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='limited_pokemon_reward', full_name='pogoprotos.data.vsseeker.VsSeekerPokemonRewards.PokemonUnlock.limited_pokemon_reward', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='guaranteed_limited_pokemon_reward', full_name='pogoprotos.data.vsseeker.VsSeekerPokemonRewards.PokemonUnlock.guaranteed_limited_pokemon_reward', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unlocked_at_rank', full_name='pogoprotos.data.vsseeker.VsSeekerPokemonRewards.PokemonUnlock.unlocked_at_rank', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='weight', full_name='pogoprotos.data.vsseeker.VsSeekerPokemonRewards.PokemonUnlock.weight', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='attack_iv_override', full_name='pogoprotos.data.vsseeker.VsSeekerPokemonRewards.PokemonUnlock.attack_iv_override', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='defense_iv_override', full_name='pogoprotos.data.vsseeker.VsSeekerPokemonRewards.PokemonUnlock.defense_iv_override', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stamina_iv_override', full_name='pogoprotos.data.vsseeker.VsSeekerPokemonRewards.PokemonUnlock.stamina_iv_override', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_VSSEEKERPOKEMONREWARDS_POKEMONUNLOCK_LIMITEDEDITIONPOKEMONENCOUNTERREWARD, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='RewardType', full_name='pogoprotos.data.vsseeker.VsSeekerPokemonRewards.PokemonUnlock.RewardType',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=548,
  serialized_end=1493,
)

_VSSEEKERPOKEMONREWARDS = _descriptor.Descriptor(
  name='VsSeekerPokemonRewards',
  full_name='pogoprotos.data.vsseeker.VsSeekerPokemonRewards',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='available_pokemon', full_name='pogoprotos.data.vsseeker.VsSeekerPokemonRewards.available_pokemon', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reward_track', full_name='pogoprotos.data.vsseeker.VsSeekerPokemonRewards.reward_track', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_VSSEEKERPOKEMONREWARDS_OVERRIDEIVRANGE, _VSSEEKERPOKEMONREWARDS_POKEMONUNLOCK, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=185,
  serialized_end=1493,
)

_VSSEEKERPOKEMONREWARDS_OVERRIDEIVRANGE_RANGE.containing_type = _VSSEEKERPOKEMONREWARDS_OVERRIDEIVRANGE
_VSSEEKERPOKEMONREWARDS_OVERRIDEIVRANGE.fields_by_name['range'].message_type = _VSSEEKERPOKEMONREWARDS_OVERRIDEIVRANGE_RANGE
_VSSEEKERPOKEMONREWARDS_OVERRIDEIVRANGE.containing_type = _VSSEEKERPOKEMONREWARDS
_VSSEEKERPOKEMONREWARDS_OVERRIDEIVRANGE.oneofs_by_name['OverrideType'].fields.append(
  _VSSEEKERPOKEMONREWARDS_OVERRIDEIVRANGE.fields_by_name['range'])
_VSSEEKERPOKEMONREWARDS_OVERRIDEIVRANGE.fields_by_name['range'].containing_oneof = _VSSEEKERPOKEMONREWARDS_OVERRIDEIVRANGE.oneofs_by_name['OverrideType']
_VSSEEKERPOKEMONREWARDS_OVERRIDEIVRANGE.oneofs_by_name['OverrideType'].fields.append(
  _VSSEEKERPOKEMONREWARDS_OVERRIDEIVRANGE.fields_by_name['zero'])
_VSSEEKERPOKEMONREWARDS_OVERRIDEIVRANGE.fields_by_name['zero'].containing_oneof = _VSSEEKERPOKEMONREWARDS_OVERRIDEIVRANGE.oneofs_by_name['OverrideType']
_VSSEEKERPOKEMONREWARDS_POKEMONUNLOCK_LIMITEDEDITIONPOKEMONENCOUNTERREWARD.fields_by_name['pokemon'].message_type = pogoprotos_dot_data_dot_quests_dot_quest__reward__pb2._QUESTREWARD_POKEMONENCOUNTERREWARD
_VSSEEKERPOKEMONREWARDS_POKEMONUNLOCK_LIMITEDEDITIONPOKEMONENCOUNTERREWARD.containing_type = _VSSEEKERPOKEMONREWARDS_POKEMONUNLOCK
_VSSEEKERPOKEMONREWARDS_POKEMONUNLOCK_LIMITEDEDITIONPOKEMONENCOUNTERREWARD.oneofs_by_name['Limit'].fields.append(
  _VSSEEKERPOKEMONREWARDS_POKEMONUNLOCK_LIMITEDEDITIONPOKEMONENCOUNTERREWARD.fields_by_name['lifetime_max_count'])
_VSSEEKERPOKEMONREWARDS_POKEMONUNLOCK_LIMITEDEDITIONPOKEMONENCOUNTERREWARD.fields_by_name['lifetime_max_count'].containing_oneof = _VSSEEKERPOKEMONREWARDS_POKEMONUNLOCK_LIMITEDEDITIONPOKEMONENCOUNTERREWARD.oneofs_by_name['Limit']
_VSSEEKERPOKEMONREWARDS_POKEMONUNLOCK_LIMITEDEDITIONPOKEMONENCOUNTERREWARD.oneofs_by_name['Limit'].fields.append(
  _VSSEEKERPOKEMONREWARDS_POKEMONUNLOCK_LIMITEDEDITIONPOKEMONENCOUNTERREWARD.fields_by_name['per_competitive_combat_season_max_count'])
_VSSEEKERPOKEMONREWARDS_POKEMONUNLOCK_LIMITEDEDITIONPOKEMONENCOUNTERREWARD.fields_by_name['per_competitive_combat_season_max_count'].containing_oneof = _VSSEEKERPOKEMONREWARDS_POKEMONUNLOCK_LIMITEDEDITIONPOKEMONENCOUNTERREWARD.oneofs_by_name['Limit']
_VSSEEKERPOKEMONREWARDS_POKEMONUNLOCK.fields_by_name['pokemon'].message_type = pogoprotos_dot_data_dot_quests_dot_quest__reward__pb2._QUESTREWARD_POKEMONENCOUNTERREWARD
_VSSEEKERPOKEMONREWARDS_POKEMONUNLOCK.fields_by_name['limited_pokemon_reward'].message_type = _VSSEEKERPOKEMONREWARDS_POKEMONUNLOCK_LIMITEDEDITIONPOKEMONENCOUNTERREWARD
_VSSEEKERPOKEMONREWARDS_POKEMONUNLOCK.fields_by_name['guaranteed_limited_pokemon_reward'].message_type = _VSSEEKERPOKEMONREWARDS_POKEMONUNLOCK_LIMITEDEDITIONPOKEMONENCOUNTERREWARD
_VSSEEKERPOKEMONREWARDS_POKEMONUNLOCK.fields_by_name['attack_iv_override'].message_type = _VSSEEKERPOKEMONREWARDS_OVERRIDEIVRANGE
_VSSEEKERPOKEMONREWARDS_POKEMONUNLOCK.fields_by_name['defense_iv_override'].message_type = _VSSEEKERPOKEMONREWARDS_OVERRIDEIVRANGE
_VSSEEKERPOKEMONREWARDS_POKEMONUNLOCK.fields_by_name['stamina_iv_override'].message_type = _VSSEEKERPOKEMONREWARDS_OVERRIDEIVRANGE
_VSSEEKERPOKEMONREWARDS_POKEMONUNLOCK.containing_type = _VSSEEKERPOKEMONREWARDS
_VSSEEKERPOKEMONREWARDS_POKEMONUNLOCK.oneofs_by_name['RewardType'].fields.append(
  _VSSEEKERPOKEMONREWARDS_POKEMONUNLOCK.fields_by_name['pokemon'])
_VSSEEKERPOKEMONREWARDS_POKEMONUNLOCK.fields_by_name['pokemon'].containing_oneof = _VSSEEKERPOKEMONREWARDS_POKEMONUNLOCK.oneofs_by_name['RewardType']
_VSSEEKERPOKEMONREWARDS_POKEMONUNLOCK.oneofs_by_name['RewardType'].fields.append(
  _VSSEEKERPOKEMONREWARDS_POKEMONUNLOCK.fields_by_name['limited_pokemon_reward'])
_VSSEEKERPOKEMONREWARDS_POKEMONUNLOCK.fields_by_name['limited_pokemon_reward'].containing_oneof = _VSSEEKERPOKEMONREWARDS_POKEMONUNLOCK.oneofs_by_name['RewardType']
_VSSEEKERPOKEMONREWARDS_POKEMONUNLOCK.oneofs_by_name['RewardType'].fields.append(
  _VSSEEKERPOKEMONREWARDS_POKEMONUNLOCK.fields_by_name['guaranteed_limited_pokemon_reward'])
_VSSEEKERPOKEMONREWARDS_POKEMONUNLOCK.fields_by_name['guaranteed_limited_pokemon_reward'].containing_oneof = _VSSEEKERPOKEMONREWARDS_POKEMONUNLOCK.oneofs_by_name['RewardType']
_VSSEEKERPOKEMONREWARDS.fields_by_name['available_pokemon'].message_type = _VSSEEKERPOKEMONREWARDS_POKEMONUNLOCK
_VSSEEKERPOKEMONREWARDS.fields_by_name['reward_track'].enum_type = pogoprotos_dot_data_dot_vsseeker_dot_vs__seeker__reward__track__pb2._VSSEEKERREWARDTRACK
DESCRIPTOR.message_types_by_name['VsSeekerPokemonRewards'] = _VSSEEKERPOKEMONREWARDS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

VsSeekerPokemonRewards = _reflection.GeneratedProtocolMessageType('VsSeekerPokemonRewards', (_message.Message,), dict(

  OverrideIvRange = _reflection.GeneratedProtocolMessageType('OverrideIvRange', (_message.Message,), dict(

    Range = _reflection.GeneratedProtocolMessageType('Range', (_message.Message,), dict(
      DESCRIPTOR = _VSSEEKERPOKEMONREWARDS_OVERRIDEIVRANGE_RANGE,
      __module__ = 'pogoprotos.data.vsseeker.vs_seeker_pokemon_rewards_pb2'
      # @@protoc_insertion_point(class_scope:pogoprotos.data.vsseeker.VsSeekerPokemonRewards.OverrideIvRange.Range)
      ))
    ,
    DESCRIPTOR = _VSSEEKERPOKEMONREWARDS_OVERRIDEIVRANGE,
    __module__ = 'pogoprotos.data.vsseeker.vs_seeker_pokemon_rewards_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.data.vsseeker.VsSeekerPokemonRewards.OverrideIvRange)
    ))
  ,

  PokemonUnlock = _reflection.GeneratedProtocolMessageType('PokemonUnlock', (_message.Message,), dict(

    LimitedEditionPokemonEncounterReward = _reflection.GeneratedProtocolMessageType('LimitedEditionPokemonEncounterReward', (_message.Message,), dict(
      DESCRIPTOR = _VSSEEKERPOKEMONREWARDS_POKEMONUNLOCK_LIMITEDEDITIONPOKEMONENCOUNTERREWARD,
      __module__ = 'pogoprotos.data.vsseeker.vs_seeker_pokemon_rewards_pb2'
      # @@protoc_insertion_point(class_scope:pogoprotos.data.vsseeker.VsSeekerPokemonRewards.PokemonUnlock.LimitedEditionPokemonEncounterReward)
      ))
    ,
    DESCRIPTOR = _VSSEEKERPOKEMONREWARDS_POKEMONUNLOCK,
    __module__ = 'pogoprotos.data.vsseeker.vs_seeker_pokemon_rewards_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.data.vsseeker.VsSeekerPokemonRewards.PokemonUnlock)
    ))
  ,
  DESCRIPTOR = _VSSEEKERPOKEMONREWARDS,
  __module__ = 'pogoprotos.data.vsseeker.vs_seeker_pokemon_rewards_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.vsseeker.VsSeekerPokemonRewards)
  ))
_sym_db.RegisterMessage(VsSeekerPokemonRewards)
_sym_db.RegisterMessage(VsSeekerPokemonRewards.OverrideIvRange)
_sym_db.RegisterMessage(VsSeekerPokemonRewards.OverrideIvRange.Range)
_sym_db.RegisterMessage(VsSeekerPokemonRewards.PokemonUnlock)
_sym_db.RegisterMessage(VsSeekerPokemonRewards.PokemonUnlock.LimitedEditionPokemonEncounterReward)


# @@protoc_insertion_point(module_scope)