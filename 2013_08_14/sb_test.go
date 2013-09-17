package sb

import "testing"

func TestTahVazio(t *testing.T) {
	b := Barbearia{
		fila:     make(chan string, 2),
		barbeiro: make(chan string, 1),
	}
	status := b.Entrar("Robert")
	if status != "Robert está sendo atendido." {
		t.Error("Robert deveria estar 'em atendimento'")
	}
}

func TestCheio(t *testing.T) {
	b := Barbearia{
		fila:     make(chan string, 2),
		barbeiro: make(chan string, 1),
	}
	b.Entrar("Robert")
	b.Entrar("Roberto")
	b.Entrar("Roberta")

	status := b.Entrar("Aline")
	if status != "Aline desistiu." {
		t.Error("Aline deveria ter desistido")
	}
}

func TestFilaEspera(t *testing.T) {
	b := Barbearia{
		fila:     make(chan string, 2),
		barbeiro: make(chan string, 1),
	}
	b.Entrar("Roberto")
	status := b.Entrar("Alice")
	if status != "Alice está esperando." {
		t.Error("Alice deveria estar esperando")
	}
}
