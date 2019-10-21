require "rspec"
require_relative "mine_sweeper"

describe MineSweeper do

  describe "Coordinates" do
    it "Nearby Coords upper left corner" do
      board = MineSweeper.new(2, 2, [])
      expect(board.nearby(0, 0)).to eql [[0, 1], [1, 0], [1, 1]].to_set
    end

    it "Nearby Coords lower right corner" do
      board = MineSweeper.new(2, 2, [])
      expect(board.nearby(1, 1)).to eql [[0,0], [0, 1], [1, 0]].to_set
    end
  end

  describe "Is mine" do
    it "must be true" do
      board = MineSweeper.new(1, 1, [[0,0]])
      expect(board.mine?(0, 0)).to eql true
    end
    it "must be false" do
      board = MineSweeper.new(1, 1, [])
      expect(board.mine?(0, 0)).to eql false
    end
  end

  describe "step" do
    it "must return 0 without mines" do
      board = MineSweeper.new(2, 2, [])
      expect(board.step(0, 0)).to eql "0"
    end

    it "must return 8 surrounded by mines" do
      board = MineSweeper.new(3, 3, [[0, 0], [0, 1], [0, 2], [1, 0], [1, 2], [2, 0], [2, 1], [2, 2]])
      expect(board.step(1, 1)).to eql "8"
    end
  end

  context "Solution" do
    it "must show 0 without mines" do
      board = MineSweeper.new(2, 2, [])
      expect(board.solution).to eql [["0", "0"], ["0", "0"]]
    end

    it "must show 0 without mines" do
      board = MineSweeper.new(4, 4, [[0, 0], [2, 1]])
      expect(board.solution).to eql [["*", "1", "0", "0"],
                                     ["2", "2", "1", "0"],
                                     ["1", "*", "1", "0"],
                                     ["1", "1", "1", "0"]]

    end
  end
end
