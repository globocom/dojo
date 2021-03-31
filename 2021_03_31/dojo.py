def append_string_value(c, value):
    if len(value) == 0:
        return c
    
    return (int(value)*c) 


def main(input_string, max_length):
    value = ""
    decoded_string = ""
    for c in input_string:
        if c.isdigit():
            value = value + c
        else:
            decoded_string += append_string_value(c,value)
        
            if len(decoded_string) > max_length:
                return "unfeasible"

            value = ""

    return decoded_string



def encode_value(value, previous_letter):
    if value == 1:
        return previous_letter
    
    return str(value) + previous_letter   

def encode_string(decoded_string):
    previous_letter = decoded_string[0]
    value = 0
    encoded_string = ""
    for c in decoded_string:
        if c == previous_letter:
            value += 1
        else:
            encoded_string += encode_value(value, previous_letter)
        
            value = 1
            previous_letter = c

    encoded_string += encode_value(value, previous_letter)
    
    return encoded_string
    
    # if decoded_string == "abcd":
    #     return "abcd"
    # if decoded_string == "aaaaabbc":
    #     return "5a2bc"
    # else:
    #     return "asdf4x"

# Celso - Ingrid - Lara - Tiago - Juan


#input
#5a2bc 8
#output
#aaaaabbc

#input
#5a2bc 7 => aaaaabbc (length: 8)
#output
#unfeasible

#input
#asdf4x 50
#output
#asdfxxxx

#input
#asjkdf10000000000kz 1000000
#output
#unfeasible

#func com o objetivo de formar o numero