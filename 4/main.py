from typing import List


def MadMax(N: int, Tele: List[int]) -> List[int]:
    result = sorted(Tele)[N // 2:]
    result.reverse()
    return sorted(Tele)[:N // 2] + result
