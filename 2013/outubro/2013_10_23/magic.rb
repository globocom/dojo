# encoding: utf-8

require 'test/unit'

MAGIC_SUM = 15

#[[7, 6, 2], ...]
def convert_str_to_square(text)
  lines = text.strip.split(/\n/) #["7 6 2", "5 1 8"]

  lines.map do |line|
    line.split.map(&:to_i)
  end
end

def validate(square)
  square.rows.all? do |row|
    row.reduce(&:+) == MAGIC_SUM
  end
end

class Square

  attr_accessor :square

  def initialize(input_square)
    if input_square.is_a?(String)
      @square = convert_str_to_square(input_square)
    else
      @square = input_square
    end

    @side = @square.size
  end

  def rows
    @square
  end

  def columns
  	cols = []

  	@side.times do |index|
  		col = []
	  	@square.each do |row|
	  		col << row[index]
	  	end

	  	cols << col
	  end
	  cols
  end

  def diagonals
  	diags = []
  	opposite_diag = []

  	@side.times do |index|
  		diags << @square[index][index]  	
  		opposite_diag << @square[index][@side-index-1]
	end
	[diags,opposite_diag]
  end

end

class DojoTestCase < Test::Unit::TestCase

  def test_convert_str_to_square_3x3
    example = <<-TXT
    1 2 3
    4 5 6
    7 8 9
    TXT
    assert_equal(convert_str_to_square(example), [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
  end

  def test_convert_str_to_square_2x2
    example = """
    1 2
    3 4
    """
    assert_equal(convert_str_to_square(example), [[1, 2], [3, 4]])
  end

  def test_validate_invalid_3x3
    array = [
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]
    ]
    square = Square.new(array)
    assert_equal(validate(square), false)
  end

  def test_validate_valid_3x3
  	array = [
		[7, 6, 2],
		[5, 1, 9],
		[3, 8, 4]
  	]
	square = Square.new(array)
    assert_equal(validate(square), true)
  end

  def test_validate_columns_2x2
  	array = [
  		[1,2],
  		[3,4]
  	]

  	square = Square.new(array)
  	assert_equal(square.columns, [[1,3],[2,4]])
  end

  def test_validate_diagonals_2x2
  	array = [
  		[1,2],
  		[3,4]
  	]
  	square = Square.new(array)
  	assert_equal(square.diagonals, [[1,4],[2,3]])
  end
end
