def main(perguntas):
    result = []
    count = 0

    for pergunta in perguntas:
        if pergunta == "PS":
            count += 1
            result.append("PS")
            if count == 2:
                result.append("B")
                count = 0
        else:
            count = 0
            result.append(pergunta)
            result.append("B")

    return result
