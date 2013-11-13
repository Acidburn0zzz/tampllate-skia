# Build ALMOST everything provided by Skia; this should be the default target.
#
# This omits the following targets that many developers won't want to build:
# - debugger: this requires QT to build
#
{
  'targets': [
    {
      'target_name': 'most',
      'type': 'none',
      'dependencies': [
        # The minimal set of static libraries for basic Skia functionality.
        'skia_lib.gyp:skia_lib',

        'bench.gyp:bench',
        'skia-test-app',
      ],
      'conditions': [
        ['skia_build_for_tizen == 0', {
          'dependencies': [
        'gm.gyp:gm',
        'SampleApp.gyp:SampleApp',
        'tests.gyp:tests',
        'tools.gyp:tools',
        'pathops_unittest.gyp:*',
        'skpskgr_test.gyp:*',
#       'pdfviewer.gyp:pdfviewer',
        'dm.gyp:dm',
        ]}],
        ['skia_os == "android"', {
          'dependencies': [ 'android_system.gyp:SampleApp_APK' ],
        }],
        # DM assumes you've got a GPU.
        ['skia_gpu == 1', {
          'dependencies': [ 'dm.gyp:dm' ],
        }],
      ],
    },
    {
      'target_name': 'skia-test-app',
      'type': 'executable',
      'dependencies': [
        'skia_lib.gyp:skia_lib',
      ],
      'sources': [
        '../skia_test.cc',
      ],
      'link_settings': {
        'libraries': [
          '-lX11',
          '-lGLESv2',
          '-lEGL',
        ],
      },
    },
  ],
}
