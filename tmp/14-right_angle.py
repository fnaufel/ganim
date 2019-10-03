import ganim as ga
from ganim.angles import DoAngle
from ganim.line_elements import DoLineSegment

ga.reset_default_style()

s1 = ga.Scene()

seg1 = DoLineSegment((0, 0), (0, 2), effect='fadein', color='r')
seg2 = DoLineSegment((0, 0), (2, 0), effect='fadein')

seg3 = DoLineSegment((3, 3), (3, 0), effect='fadein', color='r')
seg4 = DoLineSegment((3, 3), (6, 3), effect='fadein')

seg5 = DoLineSegment((1, 1), (3, 2), effect='fadein', color='r')
seg6 = DoLineSegment((1, 1), (0, 3), effect='fadein')

s1.add_part(
    duration=2,
    script=[
        seg1,
        seg2,
        seg3,
        seg4,
        seg5,
        seg6,
    ]
)

s1.add_part(
    duration=3,
    script=[
        DoAngle((0, 0), seg2, seg1, effect='fadein', facecolor='green'),
        DoAngle((3, 3), seg3, seg4, effect='fadein'),
        DoAngle((1, 1), seg5, seg6, effect='fadein')
    ]
)

print(f'Rendering scene s1:\n{s1}...')
s1.render()
print('Saving...')
s1.save('14-right_angle.mp4')
