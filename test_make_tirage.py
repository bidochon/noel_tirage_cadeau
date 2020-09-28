from make_tirage import MakeTirage


def test_initialize_list_of_participants():
	o_make = MakeTirage()
	o_make.initialize_list_of_participants_dictionary()
	list_of_participants_calculated = o_make.list_of_participants
	list_of_participants_expected = {}
	list_of_participants_expected['Isabelle'] = ['Laurent', 'Kaina']
	list_of_participants_expected['Nicolas'] = ['Kittie']
	list_of_participants_expected['Jean'] = ['Hassina', 'Rayan', 'Henia']
	list_of_participants_expected['Roland'] = ['Brigitte']
	list_of_participants_expected['Lyse'] = ['Fabrice', 'Marie']

	for _member in list_of_participants_expected.keys():
		for _other_members in list_of_participants_expected[_member]:
			assert _other_members in list_of_participants_calculated[_member]

def test_initialize_list_of_secret_santa():
	o_make = MakeTirage()
	o_make.initialize_list_of_participants_dictionary()
	o_make.initialize_list_of_secret_santa()
	secret_santa_list_calculated = o_make.secret_santa_list
	secret_santa_list_expected = {}
	for _family in o_make.families:
		for _member_of_family in _family:
			secret_santa_list_expected[_member_of_family] = ""

	assert len(secret_santa_list_expected) == len(secret_santa_list_expected)
	for _member in secret_santa_list_expected.keys():
		secret_santa_list_expected[_member] == secret_santa_list_calculated[_member]

def test_make_draw():
	o_make = MakeTirage()
	o_make.initialize_list_of_participants_dictionary()
	o_make.initialize_list_of_secret_santa()
	o_make.make_draw()
