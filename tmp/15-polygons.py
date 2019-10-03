import ganim as ga
from ganim.angles import DoAngle
from ganim.points import DoPoint
from ganim.polygons import DoPolygon

ga.reset_default_style()

s1 = ga.Scene()

vertices = [
    (0, 0), (2, 0), (1, 2)
]

triangulo = DoPolygon(vertices, facealpha=0.5, facecolor='blue')
angulo = DoAngle(
        vertices[0],
        triangulo.sides[0],
        triangulo.sides[-1],
        radius=.5,
        edgecolor='red',
        facecolor='green',
        facealpha=1,
#        effect='fadein',
#        start_after=1
)

s1.add_part(
        duration=3,
        script=[
            triangulo,
            angulo,
            DoPoint((.2, .1)),
        ]
)

print(f'Rendering scene s1:\n{s1}...')
s1.render()
print('Saving...')
s1.save('15-polygons.mp4')
