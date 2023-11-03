from typing import List

def ConquestCampaign(N: int, M: int, L: int, battalion: List[int]):
    list_batallions = set()
    for i in range(len(battalion)):
        if i % 2 != 0:
            list_batallions.add(tuple([battalion[i - 1], battalion[i]]))

    list_batallions_copy = list_batallions.copy()
    list_b = list(list_batallions)

    for i in range(len(list_batallions)):
        if list_b[i][0] - 1 != 0 and list_b[i][0] - 1 <= M and list_b[i][1] != 0 and list_b[i][1] <= N:
            list_batallions_copy.add(tuple([list_b[i][0] - 1, list_b[i][1]]))
        if list_b[i][0] - 1 != 0 and list_b[i][0] - 1 <= N and list_b[i][1] != 0 and list_b[i][1] <= M:
            list_batallions_copy.add(tuple([list_b[i][0] - 1, list_b[i][1]]))
        if list_b[i][0] + 1 != 0 and list_b[i][0] + 1 <= N and list_b[i][1] != 0 and list_b[i][1] <= M:
            list_batallions_copy.add(tuple([list_b[i][0] + 1, list_b[i][1]]))
        if list_b[i][0]  != 0 and list_b[i][0] - 1 <= N and list_b[i][1] - 1 != 0 and list_b[i][1] - 1 <= M:
            list_batallions_copy.add(tuple([list_b[i][0], list_b[i][1] - 1]))
        if list_b[i][0]  != 0 and list_b[i][0] - 1 <= N and list_b[i][1] + 1 != 0 and list_b[i][1] + 1 <= M:
            list_batallions_copy.add(tuple([list_b[i][0], list_b[i][1] + 1]))
    list_a = list(list_batallions_copy)
    result = []
    for i in range(len(list_a)):
        result.append(list_a[i][0])
        result.append(list_a[i][1])
    if result == battalion:
        return L
    return ConquestCampaign(N, M, L+1, result)

print(ConquestCampaign(15, 15, 0, [1, 1, 6, 6]))
