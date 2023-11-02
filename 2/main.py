from typing import List


def odometer(oksana: List[int]):
    result = 0
    for i in range(len(oksana)):
        if i % 2 != 0:
            result += oksana[i]*oksana[i-1]
    return result
