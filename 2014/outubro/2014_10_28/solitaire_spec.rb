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


describe Deck do

  let :deck do
    Deck.new
  end

  it "deveria ter todas as cartas válidas" do
    expect(deck.cards.all? do |card|
      Deck::VALUES.include? card.value and Deck::SUITS.include? card.suit
    end).to be true
  end

  it "deveria ter 52 cartas diferentes" do
    expect(deck.cards.size).to eql(52)
    expect(deck.cards.size).to eql(deck.cards.uniq.size)
  end

  it "deveria retorna uma carta do deck" do
    expect(deck.pop).to be_kind_of(Card)
    expect(deck.cards.size).to eql(51)
  end
end


describe Board do
  let :board do
    Board.new
  end

  it "deveria ter 7 pilhas" do
    expect(board.stacks.size).to eql(7)
  end

  describe "Estruturas viráveis" do
    it "deveria ter uma pilha virável" do
      expect(board.turnable_stack).to be_kind_of Array
    end

    it "deveria ter inicialmente uma pilha virável com 24 cartas diferentes" do
      expect(board.turnable_stack.size).to eql(24)
      expect(board.turnable_stack.size).to eql(board.turnable_stack.uniq.size)
    end

    it "deveria ter uma pilha virada" do
      expect(board.turned_stack).to be_kind_of Array
    end

    it "deveria virar apenas uma carta" do
      expect(board.turnable_stack.size).to eql 24
      expect(board.turned_stack.size).to eql 0

      card = board.turnable_stack.last

      board.turn
      expect(board.turnable_stack.size).to eql 23
      expect(board.turned_stack.size).to eql 1

      expect(board.turned_stack.last).to eql(card)
    end

    it "deveria trocar turned por turnable quando acabarem as cartas" do
      cards = board.turnable_stack.clone

      25.times do
        board.turn
      end

      expect(board.turnable_stack).to eql cards
      expect(board.turned_stack.size).to eql 0
    end

    it "deveria ter 7 pilhas com 1 a 7 cartas" do
      expect(board.stacks.size).to eql 7
      board.stacks.each_with_index do |stack, index|
        expect(stack.size).to eql(index + 1)
      end
    end

    it "deveria criar 1 lista com 4 listas vazias" do
      expect(board.completed_stacks.size).to eql(4)
      expect(board.completed_stacks.all? do |list|
        list.empty?
      end).to be true
    end
  end
end
