from random import randint

gravitational_constant = 6.67408E-11
"""Гравитационная постоянная Ньютона G"""


class Star():
    """Тип данных, описывающий звезду.
    Содержит массу, координаты, скорость звезды,
    а также визуальный радиус звезды в пикселах и её цвет.
    """

    type = "star"
    """Признак объекта звезды"""

    m = 0
    """Масса звезды"""

    x = 0
    """Координата по оси **x**"""

    y = 0
    """Координата по оси **y**"""

    Vx = 0
    """Скорость по оси **x**"""

    Vy = 0
    """Скорость по оси **y**"""

    Fx = 0
    """Сила по оси **x**"""

    Fy = 0
    """Сила по оси **y**"""

    R = 5
    """Радиус звезды"""

    color = "red"
    """Цвет звезды"""

    image = None
    """Изображение звезды"""


class Planet():
    """Тип данных, описывающий планету.
    Содержит массу, координаты, скорость планеты,
    а также визуальный радиус планеты в пикселах и её цвет
    """

    type = "planet"
    """Признак объекта планеты"""

    m = 0
    """Масса планеты"""

    x = 0
    """Координата по оси **x**"""

    y = 0
    """Координата по оси **y**"""

    Vx = 0
    """Скорость по оси **x**"""

    Vy = 0
    """Скорость по оси **y**"""

    Fx = 0
    """Сила по оси **x**"""

    Fy = 0
    """Сила по оси **y**"""

    R = 5
    """Радиус планеты"""

    color = "green"
    """Цвет планеты"""

    image = None
    """Изображение планеты"""


def calculate_force(body, space_objects):
    """Вычисляет силу, действующую на тело.

    Параметры:

    **body** — тело, для которого нужно вычислить дейстующую силу.

    **space_objects** — список объектов, которые воздействуют на тело.
    """

    body.Fx = body.Fy = 0
    for obj in space_objects:
        if body == obj:
            body.Fx += 0
            body.Fy += 0
        else:
            body.Fx += gravitational_constant * body.m * obj.m / ((body.x-obj.x)**2 + (body.y-obj.y)**2)**1.5 * (obj.x - body.x)
            body.Fy += gravitational_constant * body.m * obj.m / ((body.x-obj.x)**2 + (body.y-obj.y)**2)**1.5 * (obj.y - body.y)




def move_space_object(body, dt):
    """Перемещает тело в соответствии с действующей на него силой.

    Параметры:

    **body** — тело, которое нужно переместить.
    """

    ax = body.Fx/body.m
    body.Vx = body.Vx + ax * dt
    body.x = body.x + body.Vx*dt
    ay = body.Fy/body.m
    body.Vy = body.Vy + ay*dt
    body.y = body.y + body.Vy * dt

def calc_angular_velocity(body):
    ro = (1+body.Vx**2+body.Vy**2)**1.5/((body.Fx/body.m)**2 + (body.Fy/body.m)**2)**0.5
    Va = (body.Vx**2+body.Vy**2)**2/ro
'Второй закон Кеплера в данной симуляции выполняется в случае, если тела двужутся по круговым орбитам вокруг Солнца.'

def recalculate_space_objects_positions(space_objects, dt):
    """Пересчитывает координаты объектов.

    Параметры:

    **space_objects** — список оьъектов, для которых нужно пересчитать координаты.

    **dt** — шаг по времени
    """

    for body in space_objects:
        calculate_force(body, space_objects)
    for body in space_objects:
        move_space_object(body, dt)
    for body in space_objects:
        calc_angular_velocity(body)

if __name__ == "__main__":
    print("This module is not for direct call!")