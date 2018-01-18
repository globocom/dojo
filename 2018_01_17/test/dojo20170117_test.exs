defmodule Dojo20170117Test do
  use ExUnit.Case

  test "matrix 2x1 without mines" do
  	solution = Dojo.solve([".","."])
    assert solution == [0, 0]
  end

  test "matrix 2x1 with one mine" do
  	solution = Dojo.solve([".","*"])
	assert solution == [1, "*"]
  end

  test "matrix 2x1 with two mines" do
  	solution = Dojo.solve(["*","*"])
	assert solution == ["*", "*"]
  end

  test "matrix 2x1 with one mine 2" do
  	solution = Dojo.solve(["*","."])
	assert solution == ["*", 1]
  end

  # test "matrix 2x2 with two mines" do
  # 	solution = Dojo.solve([
  # 		["*", "*"],
  # 		[".", "."]
  # 	])
  # 	assert solution == [
  # 		["*", "*"],
  # 		[2  , 	2]
  # 	]
  # end
end
