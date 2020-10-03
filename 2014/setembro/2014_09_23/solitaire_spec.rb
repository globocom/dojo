require 'rspec'
require_relative './solitaire'

describe Card do
  it "deveria criar uma carta com valor e naipe" do
    card = Card.new("A", "♠")
    expect(card.value).to eql "A"
    expect(card.suit).to eql "♠"
  end

  it "deveria retornar a cor do naipe" do
    expect(Card.new("A", "♠").color).to eql "black"
    expect(Card.new("A", "♣").color).to eql "black"

    expect(Card.new("A", "♥").color).to eql "red"
    expect(Card.new("A", "♦").color).to eql "red"
  end

  it "deveria ser igual" do
    expect(Card.new("A", "♦")).to eql(Card.new("A", "♦"))
  end

  it "deveria ser diferente" do
    expect(Card.new("K", "♦")).not_to eql(Card.new("A", "♦"))
  end
end


# describe GarnierDeck do
#
#   it "deveria ter 52 cartas" do
#     deck = GarnierDeck.new
#     expect(deck.cards.uniq.size).to eql(52)
#   end
#
# end


describe Board do
  it "deveria ter 7 pilhas" do
    board = Board.new
    expect(board.stacks.size).to eql(7)
  end
  describe "Estruturas viráveis" do
    it "deveria ter uma pilha virável" do
      board = Board.new
      expect(board.turnable_stack).to be_kind_of Array
    end

    it "deveria ter inicialmente uma pilha virável com 24 cartas" do
      board = Board.new
      expect(board.turnable_stack.size).to eql(24)
    end

    it "deveria ter uma pilha virada" do
      board = Board.new
      expect(board.turned_stack).to be_kind_of Array
    end

    it "deveria virar apenas uma carta" do
      board = Board.new
      expect(board.turnable_stack.size).to eql 24
      expect(board.turned_stack.size).to eql 0

      card = board.turnable_stack.last

      board.turn
      expect(board.turnable_stack.size).to eql 23
      expect(board.turned_stack.size).to eql 1

      expect(board.turned_stack.last).to eql(card)
    end
  end
end
