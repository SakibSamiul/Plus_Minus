arr = [-4, 3, -9, 0, 4, 1]
plus = 0
minus = 0
zero = 0

for element in arr:
    if element > 0:
        plus += 1
    elif element < 0:
        minus += 1
    else:
        zero += 1

ratio1 = plus / len(arr)
ratio2 = minus / len(arr)
ratio3 = zero / len(arr)

print(ratio1, ratio2, ratio3)