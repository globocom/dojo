defmodule LastDojoTest do
  use ExUnit.Case
  doctest LastDojo

  test "FizzBuzz 3" do
    assert LastDojo.fizz_buzz(3) == "Fizz"
  end

  test "FizzBuzz 5" do
    assert LastDojo.fizz_buzz(5) == "Buzz"
  end

  test "FizzBuzz" do
    assert LastDojo.fizz_buzz(15) == "FizzBuzz"
  end

  test "FizzBuzz 30" do
    assert LastDojo.fizz_buzz(30) == "FizzBuzz"
  end

  test "Empty 2" do
    assert LastDojo.fizz_buzz(2) == ""
  end

  test "FizzBuzz 9" do
    assert LastDojo.fizz_buzz(9) == "Fizz"
  end

  test "FizzBuzz 9.0" do
    assert_raise(FunctionClauseError, fn ->
      LastDojo.fizz_buzz(9.0) == "Fizz"
    end)
  end

  test "FizzBuzz 10" do
    assert LastDojo.fizz_buzz(10) == "Buzz"
  end

  test "FizzBuzz does not break if a word is passed" do
    assert_raise(FunctionClauseError, fn ->
      LastDojo.fizz_buzz("Opa")
    end)
  end

end
