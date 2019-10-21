import ganim as ga
from ganim.angles import DoAngle
from ganim.line_elements import DoLineSegment

ga.reset_default_style()

s1 = ga.Scene()

seg1 = DoLineSegment((0, 0), (2, 1), effect='fadein')
seg2 = DoLineSegment((0, 0), (3, 5), effect='fadein')

s1.add_part(
    duration=2,
    script=[
        seg1,
        seg2
    ]
)

s1.add_part(
    duration=3,
    script=[
        DoAngle((0, 0), seg1, seg2, effect='fadein', label=r'$\alpha$'),
#        DoAngle((0, 0), seg2, seg1, effect='fadein', facecolor='green')
    ]
)

print(f'Rendering scene s1:\n{s1}...')
s1.render()
print('Saving...')
s1.save('13-angle.mp4')
