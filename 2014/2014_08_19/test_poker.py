#coding: utf-8
import unittest
from poker import play_poker, check_pairs, get_highest_card, Card


class PokerTestCase(unittest.TestCase):

	def test_card_compare(self):
		card1 = Card(u"4♣")
		card2 = Card(u"9♣")
		card3 = Card(u"10♣")
		card4 = Card(u"J♣")
		self.assertTrue(card2 > card1)
		self.assertTrue(card3 > card2)
		self.assertTrue(card4 > card3)

	def test_highest_card(self):
		person1 = [u"4♣", u"2♥", u"A♦", u"10♠", u"5♠"]
		person2 = [u"3♣", u"6♥", u"7♦", u"4♠", u"2♠"]
		computed = play_poker(person1, person2)
		expected = "Person 1 won"
		self.assertEqual(computed, expected)

	def test_one_pair_person1(self):
		person1 = [u"3♣", u"3♥", u"7♦", u"4♠", u"2♠"]
		person2 = [u"2♣", u"2♥", u"A♦", u"10♠", u"5♠"]
		computed = play_poker(person1, person2)
		expected = "Person 1 won"
		self.assertEqual(computed, expected)

	def test_one_pair_person2(self):
		person1 = [u"4♣", u"2♥", u"A♦", u"10♠", u"5♠"]
		person2 = [u"3♣", u"3♥", u"7♦", u"4♠", u"2♠"]
		computed = play_poker(person1, person2)
		expected = "Person 2 won"
		self.assertEqual(computed, expected)

	def test_check_one_pair(self):
		person = [u"3♣", u"3♥", u"7♦", u"4♠", u"2♠"]
		self.assertEqual(["3"], check_pairs(person))

	def test_check_no_pair(self):
		person = [u"3♣", u"9♥", u"7♦", u"4♠", u"2♠"]
		self.assertEqual([], check_pairs(person))

	def test_get_highest_card(self):
		person = [u"4♣", u"2♥", u"7♦", u"9♠", u"5♠"]
		computed = get_highest_card(person)
		expected = "9"
		self.assertEqual(computed, expected)

if __name__ == "__main__":
	unittest.main()