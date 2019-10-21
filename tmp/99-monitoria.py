import ganim as ga
from ganim.angles import DoAngle
from ganim.polygons import DoLineSegment

ga.reset_default_style()

s1 = ga.Scene()

floor = DoLineSegment((16, 0), (0, 0), color='green', effect='fadein', linewidth=2.0)
lr_floor = DoLineSegment((0, 0), (16, 0))
ramp = DoLineSegment((5, 0), (10, 5), color='white', effect='grow', linewidth=2.0, start_after=1)
leg = DoLineSegment((10, 5), (10, 0), color='yellow', effect='grow', linewidth=2.0, linestyle='dashed', start_after=1, end_at=3)
up_leg = DoLineSegment((10, 0), (10, 5))
right_angle = DoAngle((10, 0), up_leg, floor, label=r'$\frac{\pi}{2}$', effect='fadein', facecolor='black',
                      start_after=4)
angle = DoAngle((5, 0), lr_floor, ramp, label=r'$\theta$', effect='fadein', facecolor='red', start_after=0, end_at=2)

s1.add_part(
        [
            floor,
        ],
        duration=2
)

s1.add_part(
        [
            ramp,
        ],
        duration=3
)

s1.add_part(
        [
            leg,
            right_angle
        ],
        duration=7
)

s1.add_part(
        [
            angle,
        ],
        duration=3
)

print(f'Rendering scene s1:\n{s1}...')
s1.render()
print('Saving...')
s1.save('99-monitoria.mp4')
