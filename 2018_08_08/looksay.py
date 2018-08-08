def main(number):
    if len(str(number)) == 1:
        return 10 + number
    else:
        if str(number)[0] == str(number)[1]:
            result = '2' + str(number)[0]
            return int(result)
        else:
            result = '1' + str(number)[0] + '1' + str(number)[1]
            return int(result)


