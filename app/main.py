from typing import Callable


def cache(func: Callable) -> Callable:
    collected_data = {}

    def inner(*args, **kwargs) -> int:
        elem = (args, func.__name__)

        if elem in collected_data:
            print("Getting from cache")
            return collected_data[elem]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            collected_data[elem] = result
            return result
    return inner
