import ganim as ga
from ganim.line_actions import DoLineSegment

ga.reset_default_style()

fig, ax = ga.create_scene()

args = {
    'effect': 'grow'
}

parts = [
    {
        'duration': 1,
        'actions': [
            DoLineSegment(
                point_a=(4, 0),
                point_b=(4, 3),
                color='blue',
                **args
            ),
        # ]
    # },
    # {
    #     'duration': .5,
    #     'actions': [
            DoLineSegment(
                    point_a=(0, 0),
                    point_b=(4, 0),
                    color='r',
                    **args
            ),
            DoLineSegment(
                    point_a=(0, 0),
                    point_b=(4, 3),
                    color='green',
                    **args
            )
        ]
    }
]

scene = ga.render_scene(parts, fig)

print('Salvando...')
scene.save('segments04-triangle.mp4')
# plt.show()
