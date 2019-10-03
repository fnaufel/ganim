import ganim as ga
from ganim.line_elements import DoLineSegment

ga.reset_default_style()

s1 = ga.Scene()

args1 = {'stay': False, 'end_at': 2, 'effect': 'grow'}
s1.add_part(
    duration=3,
    script=[
        DoLineSegment((0, 0), (4, 3), color='green', **args1),
        DoLineSegment((4, 0), (4, 3), color='blue' , **args1),
        DoLineSegment((0, 0), (4, 0), color='red'  , **args1),
    ]
)

s1.add_part(
    duration=2,
    script=[
        DoLineSegment((0, 0), (4, 3), color='green', effect='shrink'),
        DoLineSegment((4, 0), (4, 3), color='blue' , effect='shrink'),
        DoLineSegment((0, 0), (4, 0), color='red'  , effect='shrink')
    ]
)

print(f'Rendering scene s1:\n{s1}...')
s1.render()
print('Saving...')
s1.save('10-shrink.mp4')
