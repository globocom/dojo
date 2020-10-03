#coding: utf-8


CARD_VALUES = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]


class Card(object):

	def __init__(self, card):
		self.value = card[:-1]
		self.suit = card[-1]

	def __gt__(self, other):
		return CARD_VALUES.index(self.value) > CARD_VALUES.index(other.value)

	def __lt__(self, other):
		return not self.__gt__(other)


def play_poker(person1, person2):
	score_person1 = score(person1)
	score_person2 = score(person2)
	if score_person1 > score_person2:
		return "Person 1 won"
	elif score_person1 < score_person2:
		return "Person 2 won"
	else:
		return "Tie"

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

def score(person):
	pairs = check_pairs(person)
	if pairs:
		person = remove_suit(person)
		person.remove(pairs[0])
		person.remove(pairs[0])
		return 100 + CARD_VALUES.index(pairs[0]) + (get_highest_card(map(lambda x: x+"2", person)) * 0.01)
	else:
		return CARD_VALUES.index(get_highest_card(person))
