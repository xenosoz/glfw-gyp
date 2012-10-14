#
# glfw_lib.gypi
#
{
  'targets': [
    {
      'target_name': 'glfw_static',
      'product_name': 'glfw',
      'type': 'static_library',
      'direct_dependent_settings': {
        'include_dirs': [
          'glfw-2.7.6/include/',
        ],
      },
      'link_settings': {
        'libraries': [
          '-lopengl32.lib',
          '-lglu32.lib',
        ],
      },
      'defines': [
        'WIN32',
        '_LIB',
        '_MBCS',
      ],
      'sources': [
        'glfw-2.7.6/include/GL/glfw.h',
        'glfw-2.7.6/lib/enable.c',
        'glfw-2.7.6/lib/fullscreen.c',
        'glfw-2.7.6/lib/glext.c',
        'glfw-2.7.6/lib/image.c',
        'glfw-2.7.6/lib/init.c',
        'glfw-2.7.6/lib/input.c',
        'glfw-2.7.6/lib/internal.h',
        'glfw-2.7.6/lib/joystick.c',
        'glfw-2.7.6/lib/stream.c',
        'glfw-2.7.6/lib/tga.c',
        'glfw-2.7.6/lib/thread.c',
        'glfw-2.7.6/lib/time.c',
        'glfw-2.7.6/lib/win32/platform.h',
        'glfw-2.7.6/lib/win32/win32_dllmain.c',
        'glfw-2.7.6/lib/win32/win32_enable.c',
        'glfw-2.7.6/lib/win32/win32_fullscreen.c',
        'glfw-2.7.6/lib/win32/win32_glext.c',
        'glfw-2.7.6/lib/win32/win32_init.c',
        'glfw-2.7.6/lib/win32/win32_joystick.c',
        'glfw-2.7.6/lib/win32/win32_thread.c',
        'glfw-2.7.6/lib/win32/win32_time.c',
        'glfw-2.7.6/lib/win32/win32_window.c',
        'glfw-2.7.6/lib/window.c',
      ],
      'include_dirs': [
        'glfw-2.7.6/lib/',
        'glfw-2.7.6/lib/win32/',
      ],
      'conditions': [
        ['OS!="win"', {
          'sources!': [
            'glfw-2.7.6/lib/win32/platform.h',
            'glfw-2.7.6/lib/win32/win32_dllmain.c',
            'glfw-2.7.6/lib/win32/win32_enable.c',
            'glfw-2.7.6/lib/win32/win32_fullscreen.c',
            'glfw-2.7.6/lib/win32/win32_glext.c',
            'glfw-2.7.6/lib/win32/win32_init.c',
            'glfw-2.7.6/lib/win32/win32_joystick.c',
            'glfw-2.7.6/lib/win32/win32_thread.c',
            'glfw-2.7.6/lib/win32/win32_time.c',
            'glfw-2.7.6/lib/win32/win32_window.c',
          ],
          'include_dirs!': [
            'glfw-2.7.6/lib/win32/',
          ],
        }],
      ],
    },
  ],
}
# vim:sts=2:sw=2:norl
