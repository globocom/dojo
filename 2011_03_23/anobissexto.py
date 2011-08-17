def eh_ano_bissexto(ano):
	return (ano % 4 == 0 and not ano % 100 == 0) or ano % 400 == 0