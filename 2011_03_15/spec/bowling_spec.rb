require File.expand_path(File.dirname(__FILE__) + '/../bowling')

describe Bowling do
  describe "#jogadas" do
    it "10 strikes deve pontuar 300" do
      subject.jogadas("XXXXXXXXXX").should == 300
    end

    it "Se errar todas as jogadas, deve pontuar 0" do
      subject.jogadas("--------------------").should == 0
    end

    it "Uma sequencia de 10 spares deve pontuar 150" do
      subject.jogadas('1/1/1/1/1/1/1/1/1/1/').should == 150
    end

    it "Apenas 8 pinos na primeira jogada e depois errar todas deve pontuar 8" do
      subject.jogadas('8-------------------').should == 8
    end

    it "Se errar a primeira jogada, fizer um spare e depois errar todas, deve pontuar 15" do
      subject.jogadas('-/------------------').should == 15
    end

    it "Se o cara acertar 6 e depois acertar 2 deve pontuar 8" do
      subject.jogadas('62------------------').should == 8
    end

    it "Se o cara acertar 1 strike, 1 spare e errar todas deve pontuar 45" do
      subject.jogadas('X--6/--------------').should == 45
    end

    it "Se o cara acertar strikes, spares, 6 e 2 e errar o resto, deve pontuar 53" do
      subject.jogadas('X--6/62------------').should == 53
    end

    it "9 strikes e 1 spare deve pontuar 285" do
      subject.jogadas("XXXXXXXXX1/").should == 285
    end

    it "8 strikes e 2 spares deve pontuar 270" do
      subject.jogadas("XXXXXXXX1/1/").should == 270
    end

    it "7 strikes e 3 spares deve pontuar 255" do
      subject.jogadas("XXXXXXX1/1/1/").should == 255
    end

    it "1 strike  e 9 spares deve pontuar 165" do
       subject.jogadas("X1/1/1/1/1/1/1/1/1/").should == 165
    end

    it "8 strikes, 1 spare e 2 erros deve pontuar 255" do
      subject.jogadas("XXXXXXXX1/--").should == 255
    end

    it "8 strikes, 1 spare, 2 e 6 deve pontuar 263" do
      subject.jogadas("XXXXXXXX1/26").should == 263
    end

    it "7 strikes, 1 spare, 2 e 6 e 2 erros deve pontuar 235" do
      subject.jogadas("XXXXXXX1/26--").should == 233
    end
  end

end

