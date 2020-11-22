# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/master/map_buddy_settings.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/settings/master/map_buddy_settings.proto',
  package='pogoprotos.settings.master',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n3pogoprotos/settings/master/map_buddy_settings.proto\x12\x1apogoprotos.settings.master\"\xb2\x02\n\x10MapBuddySettings\x12\x1e\n\x16\x66or_buddy_group_number\x18\x01 \x01(\x05\x12\x19\n\x11target_offset_min\x18\x02 \x01(\x02\x12\x19\n\x11target_offset_max\x18\x03 \x01(\x02\x12\x16\n\x0eleash_distance\x18\x04 \x01(\x02\x12\x1b\n\x13max_seconds_to_idle\x18\x05 \x01(\x02\x12\x1a\n\x12max_rotation_speed\x18\x06 \x01(\x02\x12\x16\n\x0ewalk_threshold\x18\x07 \x01(\x02\x12\x15\n\rrun_threshold\x18\x08 \x01(\x02\x12\x14\n\x0cshould_glide\x18\t \x01(\x08\x12\x19\n\x11glide_smooth_time\x18\n \x01(\x02\x12\x17\n\x0fglide_max_speed\x18\x0b \x01(\x02\x62\x06proto3')
)




_MAPBUDDYSETTINGS = _descriptor.Descriptor(
  name='MapBuddySettings',
  full_name='pogoprotos.settings.master.MapBuddySettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='for_buddy_group_number', full_name='pogoprotos.settings.master.MapBuddySettings.for_buddy_group_number', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='target_offset_min', full_name='pogoprotos.settings.master.MapBuddySettings.target_offset_min', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='target_offset_max', full_name='pogoprotos.settings.master.MapBuddySettings.target_offset_max', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='leash_distance', full_name='pogoprotos.settings.master.MapBuddySettings.leash_distance', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_seconds_to_idle', full_name='pogoprotos.settings.master.MapBuddySettings.max_seconds_to_idle', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_rotation_speed', full_name='pogoprotos.settings.master.MapBuddySettings.max_rotation_speed', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='walk_threshold', full_name='pogoprotos.settings.master.MapBuddySettings.walk_threshold', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='run_threshold', full_name='pogoprotos.settings.master.MapBuddySettings.run_threshold', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='should_glide', full_name='pogoprotos.settings.master.MapBuddySettings.should_glide', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='glide_smooth_time', full_name='pogoprotos.settings.master.MapBuddySettings.glide_smooth_time', index=9,
      number=10, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='glide_max_speed', full_name='pogoprotos.settings.master.MapBuddySettings.glide_max_speed', index=10,
      number=11, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=84,
  serialized_end=390,
)

DESCRIPTOR.message_types_by_name['MapBuddySettings'] = _MAPBUDDYSETTINGS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MapBuddySettings = _reflection.GeneratedProtocolMessageType('MapBuddySettings', (_message.Message,), dict(
  DESCRIPTOR = _MAPBUDDYSETTINGS,
  __module__ = 'pogoprotos.settings.master.map_buddy_settings_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.settings.master.MapBuddySettings)
  ))
_sym_db.RegisterMessage(MapBuddySettings)


# @@protoc_insertion_point(module_scope)