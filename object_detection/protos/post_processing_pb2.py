# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: object_detection/protos/post_processing.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-object_detection/protos/post_processing.proto\x12\x17object_detection.protos\"\x9a\x01\n\x16\x42\x61tchNonMaxSuppression\x12\x1a\n\x0fscore_threshold\x18\x01 \x01(\x02:\x01\x30\x12\x1a\n\riou_threshold\x18\x02 \x01(\x02:\x03\x30.6\x12%\n\x18max_detections_per_class\x18\x03 \x01(\x05:\x03\x31\x30\x30\x12!\n\x14max_total_detections\x18\x05 \x01(\x05:\x03\x31\x30\x30\"\x91\x02\n\x0ePostProcessing\x12R\n\x19\x62\x61tch_non_max_suppression\x18\x01 \x01(\x0b\x32/.object_detection.protos.BatchNonMaxSuppression\x12Y\n\x0fscore_converter\x18\x02 \x01(\x0e\x32\x36.object_detection.protos.PostProcessing.ScoreConverter:\x08IDENTITY\x12\x16\n\x0blogit_scale\x18\x03 \x01(\x02:\x01\x31\"8\n\x0eScoreConverter\x12\x0c\n\x08IDENTITY\x10\x00\x12\x0b\n\x07SIGMOID\x10\x01\x12\x0b\n\x07SOFTMAX\x10\x02')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'object_detection.protos.post_processing_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_BATCHNONMAXSUPPRESSION']._serialized_start=75
  _globals['_BATCHNONMAXSUPPRESSION']._serialized_end=229
  _globals['_POSTPROCESSING']._serialized_start=232
  _globals['_POSTPROCESSING']._serialized_end=505
  _globals['_POSTPROCESSING_SCORECONVERTER']._serialized_start=449
  _globals['_POSTPROCESSING_SCORECONVERTER']._serialized_end=505
# @@protoc_insertion_point(module_scope)
