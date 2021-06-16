def main(arr):
    arr.sort()
    max_sum = 0

    for i in range(len(arr)//2):
        tmp_sum = sum_opposites(arr, i)
        if tmp_sum > max_sum:
            max_sum = tmp_sum

    return max_sum


def sum_opposites(arr, index):
    return arr[index] + arr[ -index - 1]
    
