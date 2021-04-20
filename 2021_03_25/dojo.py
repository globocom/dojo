def main():
		pass

def calc_golpe(b, at):
	ataque = (at[0] + at[1])/2
	if at[2] % 2 == 0:
		return ataque + b
	return ataque

def ganhador(b, at1, at2):
	return "guarte"