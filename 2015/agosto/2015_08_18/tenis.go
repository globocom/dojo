package tenis

import "errors"

type Match struct {
	gameScores []int
	setScores  []int
	advantage  int
}

type Score struct {
	set  []int
	game []string
}

func newMatch() Match {
	return Match{gameScores: make([]int, 2), setScores: make([]int, 2), advantage: -1}
}

func (m *Match) Point(player int) error {
	playerIndex := player - 1
	otherPlayerIndex := (playerIndex + 1) % 2
	if playerIndex < 0 || playerIndex > 1 {
		return errors.New("invalid player")
	}
	if m.gameScores[playerIndex] == 3 && m.gameScores[otherPlayerIndex] == 3 {
		return m.handleDeuce(playerIndex, otherPlayerIndex)
	}
	m.gameScores[playerIndex]++
	if m.gameScores[playerIndex] == 4 {
		m.winGame(playerIndex)
	}
	return nil
}

func (m *Match) winGame(playerIndex int) {
	m.setScores[playerIndex]++
	m.gameScores = []int{0, 0}
	m.advantage = -1
}

func (m *Match) handleDeuce(playerIndex, otherPlayerIndex int) error {
	switch m.advantage {
	case -1:
		m.advantage = playerIndex
	case playerIndex:
		m.winGame(playerIndex)
	case otherPlayerIndex:
		m.advantage = -1
	}
	return nil
}

func (m *Match) Score() Score {
	gameScoreValues := []string{"0", "15", "30", "40"}
	gameScore := []string{
		gameScoreValues[m.gameScores[0]],
		gameScoreValues[m.gameScores[1]],
	}

	if m.advantage > -1 && m.advantage < 2 {
		gameScore[m.advantage] += " ADV"
	}
	return Score{
		set:  m.setScores,
		game: gameScore,
	}
}
