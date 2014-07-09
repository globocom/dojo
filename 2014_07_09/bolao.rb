require 'json'

class Bolao
  def importar_grupos(nome_arquivo)
    JSON.load(File.read(nome_arquivo))
  end

  def combinar_times(grupo)
    grupo["times"].combination(2).to_a
  end
end
