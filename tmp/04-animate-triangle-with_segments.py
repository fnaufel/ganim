import ganim as ga
from ganim.line_elements import DoLineSegment

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
                (4, 0),
                (4, 3),
                color='blue',
                **args
            ),
        # ]
    # },
    # {
    #     'duration': .5,
    #     'actions': [
            DoLineSegment(
                    (0, 0),
                    (4, 0),
                    color='r',
                    **args
            ),
            DoLineSegment(
                    (0, 0),
                    (4, 3),
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
