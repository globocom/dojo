def count_letters_in_numbers(number):
    numbers = {1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        }
        
    dozens = {10: 'ten',
            11: 'eleven', 
            12: 'twelve', 
            13: 'thirteen', 
            14: 'fourteen', 
            15: 'fifteen', 
            16: 'sixteen',
            17: 'seventeen', 
            18: 'eighteen',
            19: 'nineteen', 
            20: 'twenty',
            30: 'thirty',
            40: 'forty',
            50: 'fifty',
            60: 'sixty',
            70: 'seventy',
            80: 'eighty',
            90: 'ninety',
         }
        
    if number < 10:
        return len(numbers[number])
        
    if number > 20 and number < 100:
        return len(dozens[number/10 * 10]) + len(numbers[(number%10)])
        
    if number > 99:
        extenso = numbers[number/100]+"hundred"
        if number%100 < 11 and number%100 != 0:
            extenso+= "and" + numbers[(number%100)] 
        return len(extenso)
    
    
    return len(dozens[number])