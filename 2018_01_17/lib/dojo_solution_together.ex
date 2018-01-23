defmodule DojoSolutionTogether do
  def full_solve(field) do
    field
    |> map_field(fn
      "*", _x, _y -> "*"
      cell, x, y ->
        sum = 0
        sum = sum + (getm(field, x-1, y-1) |> cell_value)
        sum = sum + (getm(field, x  , y-1) |> cell_value)
        sum = sum + (getm(field, x+1, y-1) |> cell_value)
        sum = sum + (getm(field, x-1, y) |> cell_value)
        #sum=sum +  (getm(field, x  , y) |> cell_value)
        sum = sum + (getm(field, x+1, y) |> cell_value)
        sum = sum + (getm(field, x-1, y+1) |> cell_value)
        sum = sum + (getm(field, x  , y+1) |> cell_value)
        sum = sum + (getm(field, x+1, y+1) |> cell_value)
        sum |> to_string
    end)
  end

  defp map_field(field, function) do
    field
    |> Enum.with_index
    |> Enum.map(fn {row, y} ->
      row
      |> Enum.with_index
      |> Enum.map(fn {cell, x} ->
        function.(cell, x, y)
      end)
    end)
  end

  defp getm(field, x, y) when x >= 0 and y >= 0 do
    field
    |> Enum.at(y, [])
    |> Enum.at(x, ".")
  end
  defp getm(_field, _x, _y), do: "."

  defp cell_value("*"), do: 1
  defp cell_value(_), do: 0
end
