defmodule LastDojo do
  @moduledoc """
  Documentation for LastDojo.
  """

  def fizz_buzz(number) when is_integer(number) do
    cond do
      rem(number, 15) == 0 -> "FizzBuzz"
      rem(number, 3) == 0 -> "Fizz"
      rem(number, 5) == 0 -> "Buzz"
      true -> ""
    end
  end
end
