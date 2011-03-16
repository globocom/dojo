class Bowling
  def jogadas(jogadas)
    soma = 0
    jogadas.chars.each_with_index do |jogada, index|
      if jogada == 'X'
        soma += 30
      end
      
      if index + 1 <= jogadas.size and jogadas[index + 1] == '/'
        soma -= jogada.to_i
      end
      
      if jogada.to_i > 0
        soma += jogada.to_i
      end
            
      if jogada == '/'
        soma += 15
      end
    end
    return soma
  end
end