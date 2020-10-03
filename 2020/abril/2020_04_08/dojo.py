def main(extensive):

	extensive_lower = extensive.lower() 

	extensive_dict = {
		"zero":0,
		"um":1,
		"dois":2,
		"três":3,
		"quatro":4,
		"cinco":5,
		"seis":6,
		"sete":7,
		"oito":8,
		"nove":9,
		"dez":10,
		"vinte":20,
		"trinta":30,
		"quarenta":40,
		"cinquenta":50,
		"sessenta":60,
		"setenta":70,
		"oitenta":80,
		"noventa":90,
	}

	if extensive_lower in extensive_dict.keys():
		return extensive_dict[extensive_lower]

def get_extensive_list(extensive):
	extensive_list = extensive.split(" e ")
	return extensive_list

	