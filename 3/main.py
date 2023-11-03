from typing import List

def ConquestCampaign(N: int, M: int, L: int, battalion: List[int]):
    counter = 0
    in_val = battalion.copy()

    while True:
        list_batallions = set()
        for i in range(len(in_val)):
            if i % 2 != 0:
                list_batallions.add(tuple([in_val[i - 1], in_val[i]]))

        list_batallions_copy = list_batallions.copy()
        list_b = list(list_batallions)

        for i in range(len(list_batallions)):
            if list_b[i][0] - 1 != 0 and list_b[i][0] - 1 <= M and list_b[i][1] != 0 and list_b[i][1] <= N:
                list_batallions_copy.add(tuple([list_b[i][0] - 1, list_b[i][1]]))
            if list_b[i][0] - 1 != 0 and list_b[i][0] - 1 <= M and list_b[i][1] != 0 and list_b[i][1] <= N:
                list_batallions_copy.add(tuple([list_b[i][0] - 1, list_b[i][1]]))
            if list_b[i][0] + 1 != 0 and list_b[i][0] + 1 <= M and list_b[i][1] != 0 and list_b[i][1] <= N:
                list_batallions_copy.add(tuple([list_b[i][0] + 1, list_b[i][1]]))
            if list_b[i][0] != 0 and list_b[i][0] <= M and list_b[i][1] - 1 != 0 and list_b[i][1] - 1 <= N:
                list_batallions_copy.add(tuple([list_b[i][0], list_b[i][1] - 1]))
            if list_b[i][0] != 0 and list_b[i][0] <= M and list_b[i][1] + 1 != 0 and list_b[i][1] + 1 <= N:
                list_batallions_copy.add(tuple([list_b[i][0], list_b[i][1] + 1]))

        list_a = list(list_batallions_copy)
        result = []
        for i in range(len(list_a)):
            result.append(list_a[i][0])
            result.append(list_a[i][1])
        if result == in_val:
            return counter
        counter += 1
        in_val = result.copy()


print(ConquestCampaign(3, 4, 0, [2, 2, 3, 4]))
