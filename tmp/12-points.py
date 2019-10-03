import ganim as ga
from ganim.points import DoPoint

ga.reset_default_style()

s1 = ga.Scene()

s1.add_part(
    duration=3,
    script=[
        DoPoint((0, 0)),
        DoPoint((16, 0)),
        DoPoint((16, 9)),
        DoPoint((0, 9)),
        DoPoint((2, 3), marker='s', color='red', markersize=6, effect='fadein'),
        DoPoint((3, 4), marker='P', color='yellow', markersize=6, effect='fadein'),
    ]
)

print(f'Rendering scene s1:\n{s1}...')
s1.render()
print('Saving...')
s1.save('12-points.mp4')
