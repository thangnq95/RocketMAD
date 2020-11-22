# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/enums/costume.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/enums/costume.proto',
  package='pogoprotos.enums',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1epogoprotos/enums/costume.proto\x12\x10pogoprotos.enums*\x88\x08\n\x07\x43ostume\x12\x11\n\rCOSTUME_UNSET\x10\x00\x12\x10\n\x0cHOLIDAY_2016\x10\x01\x12\x0f\n\x0b\x41NNIVERSARY\x10\x02\x12\x18\n\x14ONE_YEAR_ANNIVERSARY\x10\x03\x12\x12\n\x0eHALLOWEEN_2017\x10\x04\x12\x0f\n\x0bSUMMER_2018\x10\x05\x12\r\n\tFALL_2018\x10\x06\x12\x11\n\rNOVEMBER_2018\x10\x07\x12\x0f\n\x0bWINTER_2018\x10\x08\x12\x0c\n\x08\x46\x45\x42_2019\x10\t\x12\x15\n\x11MAY_2019_NOEVOLVE\x10\n\x12\x15\n\x11JAN_2020_NOEVOLVE\x10\x0b\x12\x17\n\x13\x41PRIL_2020_NOEVOLVE\x10\x0c\x12\x18\n\x14SAFARI_2020_NOEVOLVE\x10\r\x12\x18\n\x14SPRING_2020_NOEVOLVE\x10\x0e\x12\x18\n\x14SUMMER_2020_NOEVOLVE\x10\x0f\x12\x16\n\x12\x46\x41LL_2020_NOEVOLVE\x10\x10\x12\x18\n\x14WINTER_2020_NOEVOLVE\x10\x11\x12\x19\n\x15NOT_FOR_RELEASE_ALPHA\x10\x12\x12\x18\n\x14NOT_FOR_RELEASE_BETA\x10\x13\x12\x19\n\x15NOT_FOR_RELEASE_GAMMA\x10\x14\x12\x1c\n\x18NOT_FOR_RELEASE_NOEVOLVE\x10\x15\x12\x17\n\x13KANTO_2020_NOEVOLVE\x10\x16\x12\x17\n\x13JOHTO_2020_NOEVOLVE\x10\x17\x12\x17\n\x13HOENN_2020_NOEVOLVE\x10\x18\x12\x18\n\x14SINNOH_2020_NOEVOLVE\x10\x19\x12\x1b\n\x17HALLOWEEN_2020_NOEVOLVE\x10\x1a\x12\r\n\tCOSTUME_1\x10\x1b\x12\r\n\tCOSTUME_2\x10\x1c\x12\r\n\tCOSTUME_3\x10\x1d\x12\r\n\tCOSTUME_4\x10\x1e\x12\r\n\tCOSTUME_5\x10\x1f\x12\r\n\tCOSTUME_6\x10 \x12\r\n\tCOSTUME_7\x10!\x12\r\n\tCOSTUME_8\x10\"\x12\r\n\tCOSTUME_9\x10#\x12\x0e\n\nCOSTUME_10\x10$\x12\x17\n\x13\x43OSTUME_1_NO_EVOLVE\x10%\x12\x17\n\x13\x43OSTUME_2_NO_EVOLVE\x10&\x12\x17\n\x13\x43OSTUME_3_NO_EVOLVE\x10\'\x12\x17\n\x13\x43OSTUME_4_NO_EVOLVE\x10(\x12\x17\n\x13\x43OSTUME_5_NO_EVOLVE\x10)\x12\x17\n\x13\x43OSTUME_6_NO_EVOLVE\x10*\x12\x17\n\x13\x43OSTUME_7_NO_EVOLVE\x10+\x12\x17\n\x13\x43OSTUME_8_NO_EVOLVE\x10,\x12\x17\n\x13\x43OSTUME_9_NO_EVOLVE\x10-\x12\x18\n\x14\x43OSTUME_10_NO_EVOLVE\x10.b\x06proto3')
)

_COSTUME = _descriptor.EnumDescriptor(
  name='Costume',
  full_name='pogoprotos.enums.Costume',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='COSTUME_UNSET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HOLIDAY_2016', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ANNIVERSARY', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ONE_YEAR_ANNIVERSARY', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HALLOWEEN_2017', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUMMER_2018', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FALL_2018', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOVEMBER_2018', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WINTER_2018', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FEB_2019', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAY_2019_NOEVOLVE', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='JAN_2020_NOEVOLVE', index=11, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='APRIL_2020_NOEVOLVE', index=12, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SAFARI_2020_NOEVOLVE', index=13, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SPRING_2020_NOEVOLVE', index=14, number=14,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUMMER_2020_NOEVOLVE', index=15, number=15,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FALL_2020_NOEVOLVE', index=16, number=16,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WINTER_2020_NOEVOLVE', index=17, number=17,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOT_FOR_RELEASE_ALPHA', index=18, number=18,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOT_FOR_RELEASE_BETA', index=19, number=19,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOT_FOR_RELEASE_GAMMA', index=20, number=20,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOT_FOR_RELEASE_NOEVOLVE', index=21, number=21,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KANTO_2020_NOEVOLVE', index=22, number=22,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='JOHTO_2020_NOEVOLVE', index=23, number=23,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HOENN_2020_NOEVOLVE', index=24, number=24,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SINNOH_2020_NOEVOLVE', index=25, number=25,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HALLOWEEN_2020_NOEVOLVE', index=26, number=26,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COSTUME_1', index=27, number=27,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COSTUME_2', index=28, number=28,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COSTUME_3', index=29, number=29,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COSTUME_4', index=30, number=30,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COSTUME_5', index=31, number=31,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COSTUME_6', index=32, number=32,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COSTUME_7', index=33, number=33,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COSTUME_8', index=34, number=34,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COSTUME_9', index=35, number=35,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COSTUME_10', index=36, number=36,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COSTUME_1_NO_EVOLVE', index=37, number=37,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COSTUME_2_NO_EVOLVE', index=38, number=38,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COSTUME_3_NO_EVOLVE', index=39, number=39,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COSTUME_4_NO_EVOLVE', index=40, number=40,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COSTUME_5_NO_EVOLVE', index=41, number=41,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COSTUME_6_NO_EVOLVE', index=42, number=42,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COSTUME_7_NO_EVOLVE', index=43, number=43,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COSTUME_8_NO_EVOLVE', index=44, number=44,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COSTUME_9_NO_EVOLVE', index=45, number=45,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COSTUME_10_NO_EVOLVE', index=46, number=46,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=53,
  serialized_end=1085,
)
_sym_db.RegisterEnumDescriptor(_COSTUME)

Costume = enum_type_wrapper.EnumTypeWrapper(_COSTUME)
COSTUME_UNSET = 0
HOLIDAY_2016 = 1
ANNIVERSARY = 2
ONE_YEAR_ANNIVERSARY = 3
HALLOWEEN_2017 = 4
SUMMER_2018 = 5
FALL_2018 = 6
NOVEMBER_2018 = 7
WINTER_2018 = 8
FEB_2019 = 9
MAY_2019_NOEVOLVE = 10
JAN_2020_NOEVOLVE = 11
APRIL_2020_NOEVOLVE = 12
SAFARI_2020_NOEVOLVE = 13
SPRING_2020_NOEVOLVE = 14
SUMMER_2020_NOEVOLVE = 15
FALL_2020_NOEVOLVE = 16
WINTER_2020_NOEVOLVE = 17
NOT_FOR_RELEASE_ALPHA = 18
NOT_FOR_RELEASE_BETA = 19
NOT_FOR_RELEASE_GAMMA = 20
NOT_FOR_RELEASE_NOEVOLVE = 21
KANTO_2020_NOEVOLVE = 22
JOHTO_2020_NOEVOLVE = 23
HOENN_2020_NOEVOLVE = 24
SINNOH_2020_NOEVOLVE = 25
HALLOWEEN_2020_NOEVOLVE = 26
COSTUME_1 = 27
COSTUME_2 = 28
COSTUME_3 = 29
COSTUME_4 = 30
COSTUME_5 = 31
COSTUME_6 = 32
COSTUME_7 = 33
COSTUME_8 = 34
COSTUME_9 = 35
COSTUME_10 = 36
COSTUME_1_NO_EVOLVE = 37
COSTUME_2_NO_EVOLVE = 38
COSTUME_3_NO_EVOLVE = 39
COSTUME_4_NO_EVOLVE = 40
COSTUME_5_NO_EVOLVE = 41
COSTUME_6_NO_EVOLVE = 42
COSTUME_7_NO_EVOLVE = 43
COSTUME_8_NO_EVOLVE = 44
COSTUME_9_NO_EVOLVE = 45
COSTUME_10_NO_EVOLVE = 46


DESCRIPTOR.enum_types_by_name['Costume'] = _COSTUME
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)