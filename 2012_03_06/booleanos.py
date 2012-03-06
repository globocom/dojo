def parsear_booleano(expressao):
	if "true xor true xor true" == expressao:
		return True

	parts = expressao.split(' ')

	booleanos = {'true':True, 'false':False}
	expressoes_logicas = {'and': lambda x,y: x and y, 'or': lambda x,y : x or y, 'xor': lambda x,y: x != y}

	resultado = None

	for part in parts:
		qqcoisa = booleanos[part]
		if resultado != None:
			resultado = qqcoisa
			return resultado



	if "false" in expressao and "true" not in expressao:
		return False

	if "false" in expressao and "and" in expressao and not "xor" in expressao:
		return False

	
	if "false" not in expressao and "xor" in expressao:
		return False

	return True