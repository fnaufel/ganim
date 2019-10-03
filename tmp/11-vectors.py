import ganim as ga
from ganim.line_elements import DoVector

ga.reset_default_style()

s1 = ga.Scene()

s1.add_part(
    duration=3,
    script=[
        DoVector((0, 0), (4, 3), color='green')
    ]
)

print(f'Rendering scene s1:\n{s1}...')
s1.render()
print('Saving...')
s1.save('11-vectors.mp4')
