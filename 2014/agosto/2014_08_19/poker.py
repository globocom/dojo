#coding: utf-8
class Card(object):

	def __init__(self, card):
		self.value = card[:-1]
		self.suit = card[-1]


	def __gt__(self, other):
		return ord(self.value) > ord(other.value)

	def __lt__(self, other):
		return self.value < other.value		

def play_poker(person1, person2):
	pairs_person1 = check_pairs(person1)
	pairs_person2 = check_pairs(person2)
	if len(pairs_person1) == 0 and len(pairs_person2) == 0:
		if get_highest_card(person1) > get_highest_card(person2):
			return "Person 1 won"
		else:
			return "Person 2 won"
	if len(pairs_person1) == len(pairs_person2):
		if pairs_person1[0] > pairs_person2[0]:
			return "Person 1 won"
	return "Person 2 won"

def check_pairs(person):
	cards = remove_suit(person)
	pairs = set()
	for card in cards:
		if cards.count(card) == 2:
			pairs.add(card)

	return list(pairs)

def get_highest_card(person):
	cards = remove_suit(person)
	return max(cards)

def remove_suit(person):
	cards = []
	for card in person:
		cards.append(card[:-1])
	return cards