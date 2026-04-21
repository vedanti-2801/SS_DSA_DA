arr = [10, 60, 70, 40, 50]

max_val = arr[0]

for i in range(len(arr)):
    if arr[i] > max_val:
        max_val = arr[i]

print("Max=", max_val)