from primas import eh_prima, eh_numero_primo
from nose.tools import assert_false, assert_true

def test_palavra_a_nao_eh_prima():
	assert_false(eh_prima('a'))
	
def test_palavra_c_eh_prima():
	assert_true(eh_prima('c'))

def test_palavra_ab_eh_prima():
	assert_true(eh_prima('ab'))
	
def test_palavra_C_eh_prima():
	assert_true(eh_prima('C'))

def test_numeros_nao_primos():	
	assert_false(eh_numero_primo(0))
	assert_false(eh_numero_primo(1))
	assert_false(eh_numero_primo(4))
	assert_false(eh_numero_primo(6))
	assert_false(eh_numero_primo(9))

def test_numeros_primos():
	for n in (2, 3, 7, 13, 31):
		yield numero_primo, n

def numero_primo(n):
	assert_true(eh_numero_primo(n))