from pathlib import Path


def get_input(problem: int) -> str:
    path = Path()/'projecteuler'/'inputs'/f'{problem}.txt'

    with open(path, 'r') as file:
        return "".join(file.readlines()).strip()
