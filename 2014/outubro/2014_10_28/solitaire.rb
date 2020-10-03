require 'forwardable'

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

  def hash
    (@value + @suit).hash
  end
end

class Board
  attr_reader :stacks, :turnable_stack, :turned_stack, :completed_stacks
  def initialize
    deck = Deck.new
    @turned_stack = []
    @turnable_stack = []
    24.times do
      @turnable_stack << deck.pop
    end

    @stacks = []
    7.times do |index|
      @stacks[index] = []
      (index + 1).times do
        @stacks[index] << deck.pop
      end
    end

    @completed_stacks = [[]] * 4
  end

  def turn
    card = @turnable_stack.pop
    if card.nil?
      @turnable_stack = @turned_stack
      @turned_stack = []
    else
      @turned_stack.insert(0, card)
    end
  end
end

class Deck
  extend Forwardable

  attr_reader :cards
  def_delegator :@cards, :pop

  VALUES = %w(2 3 4 5 6 7 8 9 10 J Q K A)
  SUITS = %w(♠ ♥ ♦ ♣)

  def initialize
    @cards = VALUES.map do |value|
      SUITS.map do |suit|
        Card.new(value, suit)
      end
    end.flatten
    @cards.shuffle!
  end
end
