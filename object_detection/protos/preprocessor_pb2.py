# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: object_detection/protos/preprocessor.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*object_detection/protos/preprocessor.proto\x12\x17object_detection.protos\"\xaf\x10\n\x11PreprocessingStep\x12\x42\n\x0fnormalize_image\x18\x01 \x01(\x0b\x32\'.object_detection.protos.NormalizeImageH\x00\x12O\n\x16random_horizontal_flip\x18\x02 \x01(\x0b\x32-.object_detection.protos.RandomHorizontalFlipH\x00\x12R\n\x18random_pixel_value_scale\x18\x03 \x01(\x0b\x32..object_detection.protos.RandomPixelValueScaleH\x00\x12G\n\x12random_image_scale\x18\x04 \x01(\x0b\x32).object_detection.protos.RandomImageScaleH\x00\x12\x46\n\x12random_rgb_to_gray\x18\x05 \x01(\x0b\x32(.object_detection.protos.RandomRGBtoGrayH\x00\x12S\n\x18random_adjust_brightness\x18\x06 \x01(\x0b\x32/.object_detection.protos.RandomAdjustBrightnessH\x00\x12O\n\x16random_adjust_contrast\x18\x07 \x01(\x0b\x32-.object_detection.protos.RandomAdjustContrastH\x00\x12\x45\n\x11random_adjust_hue\x18\x08 \x01(\x0b\x32(.object_detection.protos.RandomAdjustHueH\x00\x12S\n\x18random_adjust_saturation\x18\t \x01(\x0b\x32/.object_detection.protos.RandomAdjustSaturationH\x00\x12K\n\x14random_distort_color\x18\n \x01(\x0b\x32+.object_detection.protos.RandomDistortColorH\x00\x12I\n\x13random_jitter_boxes\x18\x0b \x01(\x0b\x32*.object_detection.protos.RandomJitterBoxesH\x00\x12\x45\n\x11random_crop_image\x18\x0c \x01(\x0b\x32(.object_detection.protos.RandomCropImageH\x00\x12\x43\n\x10random_pad_image\x18\r \x01(\x0b\x32\'.object_detection.protos.RandomPadImageH\x00\x12L\n\x15random_crop_pad_image\x18\x0e \x01(\x0b\x32+.object_detection.protos.RandomCropPadImageH\x00\x12W\n\x1brandom_crop_to_aspect_ratio\x18\x0f \x01(\x0b\x32\x30.object_detection.protos.RandomCropToAspectRatioH\x00\x12K\n\x14random_black_patches\x18\x10 \x01(\x0b\x32+.object_detection.protos.RandomBlackPatchesH\x00\x12K\n\x14random_resize_method\x18\x11 \x01(\x0b\x32+.object_detection.protos.RandomResizeMethodH\x00\x12\x61\n scale_boxes_to_pixel_coordinates\x18\x12 \x01(\x0b\x32\x35.object_detection.protos.ScaleBoxesToPixelCoordinatesH\x00\x12<\n\x0cresize_image\x18\x13 \x01(\x0b\x32$.object_detection.protos.ResizeImageH\x00\x12M\n\x15subtract_channel_mean\x18\x14 \x01(\x0b\x32,.object_detection.protos.SubtractChannelMeanH\x00\x12\x41\n\x0fssd_random_crop\x18\x15 \x01(\x0b\x32&.object_detection.protos.SSDRandomCropH\x00\x12H\n\x13ssd_random_crop_pad\x18\x16 \x01(\x0b\x32).object_detection.protos.SSDRandomCropPadH\x00\x12\x64\n\"ssd_random_crop_fixed_aspect_ratio\x18\x17 \x01(\x0b\x32\x36.object_detection.protos.SSDRandomCropFixedAspectRatioH\x00\x12k\n&ssd_random_crop_pad_fixed_aspect_ratio\x18\x18 \x01(\x0b\x32\x39.object_detection.protos.SSDRandomCropPadFixedAspectRatioH\x00\x12K\n\x14random_vertical_flip\x18\x19 \x01(\x0b\x32+.object_detection.protos.RandomVerticalFlipH\x00\x12\x46\n\x11random_rotation90\x18\x1a \x01(\x0b\x32).object_detection.protos.RandomRotation90H\x00\x42\x14\n\x12preprocessing_step\"v\n\x0eNormalizeImage\x12\x17\n\x0foriginal_minval\x18\x01 \x01(\x02\x12\x17\n\x0foriginal_maxval\x18\x02 \x01(\x02\x12\x18\n\rtarget_minval\x18\x03 \x01(\x02:\x01\x30\x12\x18\n\rtarget_maxval\x18\x04 \x01(\x02:\x01\x31\"9\n\x14RandomHorizontalFlip\x12!\n\x19keypoint_flip_permutation\x18\x01 \x03(\x05\"7\n\x12RandomVerticalFlip\x12!\n\x19keypoint_flip_permutation\x18\x01 \x03(\x05\"\x12\n\x10RandomRotation90\"A\n\x15RandomPixelValueScale\x12\x13\n\x06minval\x18\x01 \x01(\x02:\x03\x30.9\x12\x13\n\x06maxval\x18\x02 \x01(\x02:\x03\x31.1\"L\n\x10RandomImageScale\x12\x1c\n\x0fmin_scale_ratio\x18\x01 \x01(\x02:\x03\x30.5\x12\x1a\n\x0fmax_scale_ratio\x18\x02 \x01(\x02:\x01\x32\"+\n\x0fRandomRGBtoGray\x12\x18\n\x0bprobability\x18\x01 \x01(\x02:\x03\x30.1\"0\n\x16RandomAdjustBrightness\x12\x16\n\tmax_delta\x18\x01 \x01(\x02:\x03\x30.2\"G\n\x14RandomAdjustContrast\x12\x16\n\tmin_delta\x18\x01 \x01(\x02:\x03\x30.8\x12\x17\n\tmax_delta\x18\x02 \x01(\x02:\x04\x31.25\"*\n\x0fRandomAdjustHue\x12\x17\n\tmax_delta\x18\x01 \x01(\x02:\x04\x30.02\"I\n\x16RandomAdjustSaturation\x12\x16\n\tmin_delta\x18\x01 \x01(\x02:\x03\x30.8\x12\x17\n\tmax_delta\x18\x02 \x01(\x02:\x04\x31.25\",\n\x12RandomDistortColor\x12\x16\n\x0e\x63olor_ordering\x18\x01 \x01(\x05\"(\n\x11RandomJitterBoxes\x12\x13\n\x05ratio\x18\x01 \x01(\x02:\x04\x30.05\"\xd1\x01\n\x0fRandomCropImage\x12\x1d\n\x12min_object_covered\x18\x01 \x01(\x02:\x01\x31\x12\x1e\n\x10min_aspect_ratio\x18\x02 \x01(\x02:\x04\x30.75\x12\x1e\n\x10max_aspect_ratio\x18\x03 \x01(\x02:\x04\x31.33\x12\x15\n\x08min_area\x18\x04 \x01(\x02:\x03\x30.1\x12\x13\n\x08max_area\x18\x05 \x01(\x02:\x01\x31\x12\x1b\n\x0eoverlap_thresh\x18\x06 \x01(\x02:\x03\x30.3\x12\x16\n\x0brandom_coef\x18\x07 \x01(\x02:\x01\x30\"\x89\x01\n\x0eRandomPadImage\x12\x18\n\x10min_image_height\x18\x01 \x01(\x02\x12\x17\n\x0fmin_image_width\x18\x02 \x01(\x02\x12\x18\n\x10max_image_height\x18\x03 \x01(\x02\x12\x17\n\x0fmax_image_width\x18\x04 \x01(\x02\x12\x11\n\tpad_color\x18\x05 \x03(\x02\"\xa5\x02\n\x12RandomCropPadImage\x12\x1d\n\x12min_object_covered\x18\x01 \x01(\x02:\x01\x31\x12\x1e\n\x10min_aspect_ratio\x18\x02 \x01(\x02:\x04\x30.75\x12\x1e\n\x10max_aspect_ratio\x18\x03 \x01(\x02:\x04\x31.33\x12\x15\n\x08min_area\x18\x04 \x01(\x02:\x03\x30.1\x12\x13\n\x08max_area\x18\x05 \x01(\x02:\x01\x31\x12\x1b\n\x0eoverlap_thresh\x18\x06 \x01(\x02:\x03\x30.3\x12\x16\n\x0brandom_coef\x18\x07 \x01(\x02:\x01\x30\x12\x1d\n\x15min_padded_size_ratio\x18\x08 \x03(\x02\x12\x1d\n\x15max_padded_size_ratio\x18\t \x03(\x02\x12\x11\n\tpad_color\x18\n \x03(\x02\"O\n\x17RandomCropToAspectRatio\x12\x17\n\x0c\x61spect_ratio\x18\x01 \x01(\x02:\x01\x31\x12\x1b\n\x0eoverlap_thresh\x18\x02 \x01(\x02:\x03\x30.3\"o\n\x12RandomBlackPatches\x12\x1d\n\x11max_black_patches\x18\x01 \x01(\x05:\x02\x31\x30\x12\x18\n\x0bprobability\x18\x02 \x01(\x02:\x03\x30.5\x12 \n\x13size_to_image_ratio\x18\x03 \x01(\x02:\x03\x30.1\"A\n\x12RandomResizeMethod\x12\x15\n\rtarget_height\x18\x01 \x01(\x02\x12\x14\n\x0ctarget_width\x18\x02 \x01(\x02\"\x1e\n\x1cScaleBoxesToPixelCoordinates\"\xc0\x01\n\x0bResizeImage\x12\x12\n\nnew_height\x18\x01 \x01(\x05\x12\x11\n\tnew_width\x18\x02 \x01(\x05\x12\x45\n\x06method\x18\x03 \x01(\x0e\x32+.object_detection.protos.ResizeImage.Method:\x08\x42ILINEAR\"C\n\x06Method\x12\x08\n\x04\x41REA\x10\x01\x12\x0b\n\x07\x42ICUBIC\x10\x02\x12\x0c\n\x08\x42ILINEAR\x10\x03\x12\x14\n\x10NEAREST_NEIGHBOR\x10\x04\"$\n\x13SubtractChannelMean\x12\r\n\x05means\x18\x01 \x03(\x02\"\xb9\x01\n\x16SSDRandomCropOperation\x12\x1a\n\x12min_object_covered\x18\x01 \x01(\x02\x12\x18\n\x10min_aspect_ratio\x18\x02 \x01(\x02\x12\x18\n\x10max_aspect_ratio\x18\x03 \x01(\x02\x12\x10\n\x08min_area\x18\x04 \x01(\x02\x12\x10\n\x08max_area\x18\x05 \x01(\x02\x12\x16\n\x0eoverlap_thresh\x18\x06 \x01(\x02\x12\x13\n\x0brandom_coef\x18\x07 \x01(\x02\"T\n\rSSDRandomCrop\x12\x43\n\noperations\x18\x01 \x03(\x0b\x32/.object_detection.protos.SSDRandomCropOperation\"\xb9\x02\n\x19SSDRandomCropPadOperation\x12\x1a\n\x12min_object_covered\x18\x01 \x01(\x02\x12\x18\n\x10min_aspect_ratio\x18\x02 \x01(\x02\x12\x18\n\x10max_aspect_ratio\x18\x03 \x01(\x02\x12\x10\n\x08min_area\x18\x04 \x01(\x02\x12\x10\n\x08max_area\x18\x05 \x01(\x02\x12\x16\n\x0eoverlap_thresh\x18\x06 \x01(\x02\x12\x13\n\x0brandom_coef\x18\x07 \x01(\x02\x12\x1d\n\x15min_padded_size_ratio\x18\x08 \x03(\x02\x12\x1d\n\x15max_padded_size_ratio\x18\t \x03(\x02\x12\x13\n\x0bpad_color_r\x18\n \x01(\x02\x12\x13\n\x0bpad_color_g\x18\x0b \x01(\x02\x12\x13\n\x0bpad_color_b\x18\x0c \x01(\x02\"Z\n\x10SSDRandomCropPad\x12\x46\n\noperations\x18\x01 \x03(\x0b\x32\x32.object_detection.protos.SSDRandomCropPadOperation\"\x95\x01\n&SSDRandomCropFixedAspectRatioOperation\x12\x1a\n\x12min_object_covered\x18\x01 \x01(\x02\x12\x10\n\x08min_area\x18\x04 \x01(\x02\x12\x10\n\x08max_area\x18\x05 \x01(\x02\x12\x16\n\x0eoverlap_thresh\x18\x06 \x01(\x02\x12\x13\n\x0brandom_coef\x18\x07 \x01(\x02\"\x8d\x01\n\x1dSSDRandomCropFixedAspectRatio\x12S\n\noperations\x18\x01 \x03(\x0b\x32?.object_detection.protos.SSDRandomCropFixedAspectRatioOperation\x12\x17\n\x0c\x61spect_ratio\x18\x02 \x01(\x02:\x01\x31\"\x8a\x02\n)SSDRandomCropPadFixedAspectRatioOperation\x12\x1a\n\x12min_object_covered\x18\x01 \x01(\x02\x12\x18\n\x10min_aspect_ratio\x18\x02 \x01(\x02\x12\x18\n\x10max_aspect_ratio\x18\x03 \x01(\x02\x12\x10\n\x08min_area\x18\x04 \x01(\x02\x12\x10\n\x08max_area\x18\x05 \x01(\x02\x12\x16\n\x0eoverlap_thresh\x18\x06 \x01(\x02\x12\x13\n\x0brandom_coef\x18\x07 \x01(\x02\x12\x1d\n\x15min_padded_size_ratio\x18\x08 \x03(\x02\x12\x1d\n\x15max_padded_size_ratio\x18\t \x03(\x02\"\x93\x01\n SSDRandomCropPadFixedAspectRatio\x12V\n\noperations\x18\x01 \x03(\x0b\x32\x42.object_detection.protos.SSDRandomCropPadFixedAspectRatioOperation\x12\x17\n\x0c\x61spect_ratio\x18\x02 \x01(\x02:\x01\x31')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'object_detection.protos.preprocessor_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_PREPROCESSINGSTEP']._serialized_start=72
  _globals['_PREPROCESSINGSTEP']._serialized_end=2167
  _globals['_NORMALIZEIMAGE']._serialized_start=2169
  _globals['_NORMALIZEIMAGE']._serialized_end=2287
  _globals['_RANDOMHORIZONTALFLIP']._serialized_start=2289
  _globals['_RANDOMHORIZONTALFLIP']._serialized_end=2346
  _globals['_RANDOMVERTICALFLIP']._serialized_start=2348
  _globals['_RANDOMVERTICALFLIP']._serialized_end=2403
  _globals['_RANDOMROTATION90']._serialized_start=2405
  _globals['_RANDOMROTATION90']._serialized_end=2423
  _globals['_RANDOMPIXELVALUESCALE']._serialized_start=2425
  _globals['_RANDOMPIXELVALUESCALE']._serialized_end=2490
  _globals['_RANDOMIMAGESCALE']._serialized_start=2492
  _globals['_RANDOMIMAGESCALE']._serialized_end=2568
  _globals['_RANDOMRGBTOGRAY']._serialized_start=2570
  _globals['_RANDOMRGBTOGRAY']._serialized_end=2613
  _globals['_RANDOMADJUSTBRIGHTNESS']._serialized_start=2615
  _globals['_RANDOMADJUSTBRIGHTNESS']._serialized_end=2663
  _globals['_RANDOMADJUSTCONTRAST']._serialized_start=2665
  _globals['_RANDOMADJUSTCONTRAST']._serialized_end=2736
  _globals['_RANDOMADJUSTHUE']._serialized_start=2738
  _globals['_RANDOMADJUSTHUE']._serialized_end=2780
  _globals['_RANDOMADJUSTSATURATION']._serialized_start=2782
  _globals['_RANDOMADJUSTSATURATION']._serialized_end=2855
  _globals['_RANDOMDISTORTCOLOR']._serialized_start=2857
  _globals['_RANDOMDISTORTCOLOR']._serialized_end=2901
  _globals['_RANDOMJITTERBOXES']._serialized_start=2903
  _globals['_RANDOMJITTERBOXES']._serialized_end=2943
  _globals['_RANDOMCROPIMAGE']._serialized_start=2946
  _globals['_RANDOMCROPIMAGE']._serialized_end=3155
  _globals['_RANDOMPADIMAGE']._serialized_start=3158
  _globals['_RANDOMPADIMAGE']._serialized_end=3295
  _globals['_RANDOMCROPPADIMAGE']._serialized_start=3298
  _globals['_RANDOMCROPPADIMAGE']._serialized_end=3591
  _globals['_RANDOMCROPTOASPECTRATIO']._serialized_start=3593
  _globals['_RANDOMCROPTOASPECTRATIO']._serialized_end=3672
  _globals['_RANDOMBLACKPATCHES']._serialized_start=3674
  _globals['_RANDOMBLACKPATCHES']._serialized_end=3785
  _globals['_RANDOMRESIZEMETHOD']._serialized_start=3787
  _globals['_RANDOMRESIZEMETHOD']._serialized_end=3852
  _globals['_SCALEBOXESTOPIXELCOORDINATES']._serialized_start=3854
  _globals['_SCALEBOXESTOPIXELCOORDINATES']._serialized_end=3884
  _globals['_RESIZEIMAGE']._serialized_start=3887
  _globals['_RESIZEIMAGE']._serialized_end=4079
  _globals['_RESIZEIMAGE_METHOD']._serialized_start=4012
  _globals['_RESIZEIMAGE_METHOD']._serialized_end=4079
  _globals['_SUBTRACTCHANNELMEAN']._serialized_start=4081
  _globals['_SUBTRACTCHANNELMEAN']._serialized_end=4117
  _globals['_SSDRANDOMCROPOPERATION']._serialized_start=4120
  _globals['_SSDRANDOMCROPOPERATION']._serialized_end=4305
  _globals['_SSDRANDOMCROP']._serialized_start=4307
  _globals['_SSDRANDOMCROP']._serialized_end=4391
  _globals['_SSDRANDOMCROPPADOPERATION']._serialized_start=4394
  _globals['_SSDRANDOMCROPPADOPERATION']._serialized_end=4707
  _globals['_SSDRANDOMCROPPAD']._serialized_start=4709
  _globals['_SSDRANDOMCROPPAD']._serialized_end=4799
  _globals['_SSDRANDOMCROPFIXEDASPECTRATIOOPERATION']._serialized_start=4802
  _globals['_SSDRANDOMCROPFIXEDASPECTRATIOOPERATION']._serialized_end=4951
  _globals['_SSDRANDOMCROPFIXEDASPECTRATIO']._serialized_start=4954
  _globals['_SSDRANDOMCROPFIXEDASPECTRATIO']._serialized_end=5095
  _globals['_SSDRANDOMCROPPADFIXEDASPECTRATIOOPERATION']._serialized_start=5098
  _globals['_SSDRANDOMCROPPADFIXEDASPECTRATIOOPERATION']._serialized_end=5364
  _globals['_SSDRANDOMCROPPADFIXEDASPECTRATIO']._serialized_start=5367
  _globals['_SSDRANDOMCROPPADFIXEDASPECTRATIO']._serialized_end=5514
# @@protoc_insertion_point(module_scope)
