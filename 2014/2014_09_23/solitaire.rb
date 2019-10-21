class Card
  attr_reader :value, :suit

  def initialize(value, suit)
    @value = value
    @suit = suit
  end

  def color
    if @suit == "♠" or @suit == "♣"
      return "black"
    end
    "red"
  end

  def eql?(other)
    @value == other.value && @suit == other.suit
  end
end

class Board
  attr_reader :stacks, :turnable_stack, :turned_stack
  def initialize
    @turnable_stack = []
    24.times do
      @turnable_stack << Card.new("A", "♣")
    end
    @turned_stack = []
    @stacks = []
    7.times do
      @stacks << []
    end
  end

  def turn
    @turned_stack << @turnable_stack.pop
  end
end
