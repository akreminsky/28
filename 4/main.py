def sort_and_max_center(arr, N): Создаем


случайный
массив
чисел
random_arr = generate_random_array(N)
sorted_arr = sorted(random_arr)
arr.append(sorted_arr[0])
for i in reversed(range(len(sorted_arr))): arr.insert(0, sorted_arr[i])
max_index = len(arr) // 2
result = arr[:max_index + 1] + arr[max_index:]
return result
arr = [1, 2, 3, 4, 5, 6, 7]
start = start_impulse(arr)
print(start)
