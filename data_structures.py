# from https://stackoverflow.com/a/20666342/3967334
def merge_lhs_dict_into_rhs(source: dict, destination: dict) -> dict:
	"""
	run me with nosetests --with-doctest file.py

	>>> a = { 'first' : { 'all_rows' : { 'pass' : 'dog', 'number' : '1' } } }
	>>> b = { 'first' : { 'all_rows' : { 'fail' : 'cat', 'number' : '5' } } }
	>>> merge_lhs_dict_into_rhs(b, a) == { 'first' : { 'all_rows' : { 'pass' : 'dog', 'fail' : 'cat', 'number' : '5' } } }
	True
	"""
	for key, value in source.items():
		if isinstance(value, dict):
			# get node or create one
			node = destination.setdefault(key, {})
			merge_lhs_dict_into_rhs(value, node)
		else:
			destination[key] = value

	return destination
