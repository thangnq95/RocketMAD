# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/master/pokemon_tag_settings.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import pokemon_tag_color_pb2 as pogoprotos_dot_enums_dot_pokemon__tag__color__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/settings/master/pokemon_tag_settings.proto',
  package='pogoprotos.settings.master',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n5pogoprotos/settings/master/pokemon_tag_settings.proto\x12\x1apogoprotos.settings.master\x1a(pogoprotos/enums/pokemon_tag_color.proto\"\xbe\x02\n\x12PokemonTagSettings\x12,\n$min_player_level_for_pokemon_tagging\x18\x01 \x01(\x05\x12\\\n\rcolor_binding\x18\x02 \x03(\x0b\x32\x45.pogoprotos.settings.master.PokemonTagSettings.PokemonTagColorBinding\x12\x1c\n\x14max_num_tags_allowed\x18\x03 \x01(\x05\x12 \n\x18tag_name_character_limit\x18\x04 \x01(\x05\x1a\\\n\x16PokemonTagColorBinding\x12\x30\n\x05\x63olor\x18\x01 \x01(\x0e\x32!.pogoprotos.enums.PokemonTagColor\x12\x10\n\x08hex_code\x18\x02 \x01(\tb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_enums_dot_pokemon__tag__color__pb2.DESCRIPTOR,])




_POKEMONTAGSETTINGS_POKEMONTAGCOLORBINDING = _descriptor.Descriptor(
  name='PokemonTagColorBinding',
  full_name='pogoprotos.settings.master.PokemonTagSettings.PokemonTagColorBinding',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='color', full_name='pogoprotos.settings.master.PokemonTagSettings.PokemonTagColorBinding.color', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hex_code', full_name='pogoprotos.settings.master.PokemonTagSettings.PokemonTagColorBinding.hex_code', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=354,
  serialized_end=446,
)

_POKEMONTAGSETTINGS = _descriptor.Descriptor(
  name='PokemonTagSettings',
  full_name='pogoprotos.settings.master.PokemonTagSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='min_player_level_for_pokemon_tagging', full_name='pogoprotos.settings.master.PokemonTagSettings.min_player_level_for_pokemon_tagging', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='color_binding', full_name='pogoprotos.settings.master.PokemonTagSettings.color_binding', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_num_tags_allowed', full_name='pogoprotos.settings.master.PokemonTagSettings.max_num_tags_allowed', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tag_name_character_limit', full_name='pogoprotos.settings.master.PokemonTagSettings.tag_name_character_limit', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_POKEMONTAGSETTINGS_POKEMONTAGCOLORBINDING, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=128,
  serialized_end=446,
)

_POKEMONTAGSETTINGS_POKEMONTAGCOLORBINDING.fields_by_name['color'].enum_type = pogoprotos_dot_enums_dot_pokemon__tag__color__pb2._POKEMONTAGCOLOR
_POKEMONTAGSETTINGS_POKEMONTAGCOLORBINDING.containing_type = _POKEMONTAGSETTINGS
_POKEMONTAGSETTINGS.fields_by_name['color_binding'].message_type = _POKEMONTAGSETTINGS_POKEMONTAGCOLORBINDING
DESCRIPTOR.message_types_by_name['PokemonTagSettings'] = _POKEMONTAGSETTINGS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PokemonTagSettings = _reflection.GeneratedProtocolMessageType('PokemonTagSettings', (_message.Message,), dict(

  PokemonTagColorBinding = _reflection.GeneratedProtocolMessageType('PokemonTagColorBinding', (_message.Message,), dict(
    DESCRIPTOR = _POKEMONTAGSETTINGS_POKEMONTAGCOLORBINDING,
    __module__ = 'pogoprotos.settings.master.pokemon_tag_settings_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.settings.master.PokemonTagSettings.PokemonTagColorBinding)
    ))
  ,
  DESCRIPTOR = _POKEMONTAGSETTINGS,
  __module__ = 'pogoprotos.settings.master.pokemon_tag_settings_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.settings.master.PokemonTagSettings)
  ))
_sym_db.RegisterMessage(PokemonTagSettings)
_sym_db.RegisterMessage(PokemonTagSettings.PokemonTagColorBinding)


# @@protoc_insertion_point(module_scope)
