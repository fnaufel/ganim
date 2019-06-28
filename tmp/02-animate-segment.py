import ganim as ga
from ganim.line_elements import DoLineSegment

ga.reset_default_style()

fig, ax = ga.create_scene()

parts = [
    {
        'duration': 5,
        'actions' : [
            DoLineSegment(
                ax=ax,
                point_a=(.2, .3),
                point_b=(.9, .9),
                color='r',
                effect='grow'
            )
        ]
    },
    {
        'duration': 5,
        'actions' : [
            DoLineSegment(
                ax=ax,
                point_a=(.9, .9),
                point_b=(.1, .1),
                color='r',
            ),
            DoLineSegment(
                ax=ax,
                point_a=(.3, .3),
                point_b=(.8, .3),
                color='r',
                effect='grow'
            )
        ]
    }
]

scene = ga.render_scene(parts, fig)

print('Salvando...')
scene.save('segment02.mp4')
# plt.show()
