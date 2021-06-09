#Problema 2

def valid_sudoku(board):
    return validate_rows()

def validate_rows(board):
    for row in (board):
        numbers = []
        for number in row:
            if number != ".":
                if number in numbers:
                    return False
                else: 
                    numbers.append(number)
    return True

# def validate_columns(board):
#     i, j = 0
#     board[i][j]
#     increment i, j

#     for i in range(len(board)):


#Problema 1

def move_zeroes(input_array):
    counter = 0
    for index, char in enumerate(input_array):
        if char == 0:
            input_array.pop(index)
            counter += 1
    
    return (input_array + ([0] * counter))

# for index, value in enumerate(array)
# array.pop(index)
# [0] * 3 => [0,0,0]
# [1,2] + [3,4] => [1,2,3,4]

if __name__ == "__main__":
    main()