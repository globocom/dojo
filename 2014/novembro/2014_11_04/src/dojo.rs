use std::vec::Vec;
use std::fmt::Show;
use std::fmt::Formatter;
use std::fmt::FormatError;

#[deriving(PartialEq)]
enum States {
  Opened,
  Closed,
  Filled,
}

impl Show for States {
  fn fmt(&self, f: &mut Formatter) -> Result<(), FormatError> {
    match *self {
      Opened => " ".fmt(f),
      Closed => "#".fmt(f),
      Filled => ".".fmt(f)
    }
  }
}

pub struct Grid {
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
    match self.get_position(x, y) {
      Err(_) => return false,
      Ok(value) if value == Closed => return false,
      Ok(value) if value == Filled => return false,
      Ok(_) => {
        self.grid[x * self.line_size + y] = Filled;
        self.fill(x, y + 1);
        self.fill(x, y - 1);
        self.fill(x + 1, y);
        self.fill(x - 1, y);
        return true
      }
    }
  }

  pub fn get_position(&self, x: uint, y: uint) -> Result<States, &str> {
    if x < self.line_size && y < self.line_size {
      Ok(self.grid[x * self.line_size + y])
    } else {
      Err("Grid Out Of Bounds")
    }
  }

  pub fn print(&self) {
    for i in range(0, self.line_size) {
      for j in range(0, self.line_size) {
        print!("{}", self.get_position(j, i).unwrap());
      }
      print!("\n");
    }
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
  assert_eq!(grid.get_position(2, 4), Ok(Closed));
  grid.open(2, 4);
  assert_eq!(grid.get_position(2, 4), Ok(Opened));
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
  assert_eq!(grid.get_position(2, 4), Ok(Filled));
}

#[test]
fn must_fill_two_positions_on_top_of_each_other() {
  let mut grid = Grid::new(10u);
  grid.open(2, 3);
  grid.open(2, 4);
  let worked = grid.fill(2, 3);
  assert_eq!(worked, true);
  assert_eq!(grid.get_position(2, 3), Ok(Filled));
  assert_eq!(grid.get_position(2, 4), Ok(Filled));
}

#[test]
fn must_fill_position_to_the_right() {
  let mut grid = Grid::new(10u);
  grid.open(2, 3);
  grid.open(3, 3);
  let worked = grid.fill(2, 3);
  assert_eq!(worked, true);
  assert_eq!(grid.get_position(2, 3), Ok(Filled));
  assert_eq!(grid.get_position(3, 3), Ok(Filled));
}

#[test]
fn must_fill_position_to_the_left() {
  let mut grid = Grid::new(10u);
  grid.open(2, 3);
  grid.open(3, 3);
  let worked = grid.fill(3, 3);
  assert_eq!(worked, true);
  assert_eq!(grid.get_position(2, 3), Ok(Filled));
  assert_eq!(grid.get_position(3, 3), Ok(Filled));
}

#[test]
fn must_not_spill_when_filling() {
  let mut grid = Grid::new(10u);
  grid.open(9, 9);
  let worked = grid.fill(9, 9);
  assert_eq!(worked, true);
  assert_eq!(grid.get_position(9, 9), Ok(Filled));
}

#[test]
fn must_not_accept_higher_than_grid() {
  let grid = Grid::new(5);
  assert_eq!(grid.get_position(6, 0), Err("Grid Out Of Bounds"));
}

#[test]
fn must_not_accept_wider_than_grid() {
  let grid = Grid::new(5);
  assert_eq!(grid.get_position(0, 6), Err("Grid Out Of Bounds"));
}

#[test]
fn must_fill_whole_grid() {
  let mut grid = Grid::new(5);
  for i in range(0, 5) {
    for j in range(0, 5) {
      grid.open(i, j);
    }
  }
  let worked = grid.fill(2, 2);
  assert_eq!(worked, true);
  for i in range(0, 5) {
    for j in range(0, 5) {
      assert_eq!(grid.get_position(i, j), Ok(Filled));
    }
  }
}

#[test]
fn must_dojo() {
  let mut grid = Grid::new(8);
  grid.open(2, 0);
  grid.open(3, 0);
  grid.open(5, 0);
  grid.open(0, 1);
  grid.open(1, 1);
  grid.open(2, 1);
  grid.open(3, 1);
  grid.open(4, 1);
  grid.open(0, 2);
  grid.open(1, 2);
  grid.open(4, 2);
  grid.open(5, 2);
  grid.open(2, 3);
  grid.open(3, 3);
  grid.open(4, 3);
  grid.open(5, 3);
  grid.open(6, 3);
  grid.open(0, 4);
  grid.open(6, 4);
  grid.open(7, 4);
  grid.open(1, 5);
  grid.open(3, 5);
  grid.open(4, 5);
  grid.open(5, 5);
  grid.open(1, 6);
  grid.open(2, 6);
  grid.open(4, 6);
  grid.open(5, 6);
  grid.open(7, 6);
  grid.open(0, 7);
  grid.open(2, 7);
  grid.open(6, 7);
  grid.fill(2, 0);

  grid.print();

  assert_eq!(grid.get_position(5, 2), Ok(Filled))
  assert_eq!(grid.get_position(0, 7), Ok(Opened))
}
