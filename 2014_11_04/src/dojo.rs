use std::vec::Vec;

#[deriving(PartialEq, Show)]
enum States {
  Opened,
  Closed,
  Filled,
}

struct Grid {
  grid: Vec<States>,
  line_size: uint
}

impl Grid {
  pub fn new(line_size: uint) -> Grid {
    Grid {
      grid: Vec::from_fn(line_size * line_size, |_| { Closed }),
      line_size: line_size
    }
  }

  pub fn open(&mut self, x: uint, y: uint) {
    self.grid[x * self.line_size + y] = Opened;
  }

  pub fn fill(&mut self, x: uint, y: uint) -> bool {
    if self.get_position(x, y) == Closed {
      return false;
    }

    self.fill(x, y + 1);
    self.grid[x * self.line_size + y] = Filled;
    true
  }

  pub fn get_position(&self, x: uint, y: uint) -> States {
    self.grid[x * self.line_size + y]
  }
}

#[test]
fn must_have_a_vector_of_correct_size() {
  let grid = Grid::new(10u);
  assert_eq!(grid.grid.len(), 100u);
  assert_eq!(grid.line_size, 10u);
}

#[test]
fn must_have_a_vector_of_closed_states() {
  let grid = Grid::new(10u);
  grid.grid.iter().map(|state| {
    assert_eq!(state, &Closed);
  });
}

#[test]
fn must_open_a_position() {
  let mut grid = Grid::new(10u);
  grid.open(2, 4);
  assert_eq!(grid.grid[24], Opened);
}

#[test]
fn must_return_a_position_state() {
  let mut grid = Grid::new(10u);
  assert_eq!(grid.get_position(2, 4), Closed);
  grid.open(2, 4);
  assert_eq!(grid.get_position(2, 4), Opened);
}

#[test]
fn must_not_fill_a_closed_position() {
  let mut grid = Grid::new(10u);
  let worked = grid.fill(2, 4);
  assert_eq!(worked, false);
  assert_eq!(grid.grid[24], Closed);
}

#[test]
fn must_fill_an_open_position() {
  let mut grid = Grid::new(10u);
  grid.open(2, 4);
  let worked = grid.fill(2, 4);
  assert_eq!(worked, true);
  assert_eq!(grid.get_position(2, 4), Filled);
}

#[test]
fn must_fill_two_positions() {
  let mut grid = Grid::new(10u);
  grid.open(2, 3);
  grid.open(2, 4);
  let worked = grid.fill(2, 3);
  assert_eq!(worked, true);
  assert_eq!(grid.get_position(2, 3), Filled);
  assert_eq!(grid.get_position(2, 4), Filled);
}

#[test]
fn must_not_fill_out_of_bounds() {
  let mut grid = Grid::new(10u);
  grid.open(2, 9);
  let worked = grid.fill(2, 3);
  assert_eq!(worked, true);
  assert_eq!(grid.get_position(2, 3), Filled);
  assert_eq!(grid.get_position(2, 4), Filled);
}
