def add_value_to_permutation(i, first_number, permutation_response):
    result = []
    for j in range(0,len(permutation_response)):
        new_array = permutation_response[j][:]
        new_array.insert(i,first_number)
        result.append(new_array)
    return result

def hashme(permuts):
    return { str(x) for x in permuts }

def permutation(numbers):
    if len(numbers) == 0:
        return [[]]
    if len(numbers) == 1:
        return [numbers]
    if len(numbers) == 2:
        return [[numbers[0],numbers[1]],[numbers[1],numbers[0]]]
    
    first_number = numbers[0]

    new_x = numbers[1:]

    permutation_response = permutation(new_x)

    result = []

    for i in range(0,len(numbers)):
        result = result + add_value_to_permutation(i, first_number, permutation_response)

    return result
 
# return [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#  = 1
# r = [2,3] ---> permitation() -> [[2,3], [3,2])
                        #    -> [ [1,2,3], [1,3,2]  ]
                            #    -> [ [2,1,3], [3,1,2]  ]
                            #    -> [ [2,3,1], [3,2,1]  ]

# qtd de posicoes = tamanho do array
# tirar esse cara do array => [2,3]
# chamar funcao permutation([2,3]) => [[2,3],[3,2]] => salva numa variavel
# for na qtd de posicoes (for ate 2)

# if len(numbers) == 0:

#     return [[]]
# if len(numbers) == 1:
#     return [[0]]
# return [[0,1],[1,0]]

# Given an array nums of distinct integers, return all the possible permutations.

# Input: nums = [0,1]
# Output: [[0,1],[1,0]]

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

# Ingrid - Christian - Tiago - Sara - Andre

# [1,2,3,4]

# [[1,2,3,4],[1,2,4,3],[1,3,2,4],[1,3,4,2],[1,4,2,3],[1,4,3,2],[2,1,3,4],[2,1,4,3],[2,3,1,4],[2,3,4,1],[2,4,1,3],[2,4,3,1],[3,1,2,4],[3,1,4,2],[3,2,1,4],[3,2,4,1],[3,4,1,2],[3,4,2,1],[4,1,2,3],[4,1,3,2],[4,2,1,3],[4,2,3,1],[4,3,1,2],[4,3,2,1]]