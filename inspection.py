from typing import List
import inspect


def get_concrete_classes(module, class_name: str) -> List[str]:

	# the name of the class is used to get the actual class (Python object)
	c = getattr(module, class_name)

	# only if the class is not abstract, must it be added to the result
	res = [class_name] if not inspect.isabstract(c) else []

	# if the passed class has no subclasses...
	if not c.__subclasses__():

		return res

	# if the passed class has subclasses...
	else:

		res += [class_name for subclass in c.__subclasses__() for class_name in get_concrete_classes(
			module, subclass.__name__)]

	return res
