from typing import Callable


def cache(func: Callable) -> Callable:
    collected_data = {}

    def inner(*args):
        if args in collected_data:
            print("Getting from cache")
        else:
            print("Calculating new result")
            collected_data[args] = func(args)
            return func(args)
    return inner

