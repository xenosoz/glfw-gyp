#
# glfw_dll.gypi
#
{
  'targets': [
    {
      'target_name': 'glfw_dll',
      'product_name': 'glfw',
      'type': 'shared_library',
      'direct_dependent_settings': {
        'include_dirs': [
          'glfw-2.7.6/include/',
        ],
      },
      'defines': [
        '_GLFW_NO_DLOAD_WINMM',
        '_GLFW_NO_DLOAD_GDI32',
        'GLFW_BUILD_DLL',
        'WIN32',
        '_WINDOWS',
        '_USRDLL',
        'GLFWDLL_EXPORTS',
        '_WINDLL',
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
        'glfw-2.7.6/lib/win32/glfwdll.def',
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
      'libraries': [
        'winmm.lib',
        'opengl32.lib',
        'kernel32.lib',
        'user32.lib',
        'gdi32.lib',
        'winspool.lib',
        'comdlg32.lib',
        'advapi32.lib',
        'shell32.lib',
        'ole32.lib',
        'oleaut32.lib',
        'uuid.lib',
        'odbc32.lib',
        'odbccp32.lib',
      ],
      'conditions': [
        ['OS!="win"', {
          'sources!': [
            'glfw-2.7.6/lib/win32/glfwdll.def',
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
  ], # targets
}
# vim:sts=2:sw=2:norl
