defmodule Dojo20170117Test do
  use ExUnit.Case

  describe "simple solve" do
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
  end

  describe "full solve" do
    test "matrix 2x2 full of mines" do
      solution = Dojo.full_solve([
        ~w[* *],
        ~w[* *],
      ])
      assert solution == [
        ~w[* *],
        ~w[* *],
      ]
    end

    test "matrix 2x2 with three mines" do
      solution = Dojo.full_solve([
        ~w[. *],
        ~w[* *],
      ])
      assert solution == [
        ~w[3 *],
        ~w[* *],
      ]
    end

    test "matrix 2x2 with no mines" do
      solution = Dojo.full_solve([
        ~w[. .],
        ~w[. .],
      ])
      assert solution == [
        ~w[0 0],
        ~w[0 0],
      ]
    end

    test "matrix 3x3 with 3 mines" do
      solution = Dojo.full_solve([
        ~w[* * .],
        ~w[* . .],
        ~w[. . .],
      ])
      assert solution == [
        ~w[* * 1],
        ~w[* 3 1],
        ~w[1 1 0],
      ]
    end
  end
end
