import ganim as ga
from ganim.line_elements import DoLineSegment

ga.reset_default_style()

fig, ax = ga.create_scene()

parts = [
    {
        'duration': 5,
        'actions' : [
            DoLineSegment(
                point_a=(.3, .1),
                point_b=(.3, .9),
                color='r'
            ),
            DoLineSegment(
                point_a=(.7, .1),
                point_b=(.7, .9),
                color='yellow',
                effect='grow'
            )
        ]
    }
]

scene = ga.render_scene(parts, fig)

print('Salvando...')
scene.save('segment03.mp4')
# plt.show()
