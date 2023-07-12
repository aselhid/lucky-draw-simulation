from random_generator import RandomGenerator
import typing

class FunLuckyDraw:
    def __init__(
            self, 
            random_generator: RandomGenerator, 
            population_seed: typing.List[typing.Tuple[str, int]],
            weight_modifier: typing.Callable[[int], int]) -> None:
        self._random_generator: RandomGenerator = random_generator
        self._population: typing.List[typing.Tuple[str, int]] = population_seed
        self._weight_modifier: typing.Callable[[int], int] = weight_modifier


    def draw(self) -> typing.Tuple[str, int]:
        winner_index = self._random_generator.pick([self._weight_modifier(weight) for _, weight in self._population])
        winner = self._population[winner_index]
        self._update(winner_index)
        return winner

    def _update(self, winner: int):
        self._population = [(element[0], element[1] + 1) if index != winner else (element[0], 0) for index, element in enumerate(self._population)]

    def __str__(self) -> str:
        return "\n".join([f'{name}: {weight}' for name, weight in self._population])

