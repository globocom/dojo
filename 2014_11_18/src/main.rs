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
    board[0][2] = 'X'
}

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
}

#[test]
fn test_read_board_size() {
    let file = File::open(&Path::new("test_read_board_size.txt"));
    let mut reader = BufferedReader::new(file);
    assert_eq!(read_board_size(&mut reader), (10, 20));
}
