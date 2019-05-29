def ana_eat(bill, item):
	del bill[item]
	return bill

def bill_person(bill):
	return sum(bill) / 2

def main(bill, item, paid):
	new_bill = ana_eat(bill, item)
	avg = bill_person(new_bill)
	cashback = paid - avg
	return cashback if cashback != 0 else "Bon Appetit"
	
