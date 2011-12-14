# Port-specific Skia library code.
{
  'includes': [
    'common.gypi',
  ],
  'targets': [
    {
      'target_name': 'ports',
      'type': 'static_library',
      'include_dirs': [
        '../include/config',
        '../include/core',
        '../include/ports',
        '../include/xml',
        '../src/core',
      ],
      'sources': [
        '../src/ports/SkDebug_stdio.cpp',
        '../src/ports/SkDebug_win.cpp',
        '../src/ports/SkFontHost_sandbox_none.cpp',
        '../src/ports/SkFontHost_win.cpp',
        '../src/ports/SkThread_win.cpp',

        '../src/ports/SkFontHost_tables.cpp',
        '../src/ports/SkMemory_malloc.cpp',
        '../src/ports/SkOSFile_stdio.cpp',
        '../src/ports/SkTime_Unix.cpp',
        '../src/ports/SkTime_win.cpp',
        '../src/ports/SkXMLParser_empty.cpp',
        '../src/ports/sk_predefined_gamma.h',
      ],
      'conditions': [
        [ 'skia_os in ["linux", "freebsd", "openbsd", "solaris"]', {
          'sources': [
            '../src/ports/SkThread_pthread.cpp',
            '../src/ports/SkFontHost_FreeType.cpp',
            '../src/ports/SkFontHost_gamma_none.cpp',
            '../src/ports/SkFontHost_linux.cpp',
          ],
        }],
        [ 'skia_os == "mac"', {
          'include_dirs': [
            '../include/utils/mac',
            '../third_party/freetype/include/**',
          ],
          'sources': [
            '../src/ports/SkFontHost_mac_coretext.cpp',
#            '../src/ports/SkFontHost_FreeType.cpp',
#            '../src/ports/SkFontHost_freetype_mac.cpp',
#            '../src/ports/SkFontHost_gamma_none.cpp',
            '../src/ports/SkThread_pthread.cpp',
          ],
        }],
        [ 'skia_os == "ios"', {
          'include_dirs': [
            '../include/utils/ios',
          ],
          'sources': [
            '../src/ports/SkFontHost_mac_coretext.cpp',
            '../src/ports/SkThread_pthread.cpp',
          ],
        }],
        [ 'skia_os == "win"', {
          'include_dirs': [
            'config/win',
          ],
          'sources!': [ # these are used everywhere but windows
            '../src/ports/SkDebug_stdio.cpp',
            '../src/ports/SkTime_Unix.cpp',
          ],
        }, { # else !win
          'sources!': [
            '../src/ports/SkDebug_win.cpp',
            '../src/ports/SkFontHost_win.cpp',
            '../src/ports/SkThread_win.cpp',
            '../src/ports/SkTime_win.cpp',
          ],
        }],
        [ 'skia_os == "android"', {
          'sources!': [
            '../src/ports/SkDebug_stdio.cpp',
          ],
          'sources': [
            '../src/ports/SkDebug_android.cpp',
            '../src/ports/SkThread_pthread.cpp',
            '../src/ports/SkFontHost_android.cpp',
            '../src/ports/SkFontHost_gamma.cpp',
            '../src/ports/SkFontHost_FreeType.cpp',
            '../src/ports/FontHostConfiguration_android.cpp',
          ],
        }],        
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          '../include/ports',
        ],
      },
    },
  ],
}

# Local Variables:
# tab-width:2
# indent-tabs-mode:nil
# End:
# vim: set expandtab tabstop=2 shiftwidth=2:
