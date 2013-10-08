require './anagrama'

describe  "Anagrama" do 
  it "entra ab e retorna ab, ba" do
    ana = Anagrama.new
    ana.gera_anagramas("ab").should == ["ab", "ba"]
  end

  it "entra tres letras e retorna 6 anagramas" do
    ana = Anagrama.new
    ana.gera_anagramas("abc").size.should == 6
  end

  it "entra abc e retorna abc, acb, bac, bca, cab, cba" do
    ana = Anagrama.new
    ana.gera_anagramas("abc").should == ["abc", "acb", "bac", "bca", "cab", "cba"]
  end
end
