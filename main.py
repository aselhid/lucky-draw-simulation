import lucky_draw
import random_generator
import typing
import matplotlib.pyplot as plt

INITIAL_POPULATION = [
        ('a', 1),
        ('b', 1),
        ('c', 1),
        ('d', 1),
        ('e', 1),
        ('f', 1),
        ('g', 1),
        ('h', 1),
        ('i', 1),
        ('j', 1),
        ('k', 1),
        ('l', 1)
    ]

identity_modifier: typing.Callable[[int], int] = lambda x: x 

quadratic_modifier: typing.Callable[[int], int] = lambda x: x ** 2

fun_lucky_draw = lucky_draw.FunLuckyDraw(
        random_generator.PythonRandomGenerator(),
        INITIAL_POPULATION,
        identity_modifier
    )

weight_map = {}
for _ in range(500000):
    name, weight = fun_lucky_draw.draw()

    # print('WIN', name, weight)
    # print(fun_lucky_draw)
    # print('----\n')

    if weight in weight_map:
        weight_map[weight] += 1
    else:
        weight_map[weight] = 1


weight_map_as_list = weight_map.items()
weights = [weight for weight, _ in weight_map_as_list]
occurences = [occurence for _, occurence in weight_map_as_list]

plt.bar(weights, occurences)
plt.xlabel('# weight when called')
plt.ylabel('# occurence')
plt.show()

