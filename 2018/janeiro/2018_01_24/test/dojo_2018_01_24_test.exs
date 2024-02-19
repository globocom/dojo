defmodule Dojo20180124Test do
  use ExUnit.Case
  import Dojo20180124
  
  describe "sum of digits" do
    test "12 should result in 3" do
      assert sum_of_digits(12) == 3
    end
    test "100233 should result in 9" do
      assert sum_of_digits(100233) == 9
    end
    test "0 should result in 0" do
      assert sum_of_digits(0) == 0
    end
    test "12345 should result in 15" do
      assert sum_of_digits(12345) == 15
    end
  end

  describe "count_match" do
  	test "6 should result in 1" do
  	  assert count_match(6) == 1
  	end

  	test "9939 should result in 4" do
  	  assert count_match(9939) == 4
  	end

  	test "0 should result in 1" do
  	  assert count_match(0) == 1
  	end
  end
end
