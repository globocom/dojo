
mod dojo;


fn main() {
let mut grid = dojo::Grid::new(8);
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
}
