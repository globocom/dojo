#coding:utf-8
def collatz(numero):
	total = 1
	while numero != 1:
		if numero % 2 == 0:
			numero = numero/2
		else:
			numero = numero * 3 + 1

		total+=1
	
	return total
	
def maior_de_todos(numero):
	maior_sequencia = 0
	maior_numero = 0
	for i in xrange(1, numero):
		total_collatz = collatz(i)
		if total_collatz > maior_sequencia:
			maior_sequencia = total_collatz
			maior_numero = i
	
	return o_numero
	
if __name__ == '__main__':
	print maior_de_todos(1000000)