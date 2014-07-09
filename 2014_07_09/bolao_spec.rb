require 'rspec'
require './bolao'

describe Bolao do
  describe "importar_grupos" do
    it "deveria importar os dados do json" do
      bolao = Bolao.new
      grupos = bolao.importar_grupos("grupos.json")
      expect(grupos.size).to eql 8
      expect(grupos.class).to eql Array
    end

    it "deveria estar com estrutura correta" do
      bolao = Bolao.new
      grupos = bolao.importar_grupos("grupos.json")
      group_names = 'ABCDEFGH'
      grupos.each_with_index do |item, index|
        expect(item["grupo"]).to eql group_names[index]
        expect(item['times'].class).to eql Array
        expect(item['times'].size).to eql 4
      end
    end
  end

  describe 'Combinacao de times' do
    it "deveria combinar times de um grupo" do
      bolao = Bolao.new
      grupos = bolao.importar_grupos("grupos.json")
      grupo = {"grupo"=> "A", "times"=> ["Brasil", "Croácia", "México", "Camarões"]}

      jogos = bolao.combinar_times(grupo)
      expect(jogos.size).to eql 6
      expect(grupo["times"].combination(2).to_a.sort).to eql jogos.sort
    end
  end
end
