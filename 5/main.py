from typing import List


def SynchronizingTables(n: int, ids: List[int], salary: List[int]) -> List[int]:
    return [val for val in dict(sorted({ids[i]: sorted(salary)[i] for i in range(n)}.items())).values()]
