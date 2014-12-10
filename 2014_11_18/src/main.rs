use std::io::{BufferedReader, BufReader, File, stdin};

fn main() {
    let result = stdin().read_line().unwrap();
    let numbers: Vec<&str> = result.split(' ').collect();
}

fn read_board_size<T>(reader: &mut BufferedReader<T>)
   -> (uint, uint) where T: Reader {
    let result = reader.read_line().unwrap();
    let numbers: Vec<&str> = result.split(' ').collect();
    (from_str(numbers[0].trim()).unwrap(), from_str(numbers[1].trim()).unwrap())
}

fn read_board<T>(reader: &mut BufferedReader<T>, lines: uint, cols: uint)
  -> Vec<Vec<char>> where T: Reader {
    let mut board = Vec::new();
    for i in range(0, lines) {
      let result = reader.read_line().unwrap();
      let line = result.into_ascii();
      board.push(Vec::new());
      for j in range(0, cols) {
        board[i].push(line[j].as_char());
      }
    }
    board
}

fn mark_shots<T>(board: &mut Vec<Vec<char>>, shots_reader: &mut BufferedReader<T>)
  where T: Reader {
    let count: int = from_str(shots_reader.read_line().unwrap().trim()).unwrap();
    for _ in range(0, count) {
        let line_shot = shots_reader.read_line().unwrap().trim().clone();
        let shot: Vec<&str> = line_shot.split(' ').collect();
        let x = from_str::<uint>(shot[0]).unwrap() - 1;
        let y = from_str::<uint>(shot[1]).unwrap() - 1;
        if board[x][y] == '#' {
          board[x][y] = 'X';
        }
    }
}

// fn neighborhood<T>(board: &mut Vec<Vec<char>>, point)

// fn count_shots<T>(board: &Vec<Vec<char>>) -> uint {
//   let mut count: int = 0;
//   for i in range(0, board.len()) {
//     for j in range(0, board[0].len()) {
//       if !neighborhood(board[i][j]).contains('#') {
//         count++;
//       }
//     }
//   }
//   return count;
// }

#[test]
fn test_neighborhood() {
  let file = File::open(&Path::new("test_read_board.txt"));
  let mut reader = BufferedReader::new(file);
  let board = read_board(&mut reader, 5, 5);

  let point = Vec::new();
  point.push_all([2, 3]);
  let neighbors = Vec::new();
  neighbors.push_all(['.', '.', '.', '.']);
  assert_eq!(neighborhood(board, point), neighbors)
}

// #[test]
// fn test_count_destroyed_ships() {
//   let board_file = File::open(&Path::new("test_shot_board.txt"));
//   let mut board_reader = BufferedReader::new(board_file);
//   let mut board = read_board(&mut board_reader, 5, 5);
//
//   let count = count_shots(&board);
//   assert_eq!(count, 2);
// }

#[test]
fn test_read_board() {
    let file = File::open(&Path::new("test_read_board.txt"));
    let mut reader = BufferedReader::new(file);
    let board = read_board(&mut reader, 5, 5);
    assert_eq!(board.len(), 5);
    for line in board.iter() {
      assert_eq!(line.len(), 5);
    }
}

#[test]
fn test_read_shots() {
    let board_file = File::open(&Path::new("test_read_board.txt"));
    let mut board_reader = BufferedReader::new(board_file);
    let mut board = read_board(&mut board_reader, 5, 5);

    let shots_file = File::open(&Path::new("test_read_shots.txt"));
    let mut shots_reader = BufferedReader::new(shots_file);

    mark_shots(&mut board, &mut shots_reader);

    assert_eq!(board[0][2], 'X');
    assert_eq!(board[0][4], 'X');
    assert_eq!(board[1][0], 'X');
    assert_eq!(board[2][3], 'X');
}

#[test]
fn test_read_water_shots() {
  let board_file = File::open(&Path::new("test_read_board.txt"));
  let mut board_reader = BufferedReader::new(board_file);
  let mut board = read_board(&mut board_reader, 5, 5);

  let shots_file = File::open(&Path::new("test_read_shots.txt"));
  let mut shots_reader = BufferedReader::new(shots_file);

  mark_shots(&mut board, &mut shots_reader);

  assert_eq!(board[0][3], '.');
}

#[test]
fn test_read_board_size() {
    let file = File::open(&Path::new("test_read_board_size.txt"));
    let mut reader = BufferedReader::new(file);
    assert_eq!(read_board_size(&mut reader), (10, 20));
}
