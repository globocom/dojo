class Anagrama
  def gera_anagramas(palavra)
    arr = []
    if palavra.size == 2
      arr << palavra
      arr << palavra.reverse
      return arr
    end
  
    palavra.split("").each do |letra|
      substring = palavra.delete(letra)
      new_array = gera_anagramas(substring)
      new_array.each do |pos|
        arr << letra + pos
      end
    end

    return arr
  end
end