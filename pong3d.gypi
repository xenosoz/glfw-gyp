#
# pong3d.gypi
#
{
  'targets': [
    {
      'target_name': 'pong3d',
      'type': 'executable',
      'dependencies': [
        'glfw_static',
      ],
      'sources': [
        'glfw-2.7.6/examples/pong3d.c',
      ],
      'copies': [
        {
          'destination': '.',
          'files': [
            'glfw-2.7.6/examples/pong3d_field.tga',
            'glfw-2.7.6/examples/pong3d_instr.tga',
            'glfw-2.7.6/examples/pong3d_menu.tga',
            'glfw-2.7.6/examples/pong3d_title.tga',
            'glfw-2.7.6/examples/pong3d_winner1.tga',
            'glfw-2.7.6/examples/pong3d_winner2.tga',
          ],
        },
      ],
    },
  ],
}
# vim:sts=2:sw=2:norl
