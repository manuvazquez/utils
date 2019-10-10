import pathlib
from typing import Union

import scipy.io
import yaml


def matrix_to_yaml(
		input_file: pathlib.Path, variable: str, output_file: Union[str, pathlib.Path] = 'output.yaml',
		width: int = 200) -> None:
	"""
	Extract a matrix from a MATLAB file and write it to a text file in a format amenable to be included in a yaml file.

	Parameters
	----------
	input_file: pathlib object
		Input file
	variable: str
		Name of the variable
	output_file: str or pathlib object
		Output file
	width: int
		The maximum number of characters allowed in a line of text

	"""

	data = scipy.io.loadmat(input_file)

	with open(output_file, 'w') as f:

		for row in data[variable]:

			f.write('- ')

			yaml.dump(row.tolist(), f, default_flow_style=True, width=width)
