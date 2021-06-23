def main(nums):
    pd = [-1] * len(nums)
    pd[0] = 0
    for i, element in enumerate(nums):
        for j in range(i + 1 , i + element + 1 ):
            if j >= len(nums) or pd[j] != -1:
                continue
            pd[j] = pd[i]+1
    return pd[-1]



# pd = None

# def min_numers_jumps(nums, i):
#     global pd
#     if i >= len(nums):
#         return 0
#     if pd[i] != -1:
#         return pd[i]
#     min_jumps = 100000000
#     for j in range(1,nums[i]+1):
#         print(pd, "curr i= ", i, "j=",j)
#         min_jumps = min(min_jumps, 1 + min_numers_jumps(nums, i + j))

#     pd[i] = min_jumps
#     return min_jumps

# def main(nums):
    # esta solução não funciona porque está fazendo em profundidade primeiro
    # global pd
    # result = min_numers_jumps(nums, 0)
    # print("finish", pd)
    # return result


# [0 ,-1,-1,-1,-1]
# [0 ,-1,-1,-1,-1]



# [2,3,1,1,4]
# 0 - 2
# 1 - 3
# pd[2] = 1



# [0,0,0,0,0]
# [0,1,1,0,0] - ind0
# [0,1,1,2,2] - ind1
# [0,1,1,2,2] - ind2
# [0,1,1,2,2] - ind3
# [0,1,1,2,2] - ind4
# ...
# N === 10^4


# [4, 3, 2, 3, , ,]
# int pd[100000];
# int array[10000];
# int mochila(int j, int n)
# {
#     if (j >= n) return 0;
#     if (pd[j] != -1) return pd[j];
#     int minJump = 1e9
#     for (int jump = 1; jump <= array[j]; jump++ )
#     {
#         minJump = min(minJump, jump + mochila(j+jump, n))
#     }
#     pd[j] = minJump;
# }

# for nums
#   for 1..nums[i] # até 1000
