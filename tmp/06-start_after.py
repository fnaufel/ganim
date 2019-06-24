import ganim as ga
from ganim.line_actions import DoLineSegment

ga.reset_default_style()

fig, ax = ga.create_scene()

parts = [
    {
        'duration': 4,
        'actions': [
            DoLineSegment((4, 0), (4, 3), start_after=1, color='blue'),
            DoLineSegment((0, 0), (4, 0), start_after=2, color='red'),
            DoLineSegment((0, 0), (4, 3), start_after=3, color='green')
        ]
    }
]

scene = ga.render_scene(parts, fig)

print('Saving...')
scene.save('segments06-triangle-start_after.mp4')
