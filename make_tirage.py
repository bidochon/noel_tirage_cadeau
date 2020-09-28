import copy
import random
import numpy as np


class MakeTirage:

	families = [['Isabelle', 'Laurent', 'Kaina'],
	            ['Marie', 'Fabrice', 'Lyse'],
				['Nicolas', 'Kittie'],
	            ['Elodie', 'Maxime'],
	            ['Brigitte', 'Roland'],
	            ['Hassina', 'Jean', 'Rayan', 'Henia']]

	list_of_participants = {}

	secret_santa_list = {}

	def __init__(self):
		self.list_of_participants = {}
		self.secret_santa_list = {}

	def run(self):
		self.initialize_list_of_participants_dictionary()
		self.initialize_list_of_secret_santa()
		self.make_draw()

	def make_draw(self):
		list_of_participants = self.list_of_participants
		dict_santa_recipients = {}
		while(len(dict_santa_recipients) != len(list_of_participants)):
			dict_santa_recipients = {}
			list_of_participants = copy.deepcopy(self.list_of_participants)
			list_of_recipients_already_drawn = []
			for _member in self.secret_santa_list.keys():
				# print(f"_member is {_member}")
				list_of_participants_to_draw_from = list(list_of_participants.keys())
				for _recipients in list_of_recipients_already_drawn:
					if _recipients in list_of_participants_to_draw_from:
						list_of_participants_to_draw_from.remove(_recipients)
				# print(f"list_of_participants_to_draw_from: {list_of_participants_to_draw_from}")
				list_of_participants_to_remove = list_of_participants[_member]
				list_of_participants_to_remove.append(_member)
				# print(f"list_of_participants_to_remove: {list_of_participants_to_remove}")
				for _member_to_remove in list_of_participants_to_remove:
					if _member_to_remove in list_of_participants_to_draw_from:
						list_of_participants_to_draw_from.remove(_member_to_remove)
				# print(f"now list_of_participants_to_draw_from: {list_of_participants_to_draw_from}")
				rand_number_generated = np.int(random.random() * len(list_of_participants_to_draw_from))
				recipient_of_gift_is = list_of_participants_to_draw_from[rand_number_generated]
				list_of_recipients_already_drawn.append(recipient_of_gift_is)
				# print(f"{_member} will be the santa of {recipient_of_gift_is}")
				dict_santa_recipients[_member] = recipient_of_gift_is

		import pprint
		pprint.pprint(dict_santa_recipients)

	def initialize_list_of_participants_dictionary(self):
		for _family in self.families:
			for _member_of_family in _family:
				_key = _member_of_family
				rest_of_family_member = copy.deepcopy(_family)
				rest_of_family_member.remove(_key)
				self.list_of_participants[_key] = rest_of_family_member

	def initialize_list_of_secret_santa(self):
		for _member in self.list_of_participants:
			self.secret_santa_list[_member] = ""







