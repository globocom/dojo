# TODO conceito de strikes e spares se repete
class Bowling

  def pontuacao_para(jogadas)

    resultado  = conta_pontuacao_para_strikes(jogadas)
    resultado += conta_pontuacao_para_spares(jogadas)

    moves      = remover_jogadas_computadas(jogadas, [/X/, /\d{1}\//, /-/])

    resultado += conta_pontuacao_para_acertos(jogadas) unless jogadas.empty?

    return resultado
  end

  def conta_pontuacao_para_strikes(jogadas)
    jogadas.count('X') * 30
  end

  def conta_pontuacao_para_spares(jogadas)
    jogadas.count('/') * 15
  end

  private
    def conta_pontuacao_para_acertos(jogadas)
      jogadas.chars.collect(&:to_i).inject(&:+)
    end

    def remover_jogadas_computadas(jogadas, para_remover)
      para_remover.each { |pattern| jogadas.gsub!(pattern, '') }
      jogadas
    end
end

