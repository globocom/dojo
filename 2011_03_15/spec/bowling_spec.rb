require File.expand_path(File.dirname(__FILE__) + '/../bowling')

describe Bowling, "strike" do
  it "sequencia de 10 strikes o resultado deve ser 300 pontos" do
    subject.jogadas("XXXXXXXXXX").should == 300
  end

  it "sequencia de 10 jogadas e nenhum acerto" do
    subject.jogadas("--------------------").should == 0
  end

  it "sequencia de 10 spares" do
    subject.jogadas('1/1/1/1/1/1/1/1/1/1/').should == 150
  end

  it "o cara era ruim e derrubou apenas 8 pinos na primeira jogada" do
    subject.jogadas('8-------------------').should == 8
  end

  it "se o cara errar a primeira jogada e derrubar todas na seguda ele fez um spare" do
    subject.jogadas('-/------------------').should == 15
  end

  it "se o cara acertar 6 e depois acertar 2 deve ganhar 8 pontos" do
    subject.jogadas('62------------------').should == 8
  end

  it "se o cara acertar strike e spare e errar o resto" do
    subject.jogadas('X--6/--------------').should == 45
  end

  it "se o cara acertar strikes, spares e jogadas normais e errar o resto" do
    subject.jogadas('X--6/62------------').should == 53
  end
end

