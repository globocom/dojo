defmodule Dojo do

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
end
