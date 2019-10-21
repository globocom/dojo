package dojo

import "testing"

var solucao = Caso {
	Assassino: 2,
	Local: 4,
	Arma: 3,
}

func TestTodosCorretos(t *testing.T) {
	if solucao.valida(solucao) > 0 {
		t.Error("Erro!!")
	}
}

func TestApenasAssassinoErrado(t *testing.T) {
	suspeita := Caso {
		Assassino: 1,
		Local: 4,
		Arma: 3,
	}
	if solucao.valida(suspeita) != 1 {
		t.Error("Assassino deveria estar errado!!")
	}
}

func TestApenasLocalErrado(t *testing.T) {
	suspeita := Caso {
		Assassino: 2,
		Local: 5,
		Arma: 3,
	}
	if solucao.valida(suspeita) != 2 {
		t.Error("Local deveria estar errado!!")
	}
}

func TestApenasArmaErrada(t *testing.T) {
	suspeita := Caso {
		Assassino: 2,
		Local: 4,
		Arma: 1,
	}
	if solucao.valida(suspeita) != 3 {
		t.Error("Arma deveria estar errada!!")
	}
}

func TestAssassinoELocalErrados(t *testing.T) {
	suspeita := Caso {
		Assassino: 1,
		Local: 3,
		Arma: 3,
	}
	resultado := solucao.valida(suspeita)
	if resultado != ErroAssassino && resultado != ErroLocal {
		t.Error("Assassino e Local deveriam estar errados!!")
	}
}

func TestTodosErrados(t *testing.T) {
	suspeita := Caso {
		Assassino: 3,
		Local: 2,
		Arma: 4,
	}
	resultado := solucao.valida(suspeita)
	if resultado != ErroAssassino &&
		resultado != ErroLocal &&
		resultado != ErroArma {
		t.Error("Todos deveria estar errados!!")
	}
}