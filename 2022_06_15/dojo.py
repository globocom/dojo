def validate_phrase(phrase):
    # words = {}
    words = set()

    for word in phrase:
        if word in words:
            return False
        # words[word] = 1
        words.add(word)

    return True

def day_part_one(input):
    count = 0
    for line in input.split("\n"):
        if validate_phrase(line.split(' ')):
            count += 1

    return count

def validate_phrase2(phrase):
    words = {}

    for word in phrase:
        sorted_word = ''.join(sorted(word))
        if sorted_word in words:
            return False
        words[sorted_word] = 1

    return True

def day_part_two(input):
    count = 0
    for line in input.split("\n"):
        if validate_phrase2(line.split(' ')):
            count += 1

    return count

# part 1
# 1 - Quebrar a linha por palavra

# 2 - Adicionar em um dicionario
# 2.1 - Se ja tiver a palavra retorna false

# 2 - Adiconar em um set
# 2.1 - apos adicionar todas as palavras
# 2.2 - validar o size do set com a lista original

# 3 - Contar qtd de frases validas

# part 2
# 
