# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/map/fort/sponsored_details.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/map/fort/sponsored_details.proto',
  package='pogoprotos.map.fort',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n+pogoprotos/map/fort/sponsored_details.proto\x12\x13pogoprotos.map.fort\"\x83\x04\n\x10SponsoredDetails\x12\x17\n\x0fpromo_image_url\x18\x01 \x03(\t\x12\x19\n\x11promo_description\x18\x02 \x03(\t\x12\x1b\n\x13\x63\x61ll_to_action_link\x18\x03 \x01(\t\x12_\n\x19promo_button_message_type\x18\x04 \x01(\x0e\x32<.pogoprotos.map.fort.SponsoredDetails.PromoButtonMessageType\x12\x13\n\x0b\x63\x61mpaign_id\x18\x05 \x01(\t\x12U\n\x14promo_image_creative\x18\x06 \x01(\x0b\x32\x37.pogoprotos.map.fort.SponsoredDetails.ImageTextCreative\x1a\x90\x01\n\x11ImageTextCreative\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x19\n\x11preview_image_url\x18\x04 \x01(\t\x12\x1c\n\x14\x66ullscreen_image_url\x18\x05 \x01(\t\x12\x10\n\x08\x63ta_link\x18\x06 \x01(\t\">\n\x16PromoButtonMessageType\x12\t\n\x05UNSET\x10\x00\x12\x0e\n\nLEARN_MORE\x10\x01\x12\t\n\x05OFFER\x10\x02\x62\x06proto3')
)



_SPONSOREDDETAILS_PROMOBUTTONMESSAGETYPE = _descriptor.EnumDescriptor(
  name='PromoButtonMessageType',
  full_name='pogoprotos.map.fort.SponsoredDetails.PromoButtonMessageType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LEARN_MORE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OFFER', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=522,
  serialized_end=584,
)
_sym_db.RegisterEnumDescriptor(_SPONSOREDDETAILS_PROMOBUTTONMESSAGETYPE)


_SPONSOREDDETAILS_IMAGETEXTCREATIVE = _descriptor.Descriptor(
  name='ImageTextCreative',
  full_name='pogoprotos.map.fort.SponsoredDetails.ImageTextCreative',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='pogoprotos.map.fort.SponsoredDetails.ImageTextCreative.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='title', full_name='pogoprotos.map.fort.SponsoredDetails.ImageTextCreative.title', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='pogoprotos.map.fort.SponsoredDetails.ImageTextCreative.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='preview_image_url', full_name='pogoprotos.map.fort.SponsoredDetails.ImageTextCreative.preview_image_url', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fullscreen_image_url', full_name='pogoprotos.map.fort.SponsoredDetails.ImageTextCreative.fullscreen_image_url', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cta_link', full_name='pogoprotos.map.fort.SponsoredDetails.ImageTextCreative.cta_link', index=5,
      number=6, type=9, cpp_type=9, label=1,
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
  serialized_start=376,
  serialized_end=520,
)

_SPONSOREDDETAILS = _descriptor.Descriptor(
  name='SponsoredDetails',
  full_name='pogoprotos.map.fort.SponsoredDetails',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='promo_image_url', full_name='pogoprotos.map.fort.SponsoredDetails.promo_image_url', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='promo_description', full_name='pogoprotos.map.fort.SponsoredDetails.promo_description', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='call_to_action_link', full_name='pogoprotos.map.fort.SponsoredDetails.call_to_action_link', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='promo_button_message_type', full_name='pogoprotos.map.fort.SponsoredDetails.promo_button_message_type', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='campaign_id', full_name='pogoprotos.map.fort.SponsoredDetails.campaign_id', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='promo_image_creative', full_name='pogoprotos.map.fort.SponsoredDetails.promo_image_creative', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SPONSOREDDETAILS_IMAGETEXTCREATIVE, ],
  enum_types=[
    _SPONSOREDDETAILS_PROMOBUTTONMESSAGETYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=69,
  serialized_end=584,
)

_SPONSOREDDETAILS_IMAGETEXTCREATIVE.containing_type = _SPONSOREDDETAILS
_SPONSOREDDETAILS.fields_by_name['promo_button_message_type'].enum_type = _SPONSOREDDETAILS_PROMOBUTTONMESSAGETYPE
_SPONSOREDDETAILS.fields_by_name['promo_image_creative'].message_type = _SPONSOREDDETAILS_IMAGETEXTCREATIVE
_SPONSOREDDETAILS_PROMOBUTTONMESSAGETYPE.containing_type = _SPONSOREDDETAILS
DESCRIPTOR.message_types_by_name['SponsoredDetails'] = _SPONSOREDDETAILS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SponsoredDetails = _reflection.GeneratedProtocolMessageType('SponsoredDetails', (_message.Message,), dict(

  ImageTextCreative = _reflection.GeneratedProtocolMessageType('ImageTextCreative', (_message.Message,), dict(
    DESCRIPTOR = _SPONSOREDDETAILS_IMAGETEXTCREATIVE,
    __module__ = 'pogoprotos.map.fort.sponsored_details_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.map.fort.SponsoredDetails.ImageTextCreative)
    ))
  ,
  DESCRIPTOR = _SPONSOREDDETAILS,
  __module__ = 'pogoprotos.map.fort.sponsored_details_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.map.fort.SponsoredDetails)
  ))
_sym_db.RegisterMessage(SponsoredDetails)
_sym_db.RegisterMessage(SponsoredDetails.ImageTextCreative)


# @@protoc_insertion_point(module_scope)