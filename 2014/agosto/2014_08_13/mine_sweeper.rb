require 'set'

class EndOfGame < Exception
end

class MineSweeper
  def initialize(x_size, y_size, z_size, mine_coords)
    @x_size = x_size
    @y_size = y_size
    @z_size = z_size
    @mine_coords = mine_coords
    @board = (0...@x_size).map { |x| (0...@y_size).map { |y| "#" } }
  end

  def play(x_pos, y_pos, z_pos)
    current_step = step(x_pos, y_pos, z_pos)
    @board[x_pos][y_pos] = current_step
    raise EndOfGame if current_step == "*"

    if current_step == "0"
      nearby(x_pos, y_pos, z_pos).each do |coord|
        x, y, z = coord
        if @board[x][y] == "#"
          play(x, y, 0)
        end
      end
    end
  end

  def step(x_pos, y_pos, z_pos)
    if mine? x_pos, y_pos, z_pos
      return "*"
    end
    nearby_coords = self.nearby(x_pos, y_pos, z_pos)
    cel_value = 0
    nearby_coords.each do |coord|
      x, y, z = coord
      if mine?(x, y, z)
        cel_value += 1
      end
    end
    cel_value.to_s
  end

  def nearby(x_pos, y_pos, z_pos)
    coords = [-1,0,1].repeated_permutation(3).to_a - [[0, 0, 0]]
    candidate = Set.new
    coords.each do |coord|
      x, y, z = coord
      x = x + x_pos
      y = y + y_pos
      z = z + z_pos
      if x >= 0 && y >= 0 && z >= 0 && x < @x_size && y < @y_size && z < @z_size
        candidate << [x, y, z]
      end
    end
    candidate
  end

  def solution
    (0...@x_size).map do |x|
      (0...@y_size).map do |y|
        self.step(x, y, 0)
      end
    end
  end

  def mine?(x, y, z)
    @mine_coords.include? [x, y, z]
  end

  def state
    @board
  end
end
