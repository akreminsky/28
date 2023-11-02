from typing import List


def odometer(oksana: List[int]) -> int:
    result = 0
    for i in range(len(oksana)):
        if i == 1:
            result += oksana[1] * oksana[0]
            continue
        if i % 2 != 0:
            if oksana[i] - oksana[i - 2] < 0:
                return 0
            result += (oksana[i] - oksana[i - 2]) * oksana[i - 1]
    return result
