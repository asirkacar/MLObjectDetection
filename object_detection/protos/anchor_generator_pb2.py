# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: object_detection/protos/anchor_generator.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from object_detection.protos import grid_anchor_generator_pb2 as object__detection_dot_protos_dot_grid__anchor__generator__pb2
from object_detection.protos import ssd_anchor_generator_pb2 as object__detection_dot_protos_dot_ssd__anchor__generator__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.object_detection/protos/anchor_generator.proto\x12\x17object_detection.protos\x1a\x33object_detection/protos/grid_anchor_generator.proto\x1a\x32object_detection/protos/ssd_anchor_generator.proto\"\xc7\x01\n\x0f\x41nchorGenerator\x12M\n\x15grid_anchor_generator\x18\x01 \x01(\x0b\x32,.object_detection.protos.GridAnchorGeneratorH\x00\x12K\n\x14ssd_anchor_generator\x18\x02 \x01(\x0b\x32+.object_detection.protos.SsdAnchorGeneratorH\x00\x42\x18\n\x16\x61nchor_generator_oneof')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'object_detection.protos.anchor_generator_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_ANCHORGENERATOR']._serialized_start=181
  _globals['_ANCHORGENERATOR']._serialized_end=380
# @@protoc_insertion_point(module_scope)
