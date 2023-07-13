import abc
import typing
import random
import requests

class RandomGenerator(abc.ABC):

    @abc.abstractmethod
    def pick(self, weights: typing.List[int]) -> int:
        """Randomly pick an index from list of weights

        Args:
            weights: list of weights
        """
        pass

class QuantumRandomGenerator(RandomGenerator):
    # since the API have rate limit 1 request/minute
    # it's not practical to have it simulated
    def pick(self, weights: typing.List[int]) -> int:
        response = requests.get(f'https://qrng.anu.edu.au/API/jsonI.php?length=1&type=uint16').json()
        random_number = response['data'][0]
        expanded_weights = []
        for i in range(len(weights)):
            for _ in range(weights[i]):
                expanded_weights.append(i)
        return expanded_weights[random_number % sum(weights)]

class PythonRandomGenerator(RandomGenerator):
    def pick(self, weights: typing.List[int]) -> int:
        return random.choices([index for index in range(len(weights))], weights)[0]
        
