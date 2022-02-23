function part1(directions) {
  const initialPosition = [0, 0];
  const position = new Set();
  position.add("0-0");

  for (const c of directions) {
    if (c == ">") {
      initialPosition[0] += 1;
    } else if (c == "<") {
      initialPosition[0] -= 1;
    } else if (c == "^") {
      initialPosition[1] += 1;
    } else if (c == "v") {
      initialPosition[1] -= 1;
    }

    position.add(
      new String(initialPosition[0]) + "-" + new String(initialPosition[1])
    );
  }

  return position.size;
}

function part2_before_refactor(directions) {
  const initialPosition1 = [0, 0];
  const initialPosition2 = [0, 0];
  const position = new Set();
  position.add("0-0");

  for (let i = 0; i < directions.length; i++) {
    let c = directions[i];
    if (i % 2 == 0) {
      if (c == ">") {
        initialPosition1[0] += 1;
      } else if (c == "<") {
        initialPosition1[0] -= 1;
      } else if (c == "^") {
        initialPosition1[1] += 1;
      } else if (c == "v") {
        initialPosition1[1] -= 1;
      }

      position.add(
        new String(initialPosition1[0]) + "-" + new String(initialPosition1[1])
      );
    } else {
      if (c == ">") {
        initialPosition2[0] += 1;
      } else if (c == "<") {
        initialPosition2[0] -= 1;
      } else if (c == "^") {
        initialPosition2[1] += 1;
      } else if (c == "v") {
        initialPosition2[1] -= 1;
      }
      position.add(
        new String(initialPosition2[0]) + "-" + new String(initialPosition2[1])
      );
    }
  }

  return position.size;
}

// Refactored
function part2(directions) {
  positions = [
    [0, 0],
    [0, 0],
  ]; // [SantaPosition, RobotPosition]
  visited = new Set();
  visited.add(positions[0].toString());

  for (let i = 0; i < directions.length; i++) {
    let c = directions[i];

    if (c == ">") {
      positions[i % 2][0] += 1;
    } else if (c == "<") {
      positions[i % 2][0] -= 1;
    } else if (c == "^") {
      positions[i % 2][1] += 1;
    } else if (c == "v") {
      positions[i % 2][1] -= 1;
    }
    visited.add(positions[i % 2].toString());
  }
  return visited.size;
}

module.exports = { part1, part2 };

/*
Sara
Thiago
Christian
Pedro
Raphael
Gabriel
Guilherme
*/

/*
.....
..X#.
.OXX.
.....
*/

// ><>>^<>
