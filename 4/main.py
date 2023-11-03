from typing import List


def MadMax(N: int, Tele: List[int]) -> List[int]:
    result = sorted(Tele)[N // 2 + 1:]
    result.reverse()
    return sorted(Tele)[:N // 2 + 1] + result


arr = [1, 2, 9, 19, 4, 6, 11]
start = MadMax(7, arr)
print(start)
