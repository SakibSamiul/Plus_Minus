def plusMinus(arr):
    # Write your code here
    minus = 0
    plus = 0
    zero = 0
    for element in arr:
        if element > 0:
            plus += 1
        elif element < 0:
            minus += 1
        else:
            zero += 1
        
        ratio1 = plus / n
        ratio2 = minus / n
        ratio3 = zero / n
   
    print(ratio1)
    print(ratio2)
    print(ratio3)
if __name__ == '__main__':
    n = int(input("Size of an array: ").strip())

    arr = list(map(int, input("Elements of array: ").rstrip().split()))

    plusMinus(arr)