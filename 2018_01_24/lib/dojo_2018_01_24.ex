defmodule Dojo20180124 do
  def sum_of_digits(0), do: 0
  def sum_of_digits(n) do
    last_digit = rem(n, 10)
    rest = div(n,10)
    last_digit + sum_of_digits(rest)
  end

  def count_match(n) do
    Enum.count(0..n, fn x ->
      n == x + sum_of_digits(x) + (x |> sum_of_digits |> sum_of_digits)
    end)
  end
end
