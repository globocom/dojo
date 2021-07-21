# def main(nums,target):
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             if check_sum(nums[i], nums[j], target):
#                 return [i, j]

def main(nums, target):
    seen = {}
    for i in range(len(nums)):
        if nums[i] in seen:
            return [seen[nums[i]], i]
        seen[target-nums[i]] = i

def check_sum(a, b, target):
    return target == a+b

