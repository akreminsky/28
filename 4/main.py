def start_impulse(arr): arr.sort()


start = [arr[0]]
left = arr[1:len(arr) // 2 + 1]
right = arr[len(arr) // 2 + 1:][::-1]
start.extend(left)
start.extend(right)
return start

arr = [1, 2, 3, 4, 5, 6, 7]
start = start_impulse(arr)
print(start)
