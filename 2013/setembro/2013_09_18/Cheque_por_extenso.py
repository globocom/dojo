#coding utf-8

table = { 1 : "um", 
          2 : "dois",
          10: "dez" }

plural = {"real": "reais",
          "centavo": "centavos"}

def convert_number(value, currency="real"):
    if value == 0:
        return ""
    #if value < 0:
    #    raise Exception("Invalid value {0:d}".format(value))        
    number_string = table[value]
    if value > 1:
        currency = plural[currency]
    return "{0} {1}".format(number_string, currency)
    
def convert(value):
    quotient, remainder = divmod(value, 1)
    number_digit = int(quotient)
    convert_number()
    if number_digit > 0:
        number_string = table[number_digit]
        currency = "real"
        if number_digit > 1:
            currency = "reais"
        return "{0} {1}".format(number_string,currency)
    else:
        remainder = int(remainder * 100)
        remainder_string = table[remainder]
        currency = "centavo"
        if remainder > 1:
            currency = "centavos"
        return "{0} {1}".format(remainder_string,currency)