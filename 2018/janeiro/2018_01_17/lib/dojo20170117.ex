defmodule Dojo do

  def full_solve(field) do
    field
    |> slots_map(fn
      "*", _x, _y -> "*"
      ".", x, y ->
        field
        |> slots_around(x, y)
        |> Enum.count(fn slot -> slot == "*" end)
        |> to_string
    end)
  end

  def solve(field) do
    field
    |> Enum.with_index
    |> Enum.map(fn {slot, i} ->

      if slot == "." do
        if Enum.at(field, i+1, 0) == "*" do
          1
        else
          0
        end
      else
        "*"
      end
    end)
  end

  defp slots_map(field, function) do
    field
    |> Enum.with_index
    |> Enum.map(fn {line, y} ->
      line
      |> Enum.with_index
      |> Enum.map(fn {slot, x} ->
        function.(slot, x, y)
      end)
    end)
  end

  defp slots_around(field, x, y) do
    field
    |> Enum.slice(Enum.max([0,y-1])..(y+1))
    |> Enum.flat_map(fn row ->
      Enum.slice(row, Enum.max([0,x-1])..(x+1))
    end)
  end
end
