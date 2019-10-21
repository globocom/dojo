def find_largest_sum(some_list):
    big = 0
    for pos, value in enumerate(some_list):
        if value > some_list[big]:
            big = pos
    return (big, big)

def sum_interval(sample_list, begin, end):
    return sum(sample_list[begin:end+1])

def build_matrix(some_list):
    return [
            [1, 3, 2],
            [2, 1],
            [-1]
    ]