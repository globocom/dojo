require 'set'

class EndOfGame < Exception
end

class MineSweeper
  def initialize(rows, cols, mine_coords)
    @rows = rows
    @cols = cols
    @mine_coords = mine_coords
    @board = (0...@rows).map { |row| (0...@cols).map { |col| "#" } }
  end

  def play(row, col)
    current_step = step(row, col)
    @board[row][col] = current_step
    raise EndOfGame if current_step == "*"

    if current_step == "0"
      nearby(row, col).each do |coord|
        r, c = coord
        if @board[r][c] == "#"
          play(r, c)
        end
      end
    end
  end

  def step(row, col)
    if mine? row, col
      return "*"
    end
    nearby_coords = self.nearby(row, col)
    cel_value = 0
    nearby_coords.each do |coord|
      x, y = coord
      if mine?(x, y)
        cel_value += 1
      end
    end
    cel_value.to_s
  end

  def nearby(row, col)
    coords = [[-1, 0],
              [-1, 1],
              [0, 1],
              [1, 1],
              [1, 0],
              [1, -1],
              [0, -1],
              [-1, -1]]
    candidate = Set.new
    coords.each do |coord|
      x, y = coord
      x = x + row
      y = y + col
      if x >= 0 && y >= 0 && x < @rows && y < @cols
        candidate << [x, y]
      end
    end
    candidate
  end

  def solution
    (0...@rows).map do |row|
      (0...@cols).map do |col|
        self.step(row, col)
      end
    end
  end

  def mine?(x, y)
    @mine_coords.include? [x, y]
  end

  def state
    @board
  end
end
